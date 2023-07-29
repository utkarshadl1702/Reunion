
val query = streamingDF.writeStream
  .outputMode("append") // change the output mode depending on your requirements
  .format("parquet") // change the format based on your preferences
  .option("checkpointLocation", "<checkpoint_location>") // Specify a checkpoint location
  .table(tableName)
  .trigger(processingTime = "1 minute") // Set the desired trigger interval
