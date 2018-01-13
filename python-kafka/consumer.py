#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from kafka import KafkaConsumer
reload(sys)
sys.setdefaultencoding("utf-8")


# consumer=KafkaConsumer('sex',bootstrap_servers='127.0.0.1:9092')
consumer = KafkaConsumer('sex',bootstrap_servers='127.0.0.1:9092')
for msg in consumer:
    print msg.value.decode('utf-8')

# if __name__ == '__main__':
#     pass