#setting parameters
INPUT_DIR="/home/ls/singlecnn/sequence/scw/"
PARA="24_16_10"
SYMBOL="scw"
OUTDIR="/home/ls/singlecnn/deeplift/scw/"

arrays=(0 1 2 3 4 )
for array in ${arrays[*]}
do
	python 03get_deeplift_input.py ${INPUT_DIR}${PARA}/${PARA}_${SYMBOL}true${array}.txt ${INPUT_DIR}${SYMBOL}_utr5.fa ${OUTDIR}${PARA}_${array}.fa
	python 04shuffle.py ${OUTDIR}${PARA}_${array}.fa ${OUTDIR}${PARA}_${array}.shuffle.fa
	python 05deeplift_total.py ${INPUT_DIR}${PARA}/model${array}.h5 ${OUTDIR}${PARA}_${array}.fa ${OUTDIR}${PARA}_${array}.shuffle.fa ${OUTDIR}${PARA}_${array}.ex.npy ${OUTDIR}${PARA}_${array}.no.npy
done
python 06deeplift_visual.py ${OUTDIR} ${SYMBOL}
