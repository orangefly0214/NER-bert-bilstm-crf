# NER-bert-bilstm-crf
use bert-bilstm-crf to do the specific ner task.

1.before we start our task,we shoud download the pretrained Chinese model chinese_L-12_H-768_A-12 to current path

2.then we get bert source code from https://github.com/google-research/bert

3.then,edit the ralated path in bert_lstm_crf.py and add your own label in utils.py 

4.we should create a folder named NERdata,the NERdata need include our training corpurs and we should named them like train.txt,test.txt,dev.txt,both of them was labeled as BIO format.

then we create a folder named output to store our training output model and related files.

5.finally,start your own train.
