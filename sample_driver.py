'''
A self-contained PySpark script.

Run me with

$SPARK_HOME/spark-submit --master local sample_driver.py
'''
from pprint import pprint

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


def main(spark):
    CLICKSTREAM_FILE = '/path/to/clickstream_data/2015_01_en_clickstream.tsv.gz'
    clickstream = (spark.sparkContext.textFile(CLICKSTREAM_FILE)
                   .map(parse_line))
    clickstream_schema = StructType([
        StructField('prev_id', StringType()),
        StructField('curr_id', StringType()),
        StructField('views', IntegerType()),
        StructField('prev_title', StringType()),
        StructField('curr_title', StringType()),
    ])

    clickstream_df = spark.createDataFrame(clickstream, clickstream_schema)
    clickstream_df.createOrReplaceTempView('clickstream')
    pprint(spark.sql('SELECT * FROM clickstream LIMIT 10').collect())

def parse_line(line):
    '''Parse a line in the log file, but ensure that the 'n' or 'views' column is
    convereted to an integer.'''
    parts = line.split('\t')
    parts[2] = int(parts[2])
    return parts

if __name__ == '__main__':
    spark = (SparkSession.builder
             .appName('sample_driver')
             .getOrCreate())
    try:
        main(spark)
    finally:
        spark.stop()
