# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:31:07 2017

@author: tham
"""

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
     


popSurv = []
      
for row in data:
    if row['Survived']=='1':
        popSurv.append(row)
 

df = pd.DataFrame.from_dict(popSurv)
print(df)

#sex
propMale = proportionArr('Sex', 'male', popSurv)
propMaleDat = proportionArr('Sex', 'male', data)
propFemale = proportionArr('Sex', 'female', popSurv)
propFemaleDat = proportionArr('Sex', 'female', data)

print(propMale)
print(propMaleDat)
print (propFemale)
print(propFemaleDat)
    
maleInc = propMale/propMaleDat
femaleInc = propFemale/propFemaleDat

print ('Male factor {0}'.format(maleInc))
print ('Female factor {0}'.format(femaleInc))
#age
meanAge=0
meanAge = meanArr('Age', popSurv)

print('Average age: {0}'.format(meanAge))
arr=getArr('Age', popSurv)
arr
print ('Min age: {0} Max age: {1}'.format(min(arr), max(arr)))

#siblings
meanSib = meanArr('SibSp', popSurv)
print('Average sib spouse: {0}'.format(meanSib))
#parents
meanPar = meanArr('Parch', popSurv)
print('Average parent: {0}'.format(meanPar))
#ticket
meanTic = meanArr('Fare', popSurv)
print('Average Ticket fare: {0}'.format(meanTic))
#embarkation
arr2 = getStrArr('Embarked', popSurv)
numC = arr2.count('C')
numQ = arr2.count('Q')
numS = arr2.count('S')
print('No C: {0}, No Q: {1}, No S:{2}'.format(numC, numQ, numS))
#class
arr3 = getStrArr('Pclass', popSurv)
numF = arr3.count('1')
numSec = arr3.count('2')
numT = arr3.count('3')
print('No 1: {0}, No 2: {1}, No 3:{2}'.format(numF, numSec, numT))

#Fare
fareArr = getArr('Fare', popSurv)
fareOrgArr = getArr('Fare', data)
print ('Size {0}'.format(len(fareOrgArr)))
print('Min fare surv {0} max {1}'.format(min(fareArr), max(fareArr)))

varFare = numpy.var(fareArr)
varOrg = numpy.var(fareOrgArr)

print ('Variance fare org {0} surv {1}'.format(varOrg, varFare))

#for i in fareOrgArr:
#    print (i)
    
print('Total Min fare {0} max {1}'.format(min(fareOrgArr), max(fareOrgArr)))
#calculate probabilities
#sex prob
femProb = femaleInc/(maleInc+femaleInc)
maleProb = maleInc/(maleInc+femaleInc)
print ('Female Prob: {0}, Male Prob: {1}'.format(femProb, maleProb))

#age probabilities
ageArr = getArr('Age', popSurv)
wArr = getArr('Age', data)
ageSamp= 25
ageProb = getAgeProb(ageSamp, ageArr)
ageProb2 = getAgeProb2(ageSamp, wArr, ageArr)
ageProb3 = getAgeProb3(ageSamp, wArr, ageArr)
print ('Age prob for {1}: {0}'.format(ageProb, ageSamp))
print ('Age prob 2 for {1}: {0}'.format(ageProb2, ageSamp))
print ('Age prob 3 for {1}: {0}'.format(ageProb3, ageSamp))

spProb=0
sp = 3
spProb = getProb(sp, getArr('SibSp', data), getArr('SibSp', popSurv))
print ('Sibling Spouse prob for {0}: {1}'.format(sp, spProb))

classProb = 0
cls = 1
classProb = getProb(cls, getArr('Pclass', data), getArr('Pclass', popSurv))
print ('CClass prob for {0}: {1}'.format(cls, classProb))

parchProb = 0
parch = 2
parchProb = getProb(cls, getArr('Parch', data), getArr('Parch', popSurv))
print ('Parch prob for {0}: {1}'.format(parch, parchProb))

fareProb = 0;
fare=120
fareProb = getFareProb(fare, getArr('Fare', data), getArr('Fare', popSurv))
print ('Fare prob for {0}: {1}'.format(fare, fareProb))

emb = 'C'
embProb = getProb(emb, getStrArr('Embarked', data), getStrArr('Embarked', popSurv))

print ('Embarked prob for {0}: {1}'.format(emb, embProb))

#Start to read in the data
success = 0
for row in data:
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
    
    fare = float(row['Fare'])
    fareProb = getFareProb(fare, getArr('Fare', data), getArr('Fare', popSurv))
    
    emb = row['Embarked']
    embProb = getProb(emb, getStrArr('Embarked', data), getStrArr('Embarked', popSurv))
    #print ('{0} {1} {2} {3} {4} {5} {6}'.format(classProb, sexProb, ageProb3, spProb, parchProb, fareProb, embProb ))
    
    avg=0
    avg = classProb + sexProb + ageProb3 + spProb + parchProb + fareProb + embProb
    res = avg/7
    threshold = 0.41915
    if res>threshold:
        sur = '1'
       # print('1 {0}'.format(row['Survived']))
    else:
        sur = '0'
       # print ('0 {0}'.format(row['Survived']))
    if sur == row['Survived']:
        success = success + 1
        
print(success)
print (success / len(data))

#work on the test data set
dataTest = []
with open('test.csv', newline='') as csvfile:
   
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        
        dataTest.append(row)
  
#with open('testRes.csv', 'w', newline='') as csvfile:
    writer = open ('testSimpleRes.csv', 'w')
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
        
        avg=0
        avg = classProb + sexProb + ageProb3 + spProb + parchProb + fareProb + embProb
        res = avg/7
        threshold = 0.41915
        if res>threshold:
            sur = '1'
        else:
            sur = '0'
        #spamwriter.writerow(row['PassengerId']+','+sur)
        writer.write(row['PassengerId']+','+sur+'\n')
        
    writer.close()