PERIOD="initiation"
idx=(0 1 2 3 4)
seqs=()
for id in ${idx[*]}
do
	seqs+=("unalign/${PERIOD}/${PERIOD}${id}/fimo/fimo.txt")
done
python 19collect_unali_seq.py unalign/${PERIOD}/kegg_candidate.txt ${seqs[*]}
