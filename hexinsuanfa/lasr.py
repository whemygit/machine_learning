#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import urllib2
import numpy
from sklearn import datasets,linear_model
from math import sqrt
import matplotlib.pyplot as plot

reload(sys)
sys.setdefaultencoding("utf-8")


target_url=("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv")
data=urllib2.urlopen(target_url)

xList=[]
labels=[]
names=[]
firstLine=True
for line in data:
    if firstLine:
        names=line.strip().split(";")
        firstLine=False
    else:
        row=line.strip().split(";")
        labels.append(float(row[-1]))
        row.pop()
        floatRow=[float(num) for num in row]
        xList.append(floatRow)

nrows=len(xList)
ncols=len(xList[0])

xMeans=[]
xSD=[]

for i in range(ncols):
    col=[xList[j][i] for j in range(nrows)]
    mean=sum(col)/nrows
    xMeans.append(mean)
    colDiff=[(xList[j][i]-mean) for j in range(nrows)]
    sumSq=sum([colDiff[i]*colDiff[i] for i in range(nrows)])
    stdDev=sqrt(sumSq/nrows)
    xSD.append(stdDev)

xNormalized=[]
for i in range(nrows):
    rowNormalized=[(xList[i][j]-xMeans[j])/xSD[j] for j in range(ncols)]
    xNormalized.append(rowNormalized)

meanLabel=sum(labels)/nrows
sdLabel=sqrt(sum([(labels[i]-meanLabel)*(labels[i]-meanLabel) for i in range(nrows)])/nrows)
labelNormalized=[(labels[i]-meanLabel)/sdLabel for i in range(nrows)]

beta=[0.0]*ncols
betaMat=[]
betaMat.append(list(beta))

nSteps=5
stepSize=0.004

for i in range(nSteps):
    print 'nsteps,,,,,,,,,',i
    residuals=[0.0]*nrows
    for j in range(nrows):
        labelsHat=sum([xNormalized[j][k]*beta[k] for k in range(ncols)])
        residuals[j]=labelNormalized[j]-labelsHat

    corr=[0.0]*ncols

    for j in range(ncols):
        corr[j]=sum([xNormalized[k][j]*residuals[k] for k in range(nrows)])/nrows

    iStar=0
    corrStar=corr[0]

    for j in range(1,ncols):
        if abs(corrStar)<abs(corr[j]):
            iStar=j;corrStar=corr[j]
            print 'iStar',iStar,'corrStar',corrStar

    beta[iStar]+=stepSize*corrStar/abs(corrStar)
    betaMat.append(list(beta))
    print 'beta',list(beta)
    print 'betaMat',betaMat

# for i in range(ncols):
#     print i
#     coefCurve=[betaMat[k][i] for k in range(nSteps)]
#     xaxis=range(nSteps)
#     plot.plot(xaxis,coefCurve)
#
# plot.xlabel("steps taken")
# plot.ylabel("coefficient values")
# plot.show()




