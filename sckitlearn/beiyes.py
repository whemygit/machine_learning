#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from sklearn import datasets,naive_bayes
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding("utf-8")

def show_digits():
    digits=datasets.load_digits()
    fig=plt.figure()
    print "vector from images 0",digits.data[0]
    for i in range(25):
        ax=fig.add_subplot(5,5,i+1)
        ax.imshow(digits.images[i],cmap=plt.cm.gray_r,interpolation='nearest')
    plt.show()


def load_data():
    digits=datasets.load_digits()
    return train_test_split(digits.data,digits.target,test_size=0.25,random_state=0)

def test_GaussianNB(*data):
    x_train,x_test,y_train,y_test=data
    cls=naive_bayes.GaussianNB()
    cls.fit(x_train,y_train)
    print "training score: %.2f" %cls.score(x_train,y_train)
    print "testint score: %.2f" %cls.score(x_test,y_test)

def test_MultinomialNB(*data):
    x_train,x_test,y_train,y_test=data
    cls=naive_bayes.MultinomialNB()
    cls.fit(x_train,y_train)
    print np.unique(y_test)
    print "training score: %.2f" %cls.score(x_train,y_train)
    print "testint score: %.2f" %cls.score(x_test,y_test)

def test_BernoulliNB(*data):
    x_train,x_test,y_train,y_test=data
    cls=naive_bayes.BernoulliNB()
    cls.fit(x_train,y_train)
    print "training score: %.2f" %cls.score(x_train,y_train)
    print "testint score: %.2f" %cls.score(x_test,y_test)
    print "predict test:",(cls.predict(x_train[0]))[0]


if __name__ == '__main__':
    x_train, x_test, y_train, y_test=load_data()
    # test_GaussianNB(x_train,x_test,y_train,y_test)
    # test_MultinomialNB(x_train, x_test, y_train, y_test)
    test_BernoulliNB(x_train, x_test, y_train, y_test)
