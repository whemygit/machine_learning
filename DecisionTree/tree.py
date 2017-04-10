#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass


#计算给定数据集的香侬熵
from math import log
import operator

def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=1                                   #没有的时候先创建，初始值为0？？？？？应该为1
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt

########################################################################################################################
#测试
def createDataSet():
    dataSet=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']]
    labels=['no surfacing','flippers']
    return dataSet,labels

myDat,labels=createDataSet()
# print myDat
# print calcShannonEnt(myDat)

########################################################################################################################
#按照给定特征划分数据集
def splitDataSet(dataSet,axis,value):
    '''dataSet,待划分的数据集；axis，划分数据集的特征，即列；value，特征值，按列划分的依据，[axis]==value时的item表现'''
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])               #去掉axis列，并且,axis列的值等于value的矩阵
            retDataSet.append(reducedFeatVec)
    return retDataSet

# print splitDataSet(myDat,1,1)
# print splitDataSet(myDat,0,1)


#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    '''根据信息增益，即分类前与分类后熵值的差值（差值最大）衡量选择分类特征，初始值为分类标签'''
    numFeatures=len(dataSet[0])-1
    baseEntropy=calcShannonEnt(dataSet)
    bestInfoGain=0.0;bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEnt(subDataSet)                  #分类后的矩阵期望熵
        infoGain=baseEntropy-newEntropy
        if (infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

# print chooseBestFeatureToSplit(myDat)

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=1
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)            #字典转换为列表，倒序排序
    return sortedClassCount[0][0]

#创建树
def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    del (labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet
                                                (dataSet,bestFeat,value),subLabels)
    return myTree

# print createTree(myDat,labels)

def classify(inputTree,featLabels,testVec):
    firstStr=inputTree.keys()[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=='dict':
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:
                classLabel=secondDict[key]
    return classLabel


import treePlotter
myTree=treePlotter.retriveTree(0)
# print myTree
# print classify(myTree,labels,[1,0])
# print classify(myTree,labels,[1,1])


#决策树的保存
def storeTree(inputTree,filename):
    import pickle
    fw=open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()

#调用保存的树
def grab(filename):
    import pickle
    with open(filename) as fr:
        return pickle.load(fr)

# storeTree(myTree,'ClassifierStorage.txt')
myTree2=grab('ClassifierStorage.txt')                                 #载入保存在本地的树
# print myTree2
# print classify(myTree2,labels,[0,1])                                   #利用载入的树对输入向量进行分类


########################################################################################################################
########################################################################################################################
#####实际应用
#使用决策树预测隐形眼镜类型示例
with open("lenses.txt") as fr:
    lenses=[inst.strip().split('\t') for inst in fr.readlines()]
    lenseselabels=['age','prescript','astigmatic','tearRate']
    lensesTree=createTree(lenses,lenseselabels)                          #构建决策树
    # print lensesTree

import treePlotter
# treePlotter.createPlot(lensesTree)                                     #绘制决策树

#保存隐形眼镜类型预测数
storeTree(lensesTree,'lensesTreeStorage.txt')
#载入
lensesTree_readin=grab('lensesTreeStorage.txt')
treePlotter.createPlot(lensesTree_readin)                                 #绘制载入的决策树