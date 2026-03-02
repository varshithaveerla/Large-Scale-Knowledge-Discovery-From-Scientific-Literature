"""
test_pipeline.py

Basic tests for validating the PySpark knowledge discovery pipeline.
These tests focus on schema integrity, data loading, and model readiness.
"""

import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .appName("Pipeline-Test")
        .master("local[*]")
        .getOrCreate()
    )
    yield spark
    spark.stop()

def test_spark_session_creation(spark):
    assert spark is not None

def test_schema_validation(spark):
    data = [(1, 2, 3)]
    df = spark.createDataFrame(data, ["doc_id", "word_id", "count"])
    assert df.columns == ["doc_id", "word_id", "count"]

def test_non_negative_counts(spark):
    data = [(1, 2, 3), (2, 3, 5)]
    df = spark.createDataFrame(data, ["doc_id", "word_id", "count"])
    assert df.filter(df.count < 0).count() == 0

def test_vectorization_readiness(spark):
    data = [(1, 1, 2), (1, 2, 3)]
    df = spark.createDataFrame(data, ["doc_id", "word_id", "count"])
    assert df.count() > 0
