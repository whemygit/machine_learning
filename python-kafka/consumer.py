#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from kafka import KafkaConsumer
reload(sys)
sys.setdefaultencoding("utf-8")

consumer=KafkaConsumer('sex')
for msg in consumer:
    print msg.value.decode('utf-8')

# if __name__ == '__main__':
#     pass