idx=(0 1 2 3 4)
PERIOD="initiation"
SEQ="init"
for id in ${idx[*]}
do
	python 13extract_meme.py unalign/${PERIOD}/${PERIOD}${id}/unalign.txt align/${PERIOD}/kernel_motif_${id}.meme unalign/${PERIOD}/${PERIOD}${id}/unalign.meme
	cat motif.header unalign/${PERIOD}/${PERIOD}${id}/unalign.meme>unalign/${PERIOD}/${PERIOD}${id}/unalign.result.meme
	fimo  --oc unalign/${PERIOD}/${PERIOD}${id}/fimo/ --norc  unalign/${PERIOD}/${PERIOD}${id}/unalign.result.meme sequence/${PERIOD}/${SEQ}_utr5.fa
done	
