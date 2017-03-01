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
#calculate probabilities
#sex prob
femProb = femaleInc/(maleInc+femaleInc)
maleProb = maleInc/(maleInc+femaleInc)
print ('Female Prob: {0}, Male Prob: {1}'.format(femProb, maleProb))

#age probabilities
ageArr = getArr('Age', popSurv)
ageSamp= 16
ageProb = getAgeProb(ageSamp, ageArr)

print ('Age prob for {1}: {0}'.format(ageProb, ageSamp))
