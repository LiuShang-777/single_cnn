import sys
inputf=sys.argv[1]
inputfa=sys.argv[2]
output=sys.argv[3]
import pandas as pd
dat=pd.read_csv(inputf,sep='\t')
with open(inputfa,'r') as file:
    list_=[]
    for line in file:
        line=line.strip()
        if line[0]=='>':
            list_.append(line[1:])
features=list(set([str(i) for i in dat['#pattern name']if i[0]!='#']))
dic={}
for feature in features:
    print('stat feature: %s\n'%feature)
    tmp_=[]
    dat_features=dat.loc[dat['#pattern name']==feature]
   # dat_features=dat_features.loc[dat_features['start']>500]
    dat_features=[str(i) for i in dat_features['sequence name']]
    print('feature number is %d\n'%len(dat_features))
    count=0
    for name in list_:
        if name not in dat_features:
            tmp_.append(0)
        else:
            tmp_.append(dat_features.count(name))
        count+=1
        if count%1000==0:
            print('record %d'%count)
    dic[feature]=tmp_
dat_=pd.DataFrame(dic)
dat_.index=list_
dat_.to_csv(output,sep='\t')
