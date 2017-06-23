#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model,svm
from sklearn.model_selection import train_test_split

reload(sys)
sys.setdefaultencoding("utf-8")

def load_data_regression():
    diabetes = datasets.load_diabetes()
    return train_test_split(diabetes.data,datasets.target,test_size=0.25,random_state=0)

def load_data_classfication():
    iris=datasets.load_iris()
    x_train=iris.data
    y_train=iris.target
    return train_test_split(x_train,y_train,test_size=0.25,random_state=0,stratify=y_train)

def test_linearSVC(*data):
    x_train,x_test,y_train,y_test=data
    cls=svm.LinearSVC()
    cls.fit(x_train,y_train)
    print 'coefficients:%s, intercept:%s' %(cls.coef_,cls.intercept_)
    print 'score:%.2f' %cls.score(x_test,y_test)


def test_linearSVC_loss(*data):
    x_train,x_test,y_train,y_test=data
    losses=['hinge','squared_hinge']
    for loss in losses:
        cls=svm.LinearSVC(loss=loss)
        cls.fit(x_train,y_train)
        print 'loss:%s'%loss
        print 'coefficients:%s, intercept:%s' % (cls.coef_, cls.intercept_)
        print 'score:%.2f' % cls.score(x_test, y_test)

def test_linearSVC_l12(*data):
    x_train,x_test,y_train,y_test=data
    l12=['l1','l2']
    for p in l12:
        cls=svm.LinearSVC(penalty=p,dual=False)
        cls.fit(x_train,y_train)
        print 'penalty:%s'%p
        print 'coefficients:%s,intercept %s' %(cls.coef_,cls.intercept_)
        print 'score:%.2f'%cls.score(x_test,y_test)

def test_linearSVC_C(*data):
    x_train,x_test,y_train,y_test=data
    Cs=np.logspace(-2,1)
    train_scores=[]
    test_scores=[]
    for C in Cs:
        cls=svm.LinearSVC(C=C)
        cls.fit(x_train,y_train)
        train_scores.append(cls.score(x_train,y_train))
        test_scores.append(cls.score(x_test,y_test))

    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.plot(Cs,train_scores,label="training score")
    ax.plot(Cs,test_scores,label="testing score")
    ax.set_xlabel(r"C")
    ax.set_ylabel(r"score")
    ax.set_xscale('log')
    ax.set_title("LinearSVC")
    ax.legend(loc='best')
    plt.show()

def test_SVC_linear(*data):
    x_train,x_test,y_train,y_test=data
    cls=svm.SVC(kernel='linear')
    cls.fit(x_train,y_train)
    print 'coefficient %s,intercept %s'%(cls.coef_,cls.intercept_)
    print 'score: %.2f' %cls.score(x_test,y_test)

def test_SVC_poly(*data):
    x_train,x_test,y_train,y_test=data
    fig=plt.figure()
    degrees=range(1,20)
    train_scores=[]
    test_scores=[]
    for degree in degrees:
        cls=svm.SVC(kernel='poly',degree=degree)
        cls.fit(x_train,y_train)
        train_scores.append(cls.score(x_train,y_train))
        test_scores.append(cls.score(x_test,y_test))
    ax=fig.add_subplot(1,3,1)
    ax.plot(degrees,train_scores,label='training score',marker='+')
    ax.plot(degrees,test_scores,label='testing score',marker='o')
    ax.set_title('SVC_poly_degree')
    ax.set_xlabel('p')
    ax.set_ylabel('score')
    ax.set_ylim(0,1.05)
    ax.legend(loc='best',framealpha=0.5)

    gammas=range(1,20)
    train_scores=[]
    test_scores=[]
    for gamma in gammas:
        cls=svm.SVC(kernel='poly',gamma=gamma)
        cls.fit(x_train,y_train)
        train_scores.append(cls.score(x_train,y_train))
        test_scores.append(cls.score(x_test,y_test))
    ax=fig.add_subplot(1,3,2)
    ax.plot(gammas,train_scores,label='training score',marker='+')
    ax.plot(gammas,test_scores,label='testing score',marker='o')
    ax.set_title('SVC_poly_gamma')
    ax.set_xlabel(r'$\gamma$')
    ax.set_ylabel('score')
    ax.set_ylim(0,1.05)
    ax.legend(loc='best',framealpha=0.5)

    rs = range(1, 20)
    train_scores = []
    test_scores = []
    for r in rs:
        cls = svm.SVC(kernel='poly', gamma=10,degree=3,coef0=r)
        cls.fit(x_train, y_train)
        train_scores.append(cls.score(x_train, y_train))
        test_scores.append(cls.score(x_test, y_test))
    ax = fig.add_subplot(1, 3, 3)
    ax.plot(gammas, train_scores, label='training score', marker='+')
    ax.plot(gammas, test_scores, label='testing score', marker='o')
    ax.set_title('SVC_poly_r')
    ax.set_xlabel(r'r')
    ax.set_ylabel('score')
    ax.set_ylim(0, 1.05)
    ax.legend(loc='best', framealpha=0.5)

    plt.show()

def test_SVC_rbf(*data):
    x_train,x_test,y_train,y_test=data
    gammas=range(1,20)
    train_scores=[]
    test_scores=[]
    for gamma in gammas:
        cls=svm.SVC(kernel='rbf',gamma=gamma)
        cls.fit(x_train,y_train)
        train_scores.append(cls.score(x_train,y_train))
        test_scores.append(cls.score(x_test,y_test))
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.plot(gammas, train_scores, label='training score', marker='+')
    ax.plot(gammas, test_scores, label='testing score', marker='o')
    ax.set_title('SVC_rbf')
    ax.set_xlabel(r'$\gamma$')
    ax.set_ylabel('score')
    ax.set_ylim(0, 1.05)
    ax.legend(loc='best', framealpha=0.5)

    plt.show()


if __name__ == '__main__':
    x_train,x_test,y_train,y_test=load_data_classfication()
    # test_linearSVC(x_train,x_test,y_train,y_test)
    # test_linearSVC_loss(x_train,x_test,y_train,y_test)
    # test_linearSVC_l12(x_train,x_test,y_train,y_test)
    # test_linearSVC_C(x_train,x_test,y_train,y_test)
    # test_SVC_linear(x_train,x_test,y_train,y_test)
    # test_SVC_poly(x_train,x_test,y_train,y_test)
    test_SVC_rbf(x_train,x_test,y_train,y_test)

