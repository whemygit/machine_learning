#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors,datasets
from sklearn.model_selection import train_test_split

reload(sys)
sys.setdefaultencoding("utf-8")

def load_classification_data():
    digits=datasets.load_digits()
    x_train=digits.data
    y_train=digits.target
    return train_test_split(x_train,y_train,test_size=0.25,random_state=0,stratify=y_train)


def create_data(n):
    np.random.seed(0)
    X=5*np.random.rand(n,1)
    Y=np.sin(X).ravel()
    noise_num=(int)(n/5)
    try:
        Y[::5]+=1*(0.5-np.random.rand(noise_num))
    except ValueError as err:
        Y[::5] +=1* (0.5 - np.random.rand(noise_num+1))              #非5的整数倍时，长度不一致。len（Y[::5]）比noise_num多1
    return train_test_split(X,Y,test_size=0.25,random_state=1)

def test_KNeighborsClassifier(*data):
    x_train,x_test,y_train,y_test=data
    clf=neighbors.KNeighborsClassifier()
    clf.fit(x_train,y_train)
    print "training score:%f" % clf.score(x_train,y_train)
    print "testing score:%f" % clf.score(x_test,y_test)

if __name__ == '__main__':
    x_train, x_test, y_train, y_test=load_classification_data()
    test_KNeighborsClassifier(x_train,x_test,y_train,y_test)