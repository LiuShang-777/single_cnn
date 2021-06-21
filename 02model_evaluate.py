#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:27:22 2020

@author: ls
"""
#need data directory containing test data and predicted data with specific prefix and suffix
import numpy as np
import matplotlib.pyplot as plt
data_dir_my='/home/ls/singlecnn/sequence/scw/24_16_10/'
data_dir_pnas='/home/ls/singlecnn/pnas_scw/'
list_pred=['predict%d.npy'%i for i in range(5)]
list_true=['testy%d.npy'%i for i in range(5)]
def calculate_accuracy(data_dir,list_pred,list_true):
    #calculate accuracy for a single pair of dataset
    pred=np.load(data_dir+list_pred).argmax(axis=1)
    true=np.load(data_dir+list_true).argmax(axis=1)
    if len(pred)!=len(true):
        print('inconsistent between prediction and real samples')
        return None
    else:
        cal=0
        for i,j in zip(pred,true):
            if i==j:
                cal+=1
            else:
                continue
    return round(cal/len(pred),2)
accuracy_list_my=[ calculate_accuracy(data_dir_my,i,j) for i,j in zip(list_pred,list_true) ]  
accuracy_list_pnas=[ calculate_accuracy(data_dir_pnas,i,j) for i,j in zip(list_pred,list_true) ] 


def cal_tpr_fpr(threshold,pred,test):
    ap=len([i for i in test if i==1])
    an=len([i for i in test if i==0])
    tp,fp=0,0
    for i,j in zip(pred,test):
        if (i[1]>=threshold)&(j==1):
            tp+=1
        elif (i[1]>=threshold)&(j==0):
            fp+=1
        else:
            continue
    return (tp, fp,ap,an)
def cal_auroc(tpr,fpr):
    auroc=0
    for i in range(len(tpr[:-1])):
        height=fpr[i+1]-fpr[i]
        sum_bottom=tpr[i]+tpr[i+1]
        auroc+=abs(sum_bottom*height*0.5)
    return auroc
    
dic={}
for i in np.arange(0,1.1,0.1):
    threshold=i
    tp_,fp_,ap_,an_=0,0,0,0
    for pred,test in zip(list_pred,list_true):
        test_my=np.load(data_dir_my+test).argmax(axis=1)#data_dir
        pred_my=np.load(data_dir_my+pred)#data_dir
        tp_my,fp_my,ap_my,an_my=cal_tpr_fpr(threshold,pred_my,test_my)
        tp_+=tp_my
        fp_+=fp_my
        ap_+=ap_my
        an_+=an_my
    tpr=tp_/ap_
    fpr=fp_/an_
    dic[i]=(fpr,tpr)
auroc_my=cal_auroc([dic[i][1] for i in dic.keys()],[dic[i][0] for i in dic.keys()])

dic_={}
for i in np.arange(0,1.1,0.1):
    threshold=i
    tp_,fp_,ap_,an_=0,0,0,0
    for pred,test in zip(list_pred,list_true):
        test_pnas=np.load(data_dir_pnas+test).argmax(axis=1)#data_dir
        pred_pnas=np.load(data_dir_pnas+pred)#data_dir
        tp_pnas,fp_pnas,ap_pnas,an_pnas=cal_tpr_fpr(threshold,pred_pnas,test_pnas)
        tp_+=tp_pnas
        fp_+=fp_pnas
        ap_+=ap_pnas
        an_+=an_pnas
    tpr=tp_/ap_
    fpr=fp_/an_
    dic_[i]=(fpr,tpr)
auroc_pnas=cal_auroc([dic_[i][1] for i in dic_.keys()],[dic_[i][0] for i in dic_.keys()])
plt.figure(figsize=(3.33,3.33),dpi=600)
plt.plot([ dic[i][0] for i in dic.keys()],[ dic[i][1] for i in dic.keys()],c='blue',marker='o')
#plt.plot(np.arange(0,2),np.arange(0,2),c='r',linestyle='--')
plt.plot([ dic_[i][0] for i in dic_.keys()],[ dic_[i][1] for i in dic_.keys()],c='red',marker='v')
plt.text(0.17,0.4,'AUROC:%.2f'%auroc_my,color='blue',fontsize=10)
plt.text(0.6,0.6,'AUROC:%.2f'%auroc_pnas,color='red',fontsize=10)
plt.xlabel('FPR',fontsize=10)
plt.ylabel('TPR',fontsize=10)
plt.tight_layout()
plt.savefig('/home/ls/singlecnn/scw_auroc.png')
plt.clf() 



#accuracy
scw_my=np.array(accuracy_list_my)
scw_pnas=np.array(accuracy_list_pnas)
init_my=np.array([0.8,0.8,0.8,0.8,0.79])
init_pnas=np.array([0.82,0.82,0.81,0.81,0.81])
elong_my=np.array([0.79,0.8,0.8,0.8,0.8])
elong_pnas=np.array([0.81,0.79,0.8,0.8,0.82])
error_attri={'elinewidth':2,'ecolor':'black','capsize':6}
plt.figure(figsize=(3.33,3.33),dpi=600)
plt.bar(np.arange(1,4),[init_my.mean(),elong_my.mean(),scw_my.mean()],0.25,yerr=[init_my.std(),elong_my.std(),scw_my.std()],error_kw=error_attri)
plt.bar(np.arange(1.5,4.5),[init_pnas.mean(),elong_pnas.mean(),scw_pnas.mean()],0.25,yerr=[init_pnas.std(),elong_pnas.std(),scw_pnas.std()],error_kw=error_attri)
plt.legend(['single-layer','model in maize'])
plt.ylabel('accuracy')
plt.tight_layout()
plt.savefig('/home/ls/singlecnn/accuracy.png')
plt.clf()

[init_my.mean(),elong_my.mean(),scw_my.mean()]
[init_pnas.mean(),elong_pnas.mean(),scw_pnas.mean()]