set -eux

LANG=ja # ja
DIRECTION=en-ja #en-ja

HOME_PATH=/Users/abe-k/wat2021_sharedtask/
OUTPUTS_PATH=${HOME_PATH}submitted_outputs/${DIRECTION}

echo $OUTPUTS_PATH

for OUTPUT_PATH in $( ls ${OUTPUTS_PATH})
do
echo $OUTPUT_PATH
FILTERED_OUTPUT_PATH=${HOME_PATH}work/filtered_outputs/${DIRECTION}/${OUTPUT_PATH}.filtered
python ${HOME_PATH}src/evaluation/filter_out_sentences.py --dic ${HOME_PATH}data/dic/test.dic.${LANG} --input ${OUTPUTS_PATH}/${OUTPUT_PATH} --output ${FILTERED_OUTPUT_PATH} --lang ${LANG}
done