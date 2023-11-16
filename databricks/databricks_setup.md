
2. Install Python Dependencies to cluster
Select your newly created cluster in the clusters tab and then select the Libraries tab. In that menu click on Install New and select the PyPI tab.
spark-nlp

In the same window as before, select Maven and enter these coordinates and hit install. These dependencies are required since even if you only want to run Spark NLP in Python it will invoke computations on the JVM which depend on the Spark NLP library.

com.johnsnowlabs.nlp:spark-nlp_2.12:5.1.4
com.clickhouse:clickhouse-jdbc:0.5.0
org.apache.hadoop:hadoop-aws:3.2.0