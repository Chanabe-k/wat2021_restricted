set -eux

LANG=ja # ja
DIRECTION=en-ja #en-ja

HOME_PATH=/Users/abe-k/wat2021_sharedtask/
GOLD_PATH=${HOME_PATH}data/test_gold.${LANG}
FILTERED_OUTPUTS_PATH=${HOME_PATH}work/filtered_outputs/${DIRECTION}
# RESULT_PATH=${HOME_PATH}work/all_results_${DIRECTION}.txt

for OUTPUT_PATH in $( ls ${FILTERED_OUTPUTS_PATH})
do
echo ${OUTPUT_PATH}
#LC_ALL=ja_jp.utf-8 perl ${HOME_PATH}src/evaluation/multi-bleu.perl ${GOLD_PATH} < ${FILTERED_OUTPUTS_PATH}/${OUTPUT_PATH}
cat ${FILTERED_OUTPUTS_PATH}/${OUTPUT_PATH} | sacrebleu ${GOLD_PATH} -l ${DIRECTION} -tok ja-mecab
done
