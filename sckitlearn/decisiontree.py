#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding("utf-8")

def create_data(n):
    np.random.seed(0)
    X=5*np.random.rand(n,1)
    Y=np.sin(X).ravel()
    noise_num=(int)(n/5)
    try:
        Y[::5]+=(0.5-np.random.rand(noise_num))
    except ValueError as err:
        Y[::5] += (0.5 - np.random.rand(noise_num+1))              #非5的整数倍时，长度不一致。len（Y[::5]）比noise_num多1
    return train_test_split(X,Y,test_size=0.25,random_state=1)

def test_DecisionTreeRegressor(*data):
    x_train,x_test,y_train,y_test=data
    regr=DecisionTreeRegressor()
    regr.fit(x_train,y_train)
    print "training score:%f" %(regr.score(x_train,y_train))
    print "testing score:%f" %(regr.score(x_test,y_test))

#随机划分与最优划分的影响
def test_DecisionTreeRegressor_splitter(*data):
    x_train,x_test,y_train,y_test=data
    splitters=['best','random']
    for splitter in splitters:
        regr=DecisionTreeRegressor(splitter=splitter)
        regr.fit(x_train,y_train)
        print "Splitter ",splitter
        print "training score:%f" % (regr.score(x_train, y_train))
        print "testing score:%f" % (regr.score(x_test, y_test))
        # print x_test[0][0]
        print "model predict:%f" % (regr.predict(x_test[0][0]))


#决策树深度影响
def test_DecisionTreeRegressor_depth(x_train,x_test,y_train,y_test,maxdepth):
    # x_train,x_test,y_train,y_test=data
    depths=np.arange(1,maxdepth)
    training_scores=[]
    testing_scores=[]
    for depth in depths:
        regr=DecisionTreeRegressor(max_depth=depth)
        regr.fit(x_train,y_train)
        training_scores.append(regr.score(x_train,y_train))
        testing_scores.append(regr.score(x_test,y_test))

    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.plot(depths,training_scores,label="training score")
    ax.plot(depths,testing_scores,label="testing score")
    ax.set_xlabel("maxdepth")
    ax.set_ylabel("score")
    ax.set_title("decision tree regression")
    ax.legend(framealpha=0.5)
    plt.show()


if __name__ == '__main__':
    x_train,x_test,y_train,y_test=create_data(100)
    # test_DecisionTreeRegressor(x_train,x_test,y_train,y_test)
    test_DecisionTreeRegressor_splitter(x_train,x_test,y_train,y_test)
    # test_DecisionTreeRegressor_depth(x_train,x_test,y_train,y_test,maxdepth=20)

