# coding=utf-8
import codecs
import re

fw = codecs.open('personLabel.txt', 'w', 'utf-8', errors='ignore')
for (num,line) in enumerate(codecs.open('name_recogination_data.txt', 'r', 'utf-8',errors='ignore')):
    datas = line.strip().split('\t')
    if len(datas)>2:
        labels = datas[len(datas)-1]
        sen = line.replace(labels, '').replace('\t', '')
    else:
        sen = datas[0]
        labels = datas[1]
    if labels == '-1':
        for char in sen:
            print(char+" O")
            fw.write(char+" O"+'\n')
        print("end")
        fw.write('end'+'\n')
    else:
        print(sen)
        label_list = []
        labels = labels.split(';')
        label_list = [i for i in labels if i.strip()]
        label_list = list(set(label_list))
        print(label_list)
        index_list = []
        index_all = {}
        for label in label_list:  #将标签对应的index存储在index_list中
            ilist = [(i.start(), i.end()) for i in re.finditer(label, sen)]
            index_list += ilist
        index_list = sorted(index_list, key=lambda x:x[0], reverse=False)
        # 解决手机名在字符串中不完全匹配的情况
        for i in range(1,len(index_list)):
            if index_list[i][0] == index_list[i - 1][0]:#起点相同，终点不同，说明代表着同一个实体
                large = index_list[i][1] if index_list[i][1] > index_list[i - 1][1] else index_list[i - 1][1]
                index_list[i] = (index_list[i][0], large)
                index_list[i - 1] = (index_list[i][0], large)
            elif index_list[i][0] > index_list[i-1][0] and index_list[i][1] <= index_list[i-1][1]:#后一个被前一个包含，则将边界修改成一样的，否则，代表了句子中的两个实体
                index_list[i] = (index_list[i-1][0], index_list[i-1][1])
        index_list = list(set(index_list))
        print(index_list)
        for i in index_list:#将index存储成词典的形式
            start = i[0]
            end = i[1]
            index_all[start] = end - 1
        start = -1
        end = -1
        for i in range(0, len(sen)):
            if i in index_all:#在标记的词典里
                start = i #则标记出词典边界
                end = index_all[i]
                print(sen[i] + " B-PER")
                fw.write(sen[i] + " B-PER" + '\n')
            elif end > i > start:
                print(sen[i] + " I-PER")
                fw.write(sen[i] + " I-PER" + '\n')
            elif i == end:
                print(sen[i] + " E-PER")
                fw.write(sen[i] + " E-PER" + '\n')
            else:
                print(sen[i] + " O")
                fw.write(sen[i] + " O" + '\n')
        print("end")
        fw.write("end" + '\n')







