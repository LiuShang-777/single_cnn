import sys
import pandas as pd
inputdat=sys.argv[1]
outputf=sys.argv[2]
dat=pd.read_csv(inputdat,sep='\t',index_col=0)
print([i for i in dat.index][0])
ex=[i for i in dat.index if 'ae' in i]
no=[i for i in dat.index if 'aw' in i]
dat_ex=dat.loc[dat.index.isin(ex)]
dat_no=dat.loc[dat.index.isin(no)]
dat_ex['label']=[1 for i in ex]
dat_no['label']=[0 for i in no]
result=pd.concat([dat_ex,dat_no])
result=result.sample(frac=1)
result.to_csv(outputf,sep='\t')
