# How to run
# 1. Create a Kafka topic wordcounttopic and pass in your ZooKeeper server
# kafka-topics --create --zookeeper localhost:2181 --topic wordcounttopic --partitions 1 --replication-factor 1

# pyspark to run
from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 5)
kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', "spark-streaming-consumer", {wordcounttopic: 1})
lines = kafkaStream.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
counts.pprint()
ssc.start()
ssc.awaitTermination()


# In another window, start a Kafka producer that publishes to wordcounttopic:
# $ kafka-console-producer --broker-list localhost:6667 --topic wordcounttopic
