#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 23:15:30 2021

@author: ls
"""


import pandas as pd
import numpy as np
import sys
from sklearn import svm
inputf=sys.argv[1]
#outputf=sys.argv[2]
data=pd.read_csv(inputf,sep='\t',index_col=0)
factor=data.columns.tolist()[:-1]
for i in factor:
    print(i)
X=data[factor]
#X['intercept']=[1 for i in range(X.shape[0])]
Y=data['label']
x_train=np.array(X.iloc[10000:,:])
y_train=np.array(Y[10000:])
x_test=np.array(X.iloc[:10000,:])
y_test=np.array(Y[:10000])
#np.save(outputf+'_test.npy',y_test)


model=svm.SVC(C=2,kernel='rbf',gamma=10,decision_function_shape='ovo') 
result=model.fit(x_train,y_train)
from sklearn.metrics import accuracy_score,recall_score,precision_score
pred_y=result.predict(x_test)
pred_y=np.array([1 if i>0.5 else 0 for i in pred_y])
#np.save(outputf+'_pred.npy',pred_y)
#evaluate
print(accuracy_score(y_test,pred_y))
print(recall_score(y_test,pred_y))
print(precision_score(y_test,pred_y))
f1_score=2/((1/recall_score(y_test,pred_y))+(1/precision_score(y_test,pred_y)))
print(f1_score)

