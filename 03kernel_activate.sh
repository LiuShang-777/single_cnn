#modified three para in py scripts
idx=(0 1 2 3 4)
for id in ${idx[*]}
do
	python 07get_hot_kernals.py sequence/scw/24_16_10 ${id} deeplift/scw sequence/scw/scw_utr5.fa
done
python 08activate_kernal_visual.py deeplift/scw/ kernel.png
