from tqdm import tqdm
import re
import argparse

def filter_sentence_with_dic(sentence: str, dic: list):
    def _remove_punctuation(word):
        punctuations = r'\'"「」\()（）'
        for punc in punctuations:
            word = word.replace(punc, '')
        return word
    
    # Check whether the sent contains all the restricted words
    match_count = 0
    for word in dic:
        # Remove punctuation ('',"", 「」, () ...) from word
        word = _remove_punctuation(word)
        
        if re.search(word, sentence):
            match_count += 1
    
    # Filter
    if match_count == len(dic):
        return sentence
    else:
        return ''

def get_dic(file_path: str):
    """Load dictionary information (get dic_list)
    input: file_path(str)"""
    c = []
    for l in open(file_path):
        l = l.strip()
        if l:
            c.append(l)
        else:
            yield c
            c = []        
    yield c
        
def main():
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('--dic', type=str, help='Path to dictionary file')
    parser.add_argument('--input', type=str, help='Path to Input file (model output)')
    parser.add_argument('--output', type=str, help='Output name')
    args = parser.parse_args()

    # TODO: jaの場合、いったんdetokenizeする必要がある
    # dic_path = "../data/golddata_20210311/test.dic.en"
    # output_path = "../data/sample_output.en"
    # filtered_output_path = "../work/filtered_sample_output.en"
    dic_path = args.dic
    input_path = args.input
    filtered_output_path = args.output

    dic_list = list(get_dic(dic_path))
    print(f"dic length: {len(dic_list[:-1])}")

    with open(filtered_output_path, 'w') as f_filtered:
        # Exact match between dictionary and output 
        with open(input_path) as f_out:
            # Check file length == dictionary length
            sents = [l.strip() for l in f_out]
            assert len(sents) == len(dic_list[:-1]), "not match file length and dictionary length"
            
            # Filter out sentences not containing restricted vocab
            for sent, dic in tqdm(zip(sents, dic_list[:-1])):
                # Debug
                # print(dic_en, out_en)
                filtered_sent = filter_sentence_with_dic(sent, dic)
                f_filtered.write(filtered_sent + '\n')
        print(f"> {filtered_output_path}")

main()