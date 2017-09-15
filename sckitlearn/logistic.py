#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
from sklearn import datasets,ensemble
from sklearn.model_selection import train_test_split
from sklearn import linear_model

reload(sys)
sys.setdefaultencoding("utf-8")

def load_data():
    iris=datasets.load_iris()
    x_train=iris.data
    y_train=iris.target
    return train_test_split(x_train, y_train, test_size=0.25, random_state=0, stratify=y_train)

def test_LogisticRegression(*data):
    x_train,x_test,y_train,y_test=data
    regr=linear_model.LogisticRegression()
    regr.fit(x_train,y_train)
    print 'coefficients:%s, intercept %s'%(regr.coef_,regr.intercept_)
    print 'score: %.2f' %regr.score(x_test,y_test)

def test_LogisticRegression_multinomial(*data):
    x_train,x_test,y_train,y_test=data
    regr=linear_model.LogisticRegression(multi_class='multinomial',solver='lbfgs')
    regr.fit(x_train,y_train)
    print 'coefficients:%s, intercept %s' % (regr.coef_, regr.intercept_)
    print 'score: %.2f' % regr.score(x_test, y_test)


if __name__ == '__main__':
    x_train,x_test,y_train,y_test=load_data()
    test_LogisticRegression(x_train,x_test,y_train,y_test)
    test_LogisticRegression_multinomial(x_train,x_test,y_train,y_test)