import sys
import pandas as pd

input_tom=sys.argv[1]
idx=int(sys.argv[2])
output_unalign=sys.argv[3]


dat=pd.read_csv(input_tom,sep='\t')
ids=list(set([i for i in dat[dat.columns.tolist()[0]]]))
unalign_list=[]
for i in range(0,idx):
    if 'kernel%d'%i not in ids:
        unalign_list.append('kernel%d'%i)
with open(output_unalign,'w') as file:
    for i in unalign_list:
        file.write(i+'\n')
