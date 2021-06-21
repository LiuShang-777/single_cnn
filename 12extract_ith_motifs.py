import sys
inputf=sys.argv[1]
num=int(sys.argv[2])
outputf=sys.argv[3]
with open(inputf,'r') as file:
    list_=[]
    for line in file:
        if ('p-value' in line)&('top' in line):
            line=line.split(' top')[0]
            list_.append(' '.join(line.split(' ')[-2:]))
        else:
            continue
list_result=list_[:num]
with open(outputf,'w') as file:
    for i in list_result:
        file.write(i+'\n')

