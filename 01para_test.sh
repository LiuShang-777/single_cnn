filters=(8 12 16 20 24 28 32)
kernels=(12 14 16 18 20 22)
maxs=(2 4 6 8 10)
for filter in ${filters[*]}
do
	for kernel in ${kernels[*]}
	do
		for max in ${maxs[*]}
		do
			python 01single_detect.py sequence/scw/scw_utr5.fa sequence/scw/${filter}_${kernel}_${max} ${filter} ${kernel} ${max}
		done
	done
done
