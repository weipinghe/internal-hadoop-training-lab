import java.net.InetAddress;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
// Weiping He
// 2016/06/04 15:59:48

public class MyDNSCheck {
        public static void main(String[] args)  {
			 //disable DNS cache
			 //This code must execute before any other code in the JVM attempts to perform networking operations.
			 java.security.Security.setProperty("networkaddress.cache.ttl" , "0");
			 java.security.Security.setProperty("networkaddress.cache.negative.ttl" , "0");

			 DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
			 Date date = new Date();
			 System.out.println("Date: " + dateFormat.format(date)); //2016/06/04 15:59:48

			try {
    		  long before = System.currentTimeMillis();
              InetAddress addr = InetAddress.getByName("www.google.com");
              System. out.println(String.format( "IP:%s\nhostname:%s\ncanonicalName:%s", addr.getHostAddress(),  // The "default" IP address
                            addr.getHostName(), // The hostname (from gethostname())
                            addr.getCanonicalHostName() // The canonicalized hostname (from resolver)
              ));
             long after = System.currentTimeMillis();
			 System.out.println("DNS Query time: " + (after - before) + " ms\n");
		   }catch (Exception e) {
		    e.printStackTrace();
		   }
       }
}
