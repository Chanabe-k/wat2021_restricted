# DATA

## self_annotated_data
- 自分(abe-k)が担当したannotationデータ (annotation_1に該当)
    - {dev/devtest/test}.tsv.shuf.01 ... 参考にする文データ（他のアノテータにも同様のデータ(02, 03, ...)を配布）
    - en_words_{dev/devtest/test}.txt ... ^ を元に抽出した制約リスト（英語）
    - ja_words_{dev/devtest/test}.txt ... ^ を元に抽出した制約リスト（日本語）

    - 100sample_annotate(.numbers) ... オーガナイザ間で100件試しにannotationしたときのデータ

## annotated_data_from_drive
- Google Driveの「アノテーション共有用」をとってきたやつ

## 謝金手続き用
- 謝金手続きのために作成したFile等。アノテータがつけた作業データを全部concatして送る必要があった。
- annotation_data_all(.zip) ... 実際に謝金を払うアノテータにつけてもらったデータを集約したもの
- exp_extract_phrasepair_task.txt ... ^ を結局全てconcatする必要があったため、1つのtxtファイルにconcatしたもの（たぶんこれを送った）

## orig_data
- ASPECのoriginal data 
    - aspec-je.*.{en/ja}_orig ... 本文部分だけ抽出したもの, tokenize済（鈴木Jさん作）
    - txt -- {dev/devtest/test}.txt ... 本当の大元ファイル。delimiterが`|`
    - tsv -- *.tsv ... 上のtxtファイルのdelimiterを`\t`にしたもの。

## dic / vocabulary
- dictionary file
- 変更後がdic?

## dic_full
- 江里口さんが元データにdicを紐づけてくださったもの
- らしいが、紐づいているdicは修正前らしい......？
