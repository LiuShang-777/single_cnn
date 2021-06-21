#modify dir in all out para
ids=(0 1 2 3 4)
for id in ${ids[*]}
do
	python 09motif_trans_kernal.py sequence/initiation/24_14_10/model${id}.h5 deeplift/initiation/kernel_motif_${id}.txt deeplift/initiation/kernel_n_analysis_${id}.csv
done
