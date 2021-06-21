#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:02:00 2020

@author: ls
"""

import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras import models  
import numpy as np
import sys
#import matplotlib.pyplot as plt
import os
#get input data

dir_=sys.argv[1]
idx=int(sys.argv[2])
out_dir=sys.argv[3]
total_file=sys.argv[4]
'''

dir_='sequence/initiation/24_14_10'
idx=0
out_dir='deeplift/initiation'
total_file='sequence/initiation/init_utr5.fa'
'''

model_file=dir_+'/model%d.h5'%idx
exfile=out_dir+'/kernel_ex%d.npy'%idx
nofile=out_dir+'/kernel_no%d.npy'%idx


with open(total_file,'r') as file:
    dic_total,seq_total,name_total={},[],[]
    for line in file:
        line=line.strip()
        if line.startswith('>'):
            name_total.append(line)
        else:
            seq_total.append(line)
    for i,j in zip(name_total,seq_total):
        dic_total[i]=j
name_spe=[i for i in os.listdir(dir_) if 'true%d'%idx in i]
with open(dir_+'/'+name_spe[0],'r') as file:
    list_name,list_seq,list_length=[],[],[]
    for line in file:
        line=line.strip()
        if line in dic_total.keys():
            list_name.append(line)
            list_seq.append(dic_total[line])
            list_length.append(len(dic_total[line]))
        else:
            continue
def one_hotshot(array,classes):
    onehot=np.zeros((classes,array.shape[0]))
    for i in range(array.shape[0]):
        onehot[int(array[i]),i]=1
    return onehot
def tansfer_str_to_array(list_input):
    array=np.zeros((len(list_input),len(list_input[0])))
    for i in range(len(list_input)):
        for j in range(len(list_input[i])):
            if list_input[i][j]=='A':
                continue
            elif list_input[i][j]=='T':
                array[i,j]=1
            elif list_input[i][j]=='C':
                array[i,j]=2
            elif list_input[i][j]=='G':
                array[i,j]=3
            elif list_input[i][j]=='N':
                array[i,j]=4
    return array
init_array=tansfer_str_to_array(list_seq)                
list_result=[]
for i in range(init_array.shape[0]):
    list_result.append(one_hotshot(init_array[i,:],5))
list_result=np.array(list_result)
#get expression data
y_list=[]
for i in list_name:
    if 'aw' in i:
        y_list.append(0)
    elif 'ae' in i:
        y_list.append(1)
    else:
        break
def y_onehot(array,classes):
    narray=np.zeros((array.shape[0],classes))
    for i in range(len(array)):
        narray[i,array[i]]=1
    return narray

y_result=y_onehot(np.array(y_list),2)
list_result_idx=[i for i in range(len(list_name))]
list_result_idx=np.array(list_result_idx)
list_result=list_result[:,:,:,np.newaxis]

#get output of first conv layer
model=tf.keras.models.load_model(model_file)
tmp=model.get_layer(index=0).get_weights()
tmp=models.Model(model.input,model.get_layer(index=0).output)
tmp_output=tmp.predict(list_result)
ex,no=[],[]
for i,j in zip(y_list,tmp_output):
    if i==1:
        ex.append(j)
    else:
        no.append(j)
ex=np.array(ex)[0,:,:,:]
no=np.array(no)[0,:,:,:]
np.save(exfile,ex)
np.save(nofile,no)
