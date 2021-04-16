set -eux

for i in $(seq 2 9)
do
    cat ../data/annotated_data_from_drive/annotator_$i/*_words_*.txt > ../data/annotated_data_all/annotator_$i.txt
done