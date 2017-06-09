#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import csv
import time
from kafka import KafkaProducer


reload(sys)
sys.setdefaultencoding("utf-8")

producer=KafkaProducer(bootstrap_servers='localhost:9092')
csvfile=open('user_log.csv','r')
reader=csv.reader(csvfile)

for line in reader:
    gender=line[9]
    if gender=='gender':
        continue
    time.sleep(0.1)
    producer.send('sex',line[9].encode('utf-8'))


# if __name__ == '__main__':
#     pass