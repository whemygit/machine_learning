#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from numpy import *
import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding("utf-8")

def loadDataSet(filename):
    numFeat=len(open(filename).readline().split('\t'))-1
    dataMat=[];labelMat=[]
    fr=open(filename)
    for line in fr.readlines():
        lineArr=[]
        curLine=line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def standRegres(xArr,yArr):
    xMat=mat(xArr);yMat=mat(yArr).T
    xTx=xMat.T*xMat
    if linalg.det(xTx)==0:
        print "this matrix is singular, cannot do inverse"
        return
    ws=xTx.I*(xMat.T*yMat)
    return ws

xArr,yArr=loadDataSet('D://myfile/machine_learning_code/machinelearninginaction/Ch08/ex0.txt')
ws=standRegres(xArr,yArr)

xMat=mat(xArr)
yMat=mat(yArr)
yHat=xMat*ws

fig=plt.figure()
ax=fig.add_subplot(111)
scat=ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])

xCopy=xMat.copy()
xCopy.sort(0)
yHat=xCopy*ws
ax.plot(xCopy[:,1],yHat)
# plt.show()

if __name__ == '__main__':
    print xArr[0:2]
    print ws
