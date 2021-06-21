idx=(0 1 2 3 4)
PERIOD="scw"
KERNEL=24
for id in ${idx[*]}
do
	tomtom -oc unalign/${PERIOD}/${PERIOD}${id}   align/${PERIOD}/kernel_motif_${id}.meme database/JASPAR2018_CORE_plants_non_redundant.meme
	#python 18get_unalign_kernel.py unalign/${PERIOD}/${PERIOD}${id}/tomtom.txt ${KERNEL} unalign/${PERIOD}/${PERIOD}${id}/unalign.txt
        #python 13extract_meme.py unalign/${PERIOD}/${PERIOD}${id}/unalign.txt database/JASPAR2018_CORE_plants_non_redundant.meme unalign/${PERIOD}/${PERIOD}${id}/unalign.meme
		
done
