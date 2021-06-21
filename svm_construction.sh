PERIOD="scw"
SEQ="scw"

python 13extract_meme.py align/${PERIOD}/${PERIOD}_more_than_2.txt database/JASPAR2018_CORE_plants_non_redundant.meme align/${PERIOD}_cnn.meme
cat motif.header align/${PERIOD}_cnn.meme >align/${PERIOD}_cnn.final.meme
fimo --oc align/${PERIOD}_fimo_cnn/ --norc align/${PERIOD}_cnn.final.meme sequence/${PERIOD}/${SEQ}_utr5.fa
python 14extract_features_svm.py align/${PERIOD}_fimo_cnn/fimo.txt sequence/${PERIOD}/${SEQ}_utr5.fa align/${PERIOD}_cnn.csv 
python 15add_label.py align/${PERIOD}_cnn.csv align/${PERIOD}_cnn.result.csv
python SVM.py align/${PERIOD}_cnn.result.csv >align/${PERIOD}_cnn.log&
