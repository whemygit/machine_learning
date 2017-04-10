#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
from numpy import *
reload(sys)
sys.setdefaultencoding("utf-8")


def loadDataSet():
    dataMat=[];labelMat=[]
    with open('D://myfile/machine_learning_code/machinelearninginaction/Ch05/testSet.txt','r') as fr:
        for line in fr.readlines():
            lineArr=line.strip().split()
            dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
            labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn,classLabels):
    dataMatrix=mat(dataMatIn)
    labelMat=mat(classLabels).transpose()
    m,n=shape(dataMatrix)
    alpha=0.001
    maxCycles=500
    weights=ones((n,1))
    for k in range(maxCycles):
        h=sigmoid(dataMatrix*weights)                    #每行求和取sigmoid
        error=(labelMat-h)
        weights=weights+alpha*dataMatrix.transpose()*error
    # print error
    # print weights
    return weights

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    # weights=wei.getA()
    dataMat,labelMat=loadDataSet()
    dataArr=array(dataMat)
    n=shape(dataArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if int(labelMat[i])==1:
            xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]);ycord2.append(dataArr[i,2])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x=arange(-3.0,3.0,0.1)
    y=(-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel('x1');plt.ylabel('x2')
    plt.show()

def stocGradAscent0(dataMatrix,classLabels):
    m,n=shape(dataMatrix)
    alpha=0.01
    weights=ones(n)
    for i in range(1):
        h=sigmoid(sum(dataMatrix[i]*weights))
        # print '1',dataMatrix[i]
        # print '2',h
        error=classLabels[i]-h
        # print '3',classLabels[i]
        # print '4',error
        # print error*array(dataMatrix[i])
        # print type(array(dataMatrix))
        weights=weights+alpha*error*array(dataMatrix[i])
    return weights


def stocGradAscent1(dataMatrix,classLabels,numIter=150):
    m,n=shape(dataMatrix)
    weights=ones(n)
    for j in range(numIter):
        dataIndex=range(m)
        for i in range(m):
            alpha=4/(1.0+j+i)+0.01
            randIndex=int(random.uniform(0,len(dataIndex)))
            h=sigmoid(sum(dataMatrix[randIndex]*weights))
            error=classLabels[randIndex]-h
            weights=weights+alpha*error*array(dataMatrix[randIndex])
            del(dataIndex[randIndex])
    return weights






if __name__ == '__main__':
    dataMat, labelMat=loadDataSet()
    weights=stocGradAscent1(dataMat, labelMat)
    plotBestFit(weights)