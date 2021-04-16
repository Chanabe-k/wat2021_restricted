from itertools import groupby

sets = ['dev', 'devtest', 'test']
for set_name in sets:

    vocab_ja_path = f"../data/vocabulary/{set_name}.dic.ja"
    vocab_en_path = f"../data/vocabulary/{set_name}.dic.en"
    tsv_path = f"../data/orig_data/tsv/{set_name}.tsv"

    def get_vocab_list(f_obj) -> list:
        vocab_list = []
        for is_newline, g_rtv in groupby(f_obj, lambda line: line.strip(' ') == '\n'):
            l_rtv = list(g_rtv)
            l_rtv_clean = [rtv.strip('\n') for rtv in l_rtv]
            vocab_list.append(l_rtv_clean)
        return vocab_list

    with open(vocab_ja_path) as f_v_ja, open(vocab_en_path) as f_v_en:
        vocab_ja = get_vocab_list(f_v_ja)
        vocab_en = get_vocab_list(f_v_en)
        assert len(vocab_ja) == len(vocab_en)

    write_path = f"restricted_translation_{set_name}.tsv"
    with open(write_path, 'w') as f_w:
        for orig_line, v_ja, v_en in zip(open(tsv_path), vocab_ja, vocab_en):
            original_line = orig_line.strip()
            print('\t'.join([original_line, str(v_ja), str(v_en)]))
            # f_w.write('\t'.join([original_line, str(v_ja), str(v_en)]) + '\n')
    print(f"> {write_path}")