# WAT2021_Restricted_Translation_Task

- Restricted Translation Task is held in WAT2021, which need to translate based on given restricted target vocabularies. Please see [Website (2021)](https://sites.google.com/view/restricted-translation-task/2021?authuser=0) in details.

## requirements
- python 3.8
- `pip install -r requirements.txt`
- (for evaluation) `pip install sacrebleu[ja]`

## terminologies
- Please download the above website.

## evaluation
- We calculate two distinct metrics in this task.
1. BLEU score
2. A consistency score: the ratio of #sentences satisfying **exact match** of given constraints over the whole test corpus

For the "exact match" evaluation, we will conduct the following process:

- English: simply lowercase hypotheses and constraints, then judge character level sequence matching (including whitespaces) for each constraint
- Japanese: judge character level sequence matching (including whitespaces) for each constraint without preprocessing
