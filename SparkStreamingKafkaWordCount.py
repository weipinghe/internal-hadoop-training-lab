# How to run
# 1. Create a Kafka topic wordcounttopic and pass in your ZooKeeper server
# /usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --zookeeper localhost:2181 --topic wordcounttopic --partitions 1 --replication-factor 1

# pyspark to run
from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc.setLogLevel("WARN")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: kafka_wordcount.py <zk> <topic>", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="PythonStreamingKafkaWordCount")
    ssc = StreamingContext(sc, 1)

    zkQuorum, topic = sys.argv[1:]
    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
    lines = kvs.map(lambda x: x[1])
    counts = lines.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a+b)
    counts.pprint()

    ssc.start()
    ssc.awaitTermination()



# In another window, start a Kafka producer that publishes to wordcounttopic:
# $ /usr/hdp/current/kafka-broker/bin/kafka-console-producer.sh --broker-list localhost:6667 --topic wordcounttopic

# spark-submit --jars /usr/hdp/2.5.0.0-1133/spark/lib/spark-streaming-kafka-assembly_2.10-1.6.0.jar \
# SparkStreamingKafkaWordCount.py \
# localhost:2181 wordcounttopic

