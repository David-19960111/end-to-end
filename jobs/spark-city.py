from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("SmartCityStreaming") \
    .config("spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.13:3.5.0,"
            "org.apache.hadoop:hadoop-aws:3.3.1,"
            "com.amazonaws:aws-java-sdk:1.11.469") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.access.key", configuration.get('AWS_ACCESS_KEY')) \
    .config("spark.hadoop.fs.s3a.access.key", configuration.get('AWS_SECRET_KEY')) \
    .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.impl.SimpleAWSCredentialProvider') \
    .getOrCreate()

    spark.sparkContext.setLogLevel('WARN')

    vehicleSchema = StructType([
        StructType("id", StringType(),
                   )
    ])




if __name__ == "__main__":
    main()