#!/bin/bash
# Environment setup script for PySpark pipeline

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$JAVA_HOME/bin:$PATH

echo "Environment variables set successfully."
