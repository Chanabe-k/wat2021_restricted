from ginza import *
import spacy

nlp = spacy.load('ja_ginza')

for i, line in enumerate(open('../data/orig_data/tsv/dev.tsv')):
    line = line.strip()

    #sent_id, _, ja_text, en_text = line.split('\t')
    ja_text = "2018年の夏にフランスに行った。ジベルニー村のジャン・クロード・モネの家で池に浮かぶ睡蓮を見た。"

    print(ja_text)
    doc = nlp(ja_text)
    try:
        for ent in doc.ent:
            print(ent.text, ent.label_)
    except AttributeError as e:
            print("entity no match")
    if i > 5:
        break