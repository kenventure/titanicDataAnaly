# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:58:22 2017

@author: tham
"""
from sklearn import svm
import csv
import pandas as pd

import numpy

#functions
def proportion (val, arr):
    count=0
    for i in arr:
        if val==i:
            count=count+1            
    count
    return count

def proportionArr(header, val, arr):
    arr1=[]
    for row in arr:
        arr1.append(row[header])
    count = proportion(val, arr1)
    propor = count / len(arr)
    return propor
    
def meanArr(header, arr):
    arr1=[]
    for row in arr:
        #print(row[header])
        if (row[header]!=""):
            num  = float(row[header])
            #print(num)
            arr1.append(num) 
    return float(sum(arr1)) / max(len(arr1), 1)
        
def getArr(header, arr)    :
    arr1=[]
    for row in arr:
        if len(row[header])>0:
            #print (row[header])
            arr1.append(float(row[header]))
    return arr1
def getStrArr(header, arr)    :
    arr1=[]
    for row in arr:
        if len(row[header])>0:
            #print (row[header])
            arr1.append(row[header])
    return arr1

def getAgeProb(age, arr):
    ageProb=0
    count=0
    upperBound=0
    while upperBound<age:
        upperBound=upperBound+5
    lowerBound=upperBound-5
    
    for i in range(lowerBound, upperBound):
        count=count+arr.count(i)
    total = len(arr)
    result = count/total
    return result

def getAgeProb2(age, arrWhole, arrSurv):
    ageProb=0
    count=0
    upperBound=0
    while upperBound<age:
        upperBound=upperBound+5
    lowerBound=upperBound-5
    
    surCount=0
    for i in range(lowerBound, upperBound):
        count=count+arrWhole.count(i)
        surCount=surCount+arrSurv.count(i)
    result = surCount/count
    return result

def getAgeProb3 (ageIn, arrWhole, arrSurv):
    ageProb=0
    count=0
    upperBound=0
    while upperBound<ageIn:
        upperBound=upperBound+5
    lowerBound=upperBound-5
    surCount=0
    for i in arrWhole:
        if i >=lowerBound and i <upperBound:
            count=count+1
    
    for i in arrSurv:
        if i >=lowerBound and i <upperBound:
            surCount=surCount+1
    if count==0:
        result=0
    else:
        result = surCount/count
    return result

def getFareProb (fare, arrWhole, arrSurv):
    fareProb=0
    count=0
    upperBound=0
    while upperBound<fare:
        upperBound=upperBound+50
    lowerBound=upperBound-50
    surCount=0
    for i in arrWhole:
        if i >=lowerBound and i <upperBound:
            count=count+1
    
    for i in arrSurv:
        if i >=lowerBound and i <upperBound:
            surCount=surCount+1
    if count==0:
        result= 0
    else:
        result = surCount/count
    return result

def getProb (no, arrWhole, arrSurv):
    nSurv = arrSurv.count(no)
    nWhole = arrWhole.count(no)
    result = 0
    if nWhole==0:
        result = 0
    else:
        result = nSurv / nWhole
    #result = arrSurv.count(no) / arrWhole.count(no)
    return result

#read data from files
with open('train.csv', newline='') as csvfile:
   
    spamreader = csv.DictReader(csvfile)
    data = []
    for row in spamreader:
        
        data.append(row)
     

w, h = 7, len(data);
xArr = [[0 for x in range(w)] for y in range(h)] 
i=0
ansArr=[]
for row in data:
    cls = float(row['Pclass'])
    classProb = getProb(cls, getArr('Pclass', data), getArr('Pclass', popSurv))
    
    sexProb=0
    sex = row['Sex']
    if sex=='male':
        sexProb = maleProb
    else:
        sexProb = femProb
      
    ageStr = row['Age']
    if len(ageStr)>0:
        age = float (row['Age'])
        ageProb3 = getAgeProb3(age, getArr('Age', data), getArr('Age', popSurv))
    else:
        ageProb3=0
        
    sp = float(row['SibSp'])
    spProb = getProb(sp, getArr('SibSp', data), getArr('SibSp', popSurv))
    
    parch = float(row['Parch'])
    parchProb = getProb(parch, getArr('Parch', data), getArr('Parch', popSurv))
    
    fareStr = row['Fare']
    if len(fareStr)>0:
        fare = float(fareStr)
    else:
        fare = 0
    
    fareProb = getFareProb(fare, getArr('Fare', data), getArr('Fare', popSurv))
    
    emb = row['Embarked']
    embProb = getProb(emb, getStrArr('Embarked', data), getStrArr('Embarked', popSurv))
    print ('{0} {1} {2} {3} {4} {5} {6}'.format(classProb, sexProb, ageProb3, spProb, parchProb, fareProb, embProb ))
    
    xArr[i][0]=classProb
    xArr[i][1]=sexProb
    xArr[i][2]=ageProb3
    xArr[i][3]=spProb
    xArr[i][4]=parchProb
    xArr[i][5]=fareProb
    xArr[i][6]=embProb
    i=i+1
    ansArr.append(float(row['Survived'])) 

clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(xArr, ansArr)
#SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#    max_iter=-1, probability=False, random_state=None, shrinking=True,
#    tol=0.001, verbose=False)

#predict training data
success = 0
for row in data:
    cls = float(row['Pclass'])
    classProb = getProb(cls, getArr('Pclass', data), getArr('Pclass', popSurv))
    
    sexProb=0
    sex = row['Sex']
    if sex=='male':
        sexProb = maleProb
    else:
        sexProb = femProb
      
    ageStr = row['Age']
    if len(ageStr)>0:
        age = float (row['Age'])
        ageProb3 = getAgeProb3(age, getArr('Age', data), getArr('Age', popSurv))
    else:
        ageProb3=0
        
    sp = float(row['SibSp'])
    spProb = getProb(sp, getArr('SibSp', data), getArr('SibSp', popSurv))
    
    parch = float(row['Parch'])
    parchProb = getProb(parch, getArr('Parch', data), getArr('Parch', popSurv))
    
    fareStr = row['Fare']
    if len(fareStr)>0:
        fare = float(fareStr)
    else:
        fare = 0
    
    fareProb = getFareProb(fare, getArr('Fare', data), getArr('Fare', popSurv))
    
    emb = row['Embarked']
    embProb = getProb(emb, getStrArr('Embarked', data), getStrArr('Embarked', popSurv))
    print ('{0} {1} {2} {3} {4} {5} {6}'.format(classProb, sexProb, ageProb3, spProb, parchProb, fareProb, embProb ))
    
    arrAns=[]
    arrAns.append(classProb)
    arrAns.append(sexProb)
    arrAns.append(ageProb3)
    arrAns.append(spProb)
    arrAns.append(parchProb)
    arrAns.append(fareProb)
    arrAns.append(embProb)
    ans = clf.predict([arrAns])
    if ans==float(row['Survived']):
        success=success+1

print (success)
print (success/len(data))


#work on the test data set
dataTest = []
with open('test.csv', newline='') as csvfile:
   
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        
        dataTest.append(row)
  
#with open('testRes.csv', 'w', newline='') as csvfile:
    writer = open ('testSVMRes.csv', 'w')
    #spamwriter = csv.writer(csvfile, delimiter='',
    #                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow('PassengerId,Survived')
    writer.write('PassengerId,Survived\n')   
    for row in dataTest:
        # process row
        cls = float(row['Pclass'])
        classProb = getProb(cls, getArr('Pclass', data), getArr('Pclass', popSurv))
        
        sexProb=0
        sex = row['Sex']
        if sex=='male':
            sexProb = maleProb
        else:
            sexProb = femProb
          
        ageStr = row['Age']
        if len(ageStr)>0:
            age = float (row['Age'])
            ageProb3 = getAgeProb3(age, getArr('Age', data), getArr('Age', popSurv))
        else:
            ageProb3=0
            
        sp = float(row['SibSp'])
        spProb = getProb(sp, getArr('SibSp', data), getArr('SibSp', popSurv))
        
        parch = float(row['Parch'])
        parchProb = getProb(parch, getArr('Parch', data), getArr('Parch', popSurv))
        
        fareStr = row['Fare']
        if len(fareStr)>0:
            fare = float(fareStr)
        else:
            fare = 0
        
        fareProb = getFareProb(fare, getArr('Fare', data), getArr('Fare', popSurv))
        
        emb = row['Embarked']
        embProb = getProb(emb, getStrArr('Embarked', data), getStrArr('Embarked', popSurv))
        print ('{0} {1} {2} {3} {4} {5} {6}'.format(classProb, sexProb, ageProb3, spProb, parchProb, fareProb, embProb ))
        
        arrAns=[]
        arrAns.append(classProb)
        arrAns.append(sexProb)
        arrAns.append(ageProb3)
        arrAns.append(spProb)
        arrAns.append(parchProb)
        arrAns.append(fareProb)
        arrAns.append(embProb)
        ans = clf.predict([arrAns])  
        wriStr=""
        if ans>=0.5:
            wriStr='1'
        else:
            wriStr='0'
        writer.write(row['PassengerId']+','+wriStr+'\n')
        
    writer.close()
    
    
print('end')        
