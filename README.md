# Restricted Translation Task 2021 in WAT2021

Restricted Translation Task is held in WAT2021, which need to translate based on given restricted target vocabularies. Please see [Website](https://sites.google.com/view/restricted-translation-task/top?authuser=0) in details.

- [2022](https://github.com/Chanabe-k/wat2022_restricted/)
- 2021

## requirements
- python 3.8
- (for evaluation) `pip install sacrebleu[ja]`

## terminologies (restricted target vocabulary lists)
- Please download the above website.

## evaluation
- We calculate two distinct metrics in this task.
1. BLEU score
2. A consistency score: the ratio of #sentences satisfying **exact match** of given constraints over the whole test corpus

For the "exact match" evaluation, we will conduct the following process:

- English: simply lowercase hypotheses and constraints, then judge character level sequence matching (including whitespaces) for each constraint
- Japanese: judge character level sequence matching (including whitespaces) for each constraint without preprocessing
