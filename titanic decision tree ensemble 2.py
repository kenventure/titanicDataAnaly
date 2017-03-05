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

def getClassScore (cls):
    score=0
    if cls=='1':
        score=0.33
    else: 
        if cls=='2':
            score=0.66
        else:
            score=1
    return score

def getSexScore(sx):
    score=0
    if sx =='female':
        score=0.5
    else:
        score=1
    return score

def getAgeScore(age):
    score = age/50
    score = abs(1-score)
    return score

def getSibScore(sib):
    score = sib * 0.25
    score = abs(1-score)
    return score

def getParchScore(prch):
    score = prch * 0.25
    score = abs(1-score)
    return score

def getFareScore(fare):
    score = fare/50
    return score

def getEmbScore(emb):
    score = 0
    if emb=='C':
        score=0.33
    else:
        if emb == 'Q':
            score = 0.66
        else:
            if emb=='S':
                score = 1
    return score

#read data from files
with open('train.csv', newline='') as csvfile:
   
    spamreader = csv.DictReader(csvfile)
    data = []
    for row in spamreader:
        
        data.append(row)
     

totalNum = 891
length = 8

remainder = totalNum%length

w, h = 7, int(totalNum/length)

#xArr = []

xArr = [[[0 for k in range(w)] for j in range(h)] for i in range(length)]
ansArr=[[0 for k in range(h)] for j in range(length)]

clfArr = []
#for i in range(0,length):
#    tmpArr = [[0 for x in range(w)] for y in range(h)]
#    xArr.append(tmpArr)
#    tmpAnsArr = []
#    ansArr.append(tmpAnsArr)
    
i=0

for row in data:
    cls = row['Pclass']
    classProb = getClassScore(cls)
    
    sexProb=0
    sex = row['Sex']
    sexProb = getSexScore(sex)
      
    ageStr = row['Age']
    if len(ageStr)>0:
        age = float (row['Age'])
        ageProb3 = getAgeScore(age)
    else:
        ageProb3=0
        
    sp = float(row['SibSp'])
    spProb = getSibScore(sp)
    
    parch = float(row['Parch'])
    parchProb = getParchScore(parch)
    
    fareStr = row['Fare']
    if len(fareStr)>0:
        fare = float(fareStr)
    else:
        fare = 0
    
    fareProb = getFareScore(fare)
    
    emb = row['Embarked']
    embProb = getEmbScore(emb)
    print ('{0} {1} {2} {3} {4} {5} {6}'.format(classProb, sexProb, ageProb3, spProb, parchProb, fareProb, embProb ))
    
    index = 0
    
    index = int(i / h)
    
    subIndex = i-index*h
    print('{0} {1} {2}'.format(index, subIndex, i))
    xArr[index][subIndex][0]=classProb
    xArr[index][subIndex][1]=sexProb
    xArr[index][subIndex][2]=ageProb3
    xArr[index][subIndex][3]=spProb
    xArr[index][subIndex][4]=parchProb
    xArr[index][subIndex][5]=fareProb
    xArr[index][subIndex][6]=embProb
    ansArr[index][subIndex] = float(row['Survived'])
    
            
    i=i+1
    if i == totalNum-remainder:
        break

for i in range(0, length)  :
    tmpClf = tree.DecisionTreeClassifier()
    clfArr.append(tmpClf)


for i in range (0, length):
    clfArr[i].fit(xArr[i], ansArr[i])
    
clf1 = tree.DecisionTreeClassifier()
clf1.fit(xArr1, ansArr1)
clf2 = tree.DecisionTreeClassifier()
clf2.fit(xArr2, ansArr2)
clf3 = tree.DecisionTreeClassifier()
clf3.fit(xArr3, ansArr3)
#SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#    max_iter=-1, probability=False, random_state=None, shrinking=True,
#    tol=0.001, verbose=False)

#predict training data
success = 0
for row in data:
    cls = row['Pclass']
    classProb = getClassScore(cls)
    
    sexProb=0
    sex = row['Sex']
    sexProb = getSexScore(sex)
      
    ageStr = row['Age']
    if len(ageStr)>0:
        age = float (row['Age'])
        ageProb3 = getAgeScore(age)
    else:
        ageProb3=0
        
    sp = float(row['SibSp'])
    spProb = getSibScore(sp)
    
    parch = float(row['Parch'])
    parchProb = getParchScore(parch)
    
    fareStr = row['Fare']
    if len(fareStr)>0:
        fare = float(fareStr)
    else:
        fare = 0
    
    fareProb = getFareScore(fare)
    
    emb = row['Embarked']
    embProb = getEmbScore(emb)
    print ('{0} {1} {2} {3} {4} {5} {6}'.format(classProb, sexProb, ageProb3, spProb, parchProb, fareProb, embProb ))
    
    arrAns=[]
    arrAns.append(classProb)
    arrAns.append(sexProb)
    arrAns.append(ageProb3)
    arrAns.append(spProb)
    arrAns.append(parchProb)
    arrAns.append(fareProb)
    arrAns.append(embProb)
    ans1 = clf1.predict([arrAns])
    ans2 = clf2.predict([arrAns])
    ans3 = clf3.predict([arrAns])
    
    count = 0
    ans=0
    if ans1==1:
        count=count+1
    if ans2==1:
        count=count+1
    if ans3==1:
        count=count+1
    if count>=2:
        ans=1
    else:
        ans = 0
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
    writer = open ('testTreeEnsemRes.csv', 'w')
    #spamwriter = csv.writer(csvfile, delimiter='',
    #                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow('PassengerId,Survived')
    writer.write('PassengerId,Survived\n')   
    for row in dataTest:
        # process row
        cls = row['Pclass']
        classProb = getClassScore(cls)
        
        sexProb=0
        sex = row['Sex']
        sexProb = getSexScore(sex)
          
        ageStr = row['Age']
        if len(ageStr)>0:
            age = float (row['Age'])
            ageProb3 = getAgeScore(age)
        else:
            ageProb3=0
            
        sp = float(row['SibSp'])
        spProb = getSibScore(sp)
        
        parch = float(row['Parch'])
        parchProb = getParchScore(parch)
        
        fareStr = row['Fare']
        if len(fareStr)>0:
            fare = float(fareStr)
        else:
            fare = 0
        
        fareProb = getFareScore(fare)
        
        emb = row['Embarked']
        embProb = getEmbScore(emb)
        print ('{0} {1} {2} {3} {4} {5} {6}'.format(classProb, sexProb, ageProb3, spProb, parchProb, fareProb, embProb ))
        
        arrAns=[]
        arrAns.append(classProb)
        arrAns.append(sexProb)
        arrAns.append(ageProb3)
        arrAns.append(spProb)
        arrAns.append(parchProb)
        arrAns.append(fareProb)
        arrAns.append(embProb)
        ans1 = clf1.predict([arrAns])
        ans2 = clf2.predict([arrAns])
        ans3 = clf3.predict([arrAns])
        
        count = 0
        ans=0
        if ans1==1:
            count=count+1
        if ans2==1:
            count=count+1
        if ans3==1:
            count=count+1
        wriStr=""
        if count>=2:
            wriStr='1'
        else:
            wriStr='0'

        writer.write(row['PassengerId']+','+wriStr+'\n')
        
    writer.close()
    
    
print('end')        
