FROM openjdk:11-jre-slim

ENV SPARK_VERSION=3.5.8
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

RUN apt-get update && apt-get install -y python3 python3-pip wget && rm -rf /var/lib/apt/lists/*

RUN wget https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz &&     tar -xzf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz &&     mv spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION $SPARK_HOME &&     rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz

RUN pip3 install pyspark==$SPARK_VERSION numpy pandas matplotlib scikit-learn findspark

WORKDIR /app

COPY . /app

CMD ["python3"]
