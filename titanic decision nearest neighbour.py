# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:32:47 2017

@author: tham
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:58:22 2017

@author: tham
"""
from sklearn import tree
import csv
import pandas as pd

import numpy

def getClassDst (cls, cmp):
    score=0
    if cls != cmp:
        score = 0.5
    return score

def getSexDst(sx, cmp):
    score=0
    if sx != cmp:
        score = 0.5
    return score

def getAgeDst(age, cmp):
    score = abs (age - cmp) / 20
    return score

def getSibDst(sib, cmp):
    score = abs (sib - cmp)/ 4
    return score

def getParchDst(prch, cmp):
    score = abs (prch - cmp) / 4
    return score

def getFareDst(fare, cmp):
    score = abs(fare-cmp)/10
    if (score > 1):
        score=1
    return score

def getEmbScore(emb, cmp):
    score = 0
    if emb!=cmp:
        score = 0.5
    return score

def findNearestNeighbour (rw, data):
    minIndex = 0
    minScore=99999
    minOutcome='0'
    i = 0
    for row in data:
        cls = row['Pclass']
        clsCmp = rw['Pclass']
        classProb = getClassDst(cls, clsCmp)
        
        sexProb=0
        sex = row['Sex']
        sexCmp = rw['Sex']
        sexProb = getSexDst(sex, sexCmp)
          
        ageStr = row['Age']
        ageCmpStr = rw['Age']
        if (len(ageStr)>0) and len(ageCmpStr)>0:
            age = float (ageStr)
            ageCmp = float(ageCmpStr)
            ageProb3 = getAgeDst(age, ageCmp)
        else:
            ageProb3=0
            
        sp = float(row['SibSp'])
        spCmp = float(rw['SibSp'])
        spProb = getSibDst(sp, spCmp)
        
        parch = float(row['Parch'])
        parchCmp = float(rw['Parch'])
        parchProb = getParchDst(parch, parchCmp)
        
        fareStr = row['Fare']
        fareCmpStr = rw['Fare']
        if len(fareStr)>0 and len(fareCmpStr)>0:
            fare = float(fareStr)
            fareCmp = float(fareCmpStr)
        else:
            fare = 0
            fareCmp=0
        
        fareProb = getFareDst(fare, fareCmp)
        
        emb = row['Embarked']
        embCmp = rw['Embarked']
        embProb = getEmbScore(emb, embCmp)
        print ('{0} {1} {2} {3} {4} {5} {6}'.format(classProb, sexProb, ageProb3, spProb, parchProb, fareProb, embProb ))
        total = classProb + sexProb + ageProb3 + spProb + parchProb + fareProb + embProb 
        if total < minScore:
            minScore=total
            minIndex = i
            minOutcome = row['Survived']
        i=i+1
    return minOutcome
    
#read data from files
with open('train.csv', newline='') as csvfile:
   
    spamreader = csv.DictReader(csvfile)
    data = []
    for row in spamreader:
        
        data.append(row)
     




#for i in range(0,length):
#    tmpArr = [[0 for x in range(w)] for y in range(h)]
#    xArr.append(tmpArr)
#    tmpAnsArr = []
#    ansArr.append(tmpAnsArr)
    



    
           



    




#work on the test data set
dataTest = []
with open('test.csv', newline='') as csvfile:
   
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        
        dataTest.append(row)
  
#with open('testRes.csv', 'w', newline='') as csvfile:
    writer = open ('testNearestNeighbour.csv', 'w')
    #spamwriter = csv.writer(csvfile, delimiter='',
    #                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow('PassengerId,Survived')
    writer.write('PassengerId,Survived\n')   
    for row in dataTest:
        # process row
#        cls = row['Pclass']
#        classProb = getClassScore(cls)
#        
#        sexProb=0
#        sex = row['Sex']
#        sexProb = getSexScore(sex)
#          
#        ageStr = row['Age']
#        if len(ageStr)>0:
#            age = float (row['Age'])
#            ageProb3 = getAgeScore(age)
#        else:
#            ageProb3=0
#            
#        sp = float(row['SibSp'])
#        spProb = getSibScore(sp)
#        
#        parch = float(row['Parch'])
#        parchProb = getParchScore(parch)
#        
#        fareStr = row['Fare']
#        if len(fareStr)>0:
#            fare = float(fareStr)
#        else:
#            fare = 0
#        
#        fareProb = getFareScore(fare)
#        
#        emb = row['Embarked']
#        embProb = getEmbScore(emb)
#        print ('{0} {1} {2} {3} {4} {5} {6}'.format(classProb, sexProb, ageProb3, spProb, parchProb, fareProb, embProb ))
#        
#        arrAns=[]
#        arrAns.append(classProb)
#        arrAns.append(sexProb)
#        arrAns.append(ageProb3)
#        arrAns.append(spProb)
#        arrAns.append(parchProb)
#        arrAns.append(fareProb)
#        arrAns.append(embProb)
#        sum = 0
#        for i in range (0, length):
#            sum= sum + clfArr[i].predict([arrAns])
#        
#        
#        result = sum / length
        result = findNearestNeighbour (row, data)

        writer.write(row['PassengerId']+','+result+'\n')
        
    writer.close()
    
    
print('end')        
