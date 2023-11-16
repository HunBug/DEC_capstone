from confluent_kafka import Consumer
from pathlib import Path
import csv
import base64
import time


def encode_base64(data):
    """Encode data in base64 if it's not None."""
    if data is not None:
        return base64.b64encode(data).decode("utf-8")
    return None


def read_ccloud_config(config_file: Path) -> dict:
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split("=", 1)
                conf[parameter] = value.strip()
    return conf


if __name__ == "__main__":
    client_properties = read_ccloud_config(Path("client.properties"))
    topics = ["wiki_create_trans"]
    client_properties["group.id"] = "wiki_reader"
    client_properties["auto.offset.reset"] = "earliest"
    consumer = Consumer(client_properties)
    consumer.subscribe(topics)
    max_messages = 100
    with open("kafka_dump.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(
            [
                "key",
                "value",
                "topic",
                "partition",
                "offset",
                "timestamp",
                "timestampType",
            ]
        )

        count = 0
        while count < max_messages:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            # Encode key and value in base64
            key_b64 = encode_base64(msg.key())
            value_b64 = encode_base64(msg.value())

            # Extract other message attributes
            writer.writerow(
                [
                    key_b64,
                    value_b64,
                    msg.topic(),
                    msg.partition(),
                    msg.offset(),
                    time.strftime(
                        "%Y-%m-%d %H:%M:%S", time.localtime(msg.timestamp()[1] / 1000)
                    ),
                    msg.timestamp()[0],
                ]
            )
            count += 1

    consumer.close()
