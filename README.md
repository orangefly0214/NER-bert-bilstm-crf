# NER-bert-bilstm-crf
use bert-bilstm-crf to do the specific ner task.

1.before we start our task,we shoud download the pretrained Chinese model chinese_L-12_H-768_A-12 to current path

2.then we get bert source code from https://github.com/google-research/bert

3.last,edit the ralated path in bert_lstm_crf.py and add your own label in utils.py and start your train.
