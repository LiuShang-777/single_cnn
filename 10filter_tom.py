import pandas as pd
import sys
inputf=sys.argv[1]
outputf=sys.argv[2]
dat=pd.read_csv(inputf,sep='\t')
dat=dat.loc[dat['Orientation']=='+']
dat.to_csv(outputf,sep='\t')
