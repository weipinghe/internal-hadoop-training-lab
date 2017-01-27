# spark streaming example
#
# In a new terminal run the following command to start outputting data:
# $ nc -lkv 9999
# a. Start typing words separated by space, hit return occasionally to submit them.
# b. Look at the other terminal where the streaming application is running.
# c. While the application is running, navigate to the web UI in Firefox and explore the
# web UI tabs:
# myhostname:4040
# d. To quit the streaming application, press control-d, control-c for the terminal
# running nc.

sc.setLogLevel("WARN")
from pyspark.streaming import StreamingContext
ssc = StreamingContext(sc, 5)
inputDS = ssc.socketTextStream("myhostname",9999)
c = inputDS.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda a,b: a+b)
c.pprint()
ssc.start()
