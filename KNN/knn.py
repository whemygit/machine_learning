#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass
######################################################################################
#实验数据
from numpy import *
import operator

def createDataSet():
    '''实验数据获取'''
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels

group,labels=createDataSet()
# print labels
# print group



def classify0(inX,dataSet,labels,k):
    dataSetSize=shape(dataSet)[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet           #以inX为元素，构建(dataSetSize,1)形状的矩阵，然后计算两矩阵差
    sqDiffMat=diffMat**2                                #以各元素平方为元素组成的平方矩阵
    sqDistances=sqDiffMat.sum(axis=1)                   #行方向上求和
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()               #对distances由小到大排列的索引值
    classCount={}
    for i in range(k):
        voteILabel=labels[sortedDistIndicies[i]]          #所在类的标签
        classCount[voteILabel]=classCount.get(voteILabel,0)+1
    sortedClassCount=sorted(classCount.iteritems(),
                            key=operator.itemgetter(1),reverse=True)   #字典转换为列表，倒序排序
    return sortedClassCount[0][0]

b=classify0([0,0],group,labels,3)
# print b

#####################################################################################
# examples:improving matches from a dating site with kNN

#text record to Numpy Parsing code
def file2matrix(filename):
    import numpy
    '''读取文件数据，前三列读为矩阵，最后一列读为标签向量'''
    with open(filename) as fr:
        numberOfLines=len(fr.readlines())
        returnMat=zeros((numberOfLines,3))
        classLabelVector=[]
        with open(filename) as fr:                                                #一定要重新打开一次！！！！！！！不然写不进去。。。。。。。。
            index=0
            for line in fr.readlines():
                line=line.strip()
                listFromLine=line.split('\t')
                returnMat[index,:]=listFromLine[0:3]
                classLabelVector.append(int(listFromLine[-1]))
    print shape(returnMat)
    print len(classLabelVector)
    return returnMat,classLabelVector


#获取数据
datingDataMat,datingLabels=file2matrix("D://myfile/machine_learning_code/machinelearninginaction/Ch02/datingTestSet2.txt")
# print datingDataMat


#图形展示
import matplotlib
import matplotlib.pyplot as plt
fig=plt.figure()                             #创建图表对象
ax=fig.subplot(111)                          #添加坐标
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()