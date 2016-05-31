import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.hdfs.DistributedFileSystem;
import org.apache.hadoop.hdfs.protocol.DatanodeInfo;
import org.apache.hadoop.hdfs.protocol.HdfsConstants.DatanodeReportType;

// Weiping 23:08 2016/05/30
// Run in Cloudera CDH
// /usr/java/jdk1.7.0_45-cloudera/bin/javac -classpath \
// "/opt/cloudera/parcels/CDH/lib/hadoop/*:/opt/cloudera/parcels/CDH/lib/hadoop/lib/*:/opt/cloudera/parcels/CDH/lib/hadoop-hdfs/*" \
// QueryLiveDatanodes.java

// /usr/java/jdk1.7.0_45-cloudera/bin/jar -cvf QueryLiveDatanodes.jar QueryLiveDatanodes.class
// mv QueryLiveDatanodes.jar /tmp
// cd /tmp

// export CLASSPATH="/opt/cloudera/parcels/CDH/lib/hadoop/*:\
// /opt/cloudera/parcels/CDH/lib/hadoop/lib/*:\
// /opt/cloudera/parcels/CDH/lib/hadoop-0.20-mapreduce/*:\
// /opt/cloudera/parcels/CDH/lib/hadoop-hdfs/*:."

// hadoop jar QueryLiveDatanodes.jar QueryLiveDatanodes


public class QueryLiveDatanodes {

   public static void main(String[] args) throws Exception {
		try {
		   final Configuration myconf = new Configuration();
	       DistributedFileSystem dfs = (DistributedFileSystem) FileSystem.get(myconf);
	       DatanodeInfo[] live = dfs.getDataNodeStats(DatanodeReportType.LIVE);
	       for (DatanodeInfo dn : live) {
	       	System.out.println(dn.getHostName());
	       }
		} catch(Exception e) {
			System.out.println(e);
			e.printStackTrace();
	   }

	}
}