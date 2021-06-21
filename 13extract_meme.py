import sys
protein_file=sys.argv[1]
meme_file=sys.argv[2]
out_file=sys.argv[3]
with open(protein_file,'r') as file:
    protein_list=[]
    for line in file:
        line=line.strip()
        protein_list.append(line)
with open(meme_file,'r') as file:
    dic={}
    flag=0
    name,matrix,tmp,letter=[],[],[],[]
    for line in file:
        line=line.strip()
        if 'MOTIF' in line:
            name.append(line)
            matrix.append('\n'.join(tmp))
            tmp=[]
        elif 'letter-' in line:
            letter.append(line)
        elif (line.startswith('0'))|(line.startswith('1')):
            tmp.append(line)
        else:
            continue
    matrix.append('\n'.join(tmp))
    tmp=[]
    matrix=matrix[1:]
for i,j,z in zip(name,matrix,letter):
    dic[i]=(z,j)
extract_list=[]
for i in protein_list:
    for j in dic.keys():
        if i in j:
            extract_list.append(j)
            break
        else:
            continue
with open(out_file,'w') as file:
    for i in extract_list:
        file.write(i+'\n')
        file.write('\n')
        file.write(dic[i][0]+'\n')
        file.write(dic[i][1]+'\n')
        file.write('URL=13extraction\n')
        file.write('\n')

            
