#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass
########################################################################################################################
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

########################################################################################################################
# examples:improving matches from a dating site with kNN

#text record to Numpy Parsing code
from numpy import *
def file2matrix(filename):
    '''读取文件数据，前三列读为矩阵，最后一列读为标签向量'''
    with open(filename) as fr:
        lines=fr.readlines()                                                        #重新赋值给变量很重要，否则还需再打开一次（即还需要执行line56）
        numberOfLines=len(lines)
        returnMat=zeros((numberOfLines,3))
        classLabelVector=[]
        # with open(filename) as fr:                                                #一定要重新打开一次！！！！！！！不然写不进去。。。。。。。。
        index=0
        for line in lines:
            line=line.strip()
            listFromLine=line.split('\t')
            returnMat[index,:]=listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1]))
            index+=1
    # print shape(returnMat)
    # print len(classLabelVector)
    return returnMat,classLabelVector

#获取数据
datingDataMat,datingLabels=file2matrix("D://myfile/machine_learning_code/machinelearninginaction/Ch02/datingTestSet2.txt")
# print datingDataMat
# print datingLabels
# print datingDataMat[2][1]

#图形展示
# import matplotlib
# import matplotlib.pyplot as plt
# fig=plt.figure()                             #创建图表对象
# ax=fig.add_subplot(111)                          #当前图表对象位置,等同于（1,1,1）
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
# plt.show()


#为了减小各变量量值不同的影响，进行归一化处理
def autoNorm(dataSet):
    # print dataSet
    minVals=dataSet.min(0)                 #0表示列方向,计算每列最小值
    # print minVals
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals                  #计算每列极差
    normDataset=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataset=dataSet-tile(minVals,(m,1))  #构建（m,1）结构的矩阵
    normDataset=normDataset/tile(ranges,(m,1))
    return normDataset,ranges,minVals


normMat,ranges,minVals=autoNorm(datingDataMat)
# print normMat
# print ranges
# print minVals

########################################################################################################################
#分类器针对约会网站的测试代码
def datingClassTest():
    hoRatio=0.10
    datingDataMat,datingLabels=file2matrix('D://myfile/machine_learning_code/machinelearninginaction/Ch02/datingTestSet2.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m=normMat.shape[0]
    numTestVecs=int(m*hoRatio)
    errorCount=0.0
    for i in range(numTestVecs):
        classfierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],
                                  datingLabels[numTestVecs:m],3)
        print "the classifier came back with: %d,the real answer is: %d" % (classfierResult,datingLabels[i])
        if classfierResult!=datingLabels[i]:errorCount+=1.0
    print "the total error rate is: %f" %(errorCount/float(numTestVecs))

# datingClassTest()

############################################################################################################
#约会网站预测函数
def classifyPerson():
    resultList=['not at all','in small doses','in large doses']
    percentTats=float(raw_input(
        "percentage of time spent playing video games"
    ))
    ffMiles=float(raw_input("frequent fliter miles earned per year"))
    iceCream=float(raw_input("liters of ice cream consumed per year"))
    datingDataMat,datingLabels=file2matrix('D://myfile/machine_learning_code/machinelearninginaction/Ch02/datingTestSet2.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    inArr=array([ffMiles,percentTats,iceCream])
    classfierResult=classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print "you will probably like this person:",resultList[classfierResult-1]

# classifyPerson()





