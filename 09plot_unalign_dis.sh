idx=(0 1 2 3 4)
PERIOD="elongation"
SEQ="elong"
for id in ${idx[*]}
do
	python 17plot_motif_distribution.py unalign/${PERIOD}/${PERIOD}${id}/fimo/fimo.txt
done	
