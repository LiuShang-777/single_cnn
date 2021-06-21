# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:37:21 2020

@author: liushang
"""

#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams['font.family']='Times New Roman'
import sys
import os
dir_=sys.argv[1]
output=sys.argv[2]
file_ex=[i for i in os.listdir(dir_) if 'kernel_ex' in i]
file_no=[i for i in os.listdir(dir_) if 'kernel_no' in i]
for idx in range(5):
    ex=np.load(dir_+file_ex[idx])
    no=np.load(dir_+file_no[idx])
    print(ex.shape)
    print(no.shape)
    plt.figure(figsize=(6,48),dpi=600)
    for i in range(ex.shape[2]):
        plt.subplot(ex.shape[2],1,i+1)
        plt.title('kernel%d'%i)
        plt.scatter(np.arange(ex.shape[1]),ex[0,:,i],s=0.5,color='r')
        plt.scatter(np.arange(no.shape[1]),no[0,:,i],s=0.5,color='b')
        plt.legend(['expressed','low expressed'])
        plt.tight_layout()
    plt.savefig(dir_+str(idx)+'_'+output)
    plt.clf()
    
    
    

