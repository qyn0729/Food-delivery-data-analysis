from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession, HiveContext
from pyspark.sql.types import *
from pyspark.sql import Row

orcPath = "D:\\aMyFile\\Data\\Takeout\\data\\Dianwoda\\part-00000-8a7fb249-6bae-4a4e-aa5e-624f83552d84.snappy.orc";

spark = SparkSession.builder.config("spark.driver.host", "localhost").appName("OrcFileTest").master("local").getOrCreate();

df = spark.read.orc(orcPath)
df.createOrReplaceTempView("order")
sqldf = spark.sql("with leave as (select * from order where status='leave'),"
                      "finish as (select * from order where status='finish')"
                      "select leave.order_id as order_id, leave.timestamp as leave_time, leave.rider_id as leave_rider, leave.latitude/1000000 as leave_latitude, leave.longitude/1000000 as leave_longitude, finish.timestamp as finish_time, finish.rider_id as finish_rider, finish.latitude/1000000 as finish_latitude, finish.longitude/1000000 as finish_longitude from leave full join finish where leave.order_id = finish.order_id")

files = ["part-00000-48c1a0b7-6ab4-4731-ab2a-cb9c01f595bc.snappy.orc", "part-00000-2013ceb0-7435-4120-bfb4-b0b4bc984776.snappy.orc", "part-00000-5987e821-df34-4b34-84b0-9ab8bec091b7.snappy.orc", "part-00000-c616e08f-02f3-464c-a3d9-8f786dcaf48d.snappy.orc", "part-00000-f45ff5dc-3d79-4e8a-aed2-789d83ac177a.snappy.orc"]

for filename in files:
    orcPath = "D:\\aMyFile\\Data\\Takeout\\data\\Dianwoda\\"+ filename;
    df = spark.read.orc(orcPath)
    df.createOrReplaceTempView("order")
    tmpdf = spark.sql("with leave as (select * from order where status='leave'),"
                      "finish as (select * from order where status='finish')"
                      "select leave.order_id as order_id, leave.timestamp as leave_time, leave.rider_id as leave_rider, leave.latitude/1000000 as leave_latitude, leave.longitude/1000000 as leave_longitude, finish.timestamp as finish_time, finish.rider_id as finish_rider, finish.latitude/1000000 as finish_latitude, finish.longitude/1000000 as finish_longitude from leave full join finish where leave.order_id = finish.order_id")
    tmpdf.show()
    sqldf = sqldf.unionAll(tmpdf)
    print(sqldf.count())

print(sqldf.count())
sqldf.repartition(1).write.mode("append").option("header", "true").csv("allorder.csv")