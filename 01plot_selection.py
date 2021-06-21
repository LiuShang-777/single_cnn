import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
dirs=sys.argv[1]
output=sys.argv[3]
symbol=sys.argv[2]
filters=[8,12,16,20,24,28,32]
lengths=[12,14,16,18,20,22]
maxs=[2,4,6,8,10]
def get_accuracy(file_):
    with open(file_,'r') as file:
        list_=[]
        for line in file:
            line=line.strip()
            if len(line)!=0:
                list_.append(float(line))
            else:
                continue
    result=np.array(list_)
    return (str(result.mean(axis=0)),str(result.std(axis=0)))
results=[]
for filter_ in filters:
    for length in lengths:
        for max_ in maxs:
            file_=dirs+'/'+'%d_%d_%d/'%(filter_,length,max_)+'%d_%d_%d_%s.txt'%(filter_,length,max_,symbol)
            mean,std=get_accuracy(file_)
            results.append('\t'.join([str(filter_),str(length),str(max_),mean,std]))
with open(output,'w') as file:
    file.write('\t'.join(['filters','kernel_size','maxpool_size','accuracy','std'])+'\n')
    for i in results:
        file.write(i+'\n')
dat=pd.read_csv(output,sep='\t')
dat=dat.sort_values('accuracy',ascending=True)
plt.figure(figsize=(6.63,2.5),dpi=600)
plt.hist(dat['accuracy'],color='#00ba38',edgecolor='k',bins=20)
plt.xlabel('accuracy')
plt.ylabel('model numbers')
plt.savefig(output+'.png')
dat=dat.loc[dat['accuracy']>=0.78]
dat.to_csv(output+'_select.csv',sep='\t')
