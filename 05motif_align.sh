idx=(0 1 2 3 4)
PERIOD="scw"
for id in ${idx[*]}
do
	chen2meme deeplift/${PERIOD}/kernel_motif_${id}.txt >align/${PERIOD}/kernel_motif_${id}.meme
	tomtom -oc align/${PERIOD}/${PERIOD}${id} -thresh 0.1  align/${PERIOD}/kernel_motif_${id}.meme database/JASPAR2018_CORE_plants_non_redundant.meme
	python 10filter_tom.py align/${PERIOD}/${PERIOD}${id}/tomtom.txt align/${PERIOD}/${PERIOD}${id}/tomtom.filter.txt
done
