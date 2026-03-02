"""
run_pipeline.py

Entry point for executing the full PySpark knowledge discovery pipeline.
"""

from pyspark.sql import SparkSession

def main():
    spark = (
        SparkSession.builder
        .appName("Large-Scale-Knowledge-Discovery-Pipeline")
        .getOrCreate()
    )

    print("Pipeline started successfully.")
    # Pipeline execution logic goes here

    spark.stop()

if __name__ == "__main__":
    main()
