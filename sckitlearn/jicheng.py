#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,ensemble
from sklearn.model_selection import train_test_split

reload(sys)
sys.setdefaultencoding("utf-8")

def load_data_regression():
    diabetes=datasets.load_diabetes()
    return train_test_split(diabetes.data,diabetes.target,test_size=0.25,random_state=0)

def load_data_classification():
    digits=datasets.load_digits()
    return train_test_split(digits.data,digits.target,test_size=0.25,random_state=0)

def test_adaboost_classifier(*data):
    x_train,x_test,y_train,y_test=data
    clf=ensemble.AdaBoostClassifier(learning_rate=0.1)
    clf.fit(x_train,y_train)

    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    estimators_num=len(clf.estimators_)
    x=range(1,estimators_num+1)
    ax.plot(list(x),list(clf.staged_score(x_train,y_train)),label="training score")
    ax.plot(list(x),list(clf.staged_score(x_test,y_test)),label="testing score")
    ax.set_xlabel("estimator num")
    ax.set_ylabel("score")
    ax.legend(loc="best")
    ax.set_title("adaboostclassifier")
    plt.show()





if __name__ == '__main__':
    x_train,x_test,y_train,y_test=load_data_classification()
    test_adaboost_classifier(x_train,x_test,y_train,y_test)