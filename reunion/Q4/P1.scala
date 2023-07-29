import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

val spark = SparkSession.builder()
  .appName("JSON Files Ingestion")
  .getOrCreate()

val jsonSchema = spark.read.json("<cloud_storage_path>/json_files.zip").schema

val streamingDF = spark.readStream
  .schema(jsonSchema)
  .json("https://reunion223.s3.ap-northeast-1.amazonaws.com/json_files.zip")
