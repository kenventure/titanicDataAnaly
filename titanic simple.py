# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:31:07 2017

@author: tham
"""

import csv
import pandas as pd

import numpy

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

meanAge=0
meanAge = meanArr('Age', popSurv)

print('Average age: {0}'.format(meanAge))
arr=getArr('Age', popSurv)
arr
print ('Min age: {0} Max age: {1}'.format(min(arr), max(arr)))

meanSib = meanArr('SibSp', popSurv)
print('Average sib spouse: {0}'.format(meanSib))

meanPar = meanArr('Parch', popSurv)
print('Average parent: {0}'.format(meanPar))

