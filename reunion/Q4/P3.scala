import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder()
  .appName("JSON Files Ingestion")
  .getOrCreate()

val streamingDF = spark.readStream
  .option("inferSchema", "true") // Automatically infer the schema
  .json("https://reunion223.s3.ap-northeast-1.amazonaws.com/json_files.zip")
