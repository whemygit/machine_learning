#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import sys
import numpy as np
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding("utf-8")

def load_data():
    iris=datasets.load_iris()
    x_train=iris.data
    y_train=iris.target
    return train_test_split(x_train,y_train,test_size=0.25,random_state=0,stratify=y_train)

def test_DecisionTreeClassifier(*data):
    x_train,x_test,y_train,y_test=data
    clf=DecisionTreeClassifier()
    clf.fit(x_train,y_train)
    print "training score:%f" %(clf.score(x_train,y_train))
    print "testing score:%f" %(clf.score(x_test,y_test))

#考察评价切分质量的评价准则对于分类性能的影响
def test_DecisionTreeClassifier_criterion(*data):
    x_train,x_test,y_train,y_test=data
    criterions=['gini','entropy']
    for criterion in criterions:
        clf=DecisionTreeClassifier(criterion=criterion)
        clf.fit(x_train,y_train)
        print "criterion:%s" % criterion
        print "training score:%f" % (clf.score(x_train,y_train))
        print "testing score:%f" % (clf.score(x_test,y_test))


if __name__ == '__main__':
    x_train, x_test, y_train, y_test=load_data()
    # test_DecisionTreeClassifier(x_train, x_test, y_train, y_test)
    # test_DecisionTreeClassifier_criterion(x_train, x_test, y_train, y_test)
    clf=DecisionTreeClassifier()
    clf.fit(x_train,y_train)
    export_graphviz(clf,'out_clf.pdf')