val tableName = "your_table_name"

val query = streamingDF.writeStream
  .outputMode("append") // change the output mode depending on your requirements
  .format("parquet") // change the format based on your preferences
  .option("checkpointLocation", "<checkpoint_location>") // specify a checkpoint location
  .table(tableName)

query.awaitTermination()
