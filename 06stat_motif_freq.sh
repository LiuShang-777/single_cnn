idx=(0 1 2 3 4)
PERIOD="initiation"
thre=2


FILE_LIST=()
for id in ${idx[*]}
do
	FILE_LIST+=(${PERIOD}${id})
done
python 11stat_motif_presence.py database/JASPAR2018_CORE_plants_non_redundant.meme align/${PERIOD}/${PERIOD}_more_than_${thre}.txt ${PERIOD} ${thre} ${FILE_LIST[*]}
