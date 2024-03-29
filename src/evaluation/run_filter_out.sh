set -eux

LANG=$1 # ja/en
DIRECTION=$2 #en-ja/ja-en

HOME_PATH=/Users/abe-k/restricted_translation/wat2021_restricted/
OUTPUTS_PATH=${HOME_PATH}submitted_outputs/${DIRECTION}

echo $OUTPUTS_PATH

for OUTPUT_PATH in $( ls ${OUTPUTS_PATH})
do
echo $OUTPUT_PATH
# normal
FILTERED_OUTPUT_PATH=${HOME_PATH}work/filtered_outputs/${DIRECTION}/${OUTPUT_PATH}.filtered
# remove backslash
# FILTERED_OUTPUT_PATH=${HOME_PATH}work/filtered_outputs_includeslash/${DIRECTION}/${OUTPUT_PATH}.filtered
python ${HOME_PATH}src/evaluation/filter_out_sentences.py --dic ${HOME_PATH}data/dic/test.dic.${LANG} --input ${OUTPUTS_PATH}/${OUTPUT_PATH} --output ${FILTERED_OUTPUT_PATH} --lang ${LANG}
done