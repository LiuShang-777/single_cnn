#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:38:35 2020

@author: ls
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#plt.rcParams['font.family']='Times New Roman'
plt.rcParams['font.size']=12
import sys
fimo=sys.argv[1]
dataframe=pd.read_csv(fimo,sep='\t')
columns=dataframe.columns.tolist()
ids=dataframe[columns[0]]
target_motifs=[i for i in ids]
def get_ex_no_dataframe(dataframe,target_motifs):
    result_dic={}
    for target_motif in target_motifs:        
        data_targets=dataframe.loc[dataframe['#pattern name']==target_motif]
        data_targets_ex=data_targets.loc[data_targets['sequence name'].isin(list(set([i for i in data_targets['sequence name'] if 'ae' in i])))]
        data_targets_no=data_targets.loc[data_targets['sequence name'].isin(list(set([i for i in data_targets['sequence name'] if 'aw' in i])))]
        result_dic[target_motif]=(data_targets_ex,data_targets_no)
    return result_dic
        
def calculate_ratio(data_targets_ex):
    dic={}
    coord=[(i,j) for i,j in zip(data_targets_ex['start'],data_targets_ex['stop'])]
    gene_numbers_ex=len(list(set([i for i in data_targets_ex['sequence name']])))
    if gene_numbers_ex==0:
        for i in range(1,1001):
            dic[i]=0
    else:        
        for i in range(1,1001):
            dic[i]=0
            for z in coord:
                if (i>=z[0])&(i<=z[1]):
                    dic[i]+=1
                else:
                    continue
            dic[i]=dic[i]/gene_numbers_ex
    return dic
#def
target_motifs_dics=get_ex_no_dataframe(dataframe,target_motifs)
for motif in target_motifs_dics.keys():
    print('fetching genes with %s'%motif)
    dat=target_motifs_dics[motif][0]
    with open(fimo+'_%s.txt'%motif,'w') as file:
        for i in dat['sequence name']:
            file.write(i[:-2]+'\n')

def get_data_visualize(target_motifs__dics):
    visualization_result={}
    for motif in target_motifs__dics.keys():
        dic_ex=calculate_ratio(target_motifs__dics[motif][0])
        dic_no=calculate_ratio(target_motifs__dics[motif][1])
        visualization_result[motif]=(dic_ex,dic_no)
    return visualization_result
visualization_results=get_data_visualize(target_motifs_dics)
for i in visualization_results.keys():
    data_ex,data_no=visualization_results[i][0],visualization_results[i][1]
    plt.figure(figsize=(6.68,3),dpi=600)
    plt.plot(np.arange(1,1001),[data_ex[i]*100 for i in np.arange(1,1001)],c='r')
    plt.plot(np.arange(1,1001),[data_no[i]*100 for i in np.arange(1,1001)],c='b')
    plt.xticks([0,100,200,300,400,500,600,700,800,900,1000],[-500,-400,-300,-200,-100,'TSS',100,200,300,400,500])
    plt.xlabel('Loc')
    plt.ylabel('Ratio(%)')
    plt.legend(['expressed','unexpressed'])
    plt.title(i)
    plt.savefig('%s_%s.png'%(fimo,i))
plt.clf()
