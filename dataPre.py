# --*-- coding:utf-8 --*--
import os
# path='./NERdata'
def dataPre(path,file_name):
    num=0
    try:
        with open(os.path.join(path,file_name),'a+') as wf:
            for file in os.listdir(path):
               try:
                    with open(os.path.join(path,file),'r') as fd:
                        item=fd.read()
                        print(len(item))
                        num+=len(item)
                        wf.write(item)
               except:
                   print("文件打开异常")
               finally:
                   fd.close()
            print(num)
    finally:
        wf.close()
    print("文件写入完毕")

def dataPre2(root_path,file,file_name):
    try:
        with open(os.path.join(root_path,file_name),'a+') as wf:
               try:
                    with open(os.path.join(root_path,file),'r') as fd:
                        item=fd.read()
                        print(len(item))
                        wf.write(item)
               except:
                   print("文件打开异常")
               finally:
                   fd.close()
    finally:
        wf.close()
    print("文件写入完毕")
    return len(item)


if __name__ == '__main__':
    root_path='./test/201901302011/iob'
    file_name1='dev.txt'
    file_name2='test.txt'
    file_list=os.listdir(root_path)
    num1 = 0
    num2 = 0
    for i,item in enumerate(file_list):
        if(i<45):
            #dev.txt
            len1=dataPre2(root_path,item,file_name1)
            num1+=len1
        else:
            #test.text
            len2=dataPre2(root_path, item, file_name2)
            num2+=len2
    print(num1)
    print(num2)
    # file_name='dev.txt'
    # dataPre(path,file_name)
    # with open(os.path.join(path,file_name),'r') as ff:
    #     train_data=ff.read()
    # print(len(train_data))