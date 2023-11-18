from sseclient import SSEClient
from confluent_kafka import Producer
import json
from pathlib import Path
import logging
import multiprocessing


def construct_event(event_data, user_types):
    # use dictionary to change assign namespace value and catch any unknown namespaces (like ns 104)
    event_data["namespace"] = event_data["namespace"]

    # assign user type value to either bot or human
    user_type = user_types[event_data["bot"]]

    # define the structure of the json event that will be published to kafka topic
    event = {
        "id": event_data["id"],
        "domain": event_data["meta"]["domain"],
        "namespace": event_data["namespace"],
        "title": event_data["title"],
        # "comment": event_data['comment'],
        "timestamp": event_data["meta"]["dt"],  # event_data['timestamp'],
        "user_name": event_data["user"],
        "user_type": user_type,
        # "minor": event_data['minor'],
        "old_length": event_data["length"]["old"],
        "new_length": event_data["length"]["new"],
    }

    return event


def read_ccloud_config(config_file: Path) -> dict:
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split("=", 1)
                conf[parameter] = value.strip()
    return conf


def read_source_config(config_file: Path) -> dict:
    with open(config_file) as fh:
        config = json.load(fh)
    return config


def delivery_callback(err, msg):
    if err:
        logging.error(f"Message failed delivery: {err}")
    else:
        logging.info(
            f"Message delivered to {msg.topic()} [{msg.partition()}] @ {msg.offset()}"
        )


def produce_events_from_url(
    url: str, topic_name: str, kafka_properties: dict, max_events: int = 100
):
    # get the multiprocessing logger with stderr stream handler added
    proc_logger = multiprocessing.log_to_stderr()
    # log all messages, debug and up
    proc_logger.setLevel(logging.INFO)
    proc_logger.info(f"Producing events from {url} to topic {topic_name}")
    producer = Producer(kafka_properties)
    messages_count = 0

    for event in SSEClient(url):
        if event.event == "message":
            try:
                event_data = json.loads(event.data)
            except ValueError:
                pass
            else:
                # event_to_send = construct_event(event_data, user_types)
                event_to_send = event_data
                producer.produce(
                    topic=topic_name,
                    key=json.dumps(event_to_send["meta"]["id"]).encode("utf-8"),
                    value=json.dumps(event_to_send).encode("utf-8"),
                    callback=delivery_callback,
                )
                producer.poll(0)
                proc_logger.debug(f"Produced event: {event_to_send}")

                messages_count += 1

        if max_events > 0 and messages_count >= max_events:
            proc_logger.info(
                f"Produced {messages_count} messages to Kafka topic {topic_name}. Exiting."
            )
            break
    producer.flush()


if __name__ == "__main__":
    max_events = 10000  # For safety, prevent this from running forever
    messages_count = 0

    client_properties = read_ccloud_config(Path("client.properties"))
    source_config = read_source_config(Path("source_config.json"))
    base_url: str = source_config["base_url"]
    streams: dict = source_config["streams"]

    # Create a process for each URL
    processes = []
    for topic, stream_name in streams.items():
        url = base_url + stream_name
        processes.append(
            multiprocessing.Process(
                target=produce_events_from_url,
                args=(url, topic, client_properties, max_events),
            )
        )

    logging.info(f"Starting {len(processes)} processes")
    # Start the processes
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
