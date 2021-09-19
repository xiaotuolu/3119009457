import re
from math import sqrt
import jieba
import sys
import os
def compare():
    file1 = input("输入文件一路径：")

    file2 = input("输入文件二路径：")

    #判断文件一是否存在，是否为空
    if os.path.exists(file1):

        size1 = os.path.getsize(file1)

        if size1:

            pass

        else:

            print("第一个文件为空")

            sys.exit()

    else:

        print("文件一不存在")

        sys.exit()

    #判断文件二是否存在，是否为空
    if os.path.exists(file2):

        size2 = os.path.getsize(file2)

        if size2:

            pass

        else:

            print("第二个文件为空")

            sys.exit()

    else:

        print("文件二不存在")

        sys.exit()

    #该字典用来存放关键词及其权重
    words = {}

    #该列表存放停用词
    list = ['的','了','和','呢','啊','哦','恩','嗯','吧'];

    #编译中文正则表达式
    accepted_chars = re.compile('[\u4E00-\u9FA5]+$')

    try:

        #读取文件一
        file_object1 = open(file1, 'r', encoding='utf-8')

        all_the_text = file_object1.read()

        #用jieba进行分词
        seg_list = jieba.cut(all_the_text, cut_all=True)

        #遍历循环该列表，将不在停用词列表中的中文字词作为键，值是只有两个初始元素为0的列表。如果该字词第一次出现，则这个键对应的值的第一个元素为1，如果不是第一次出现，这个列表值的第一个元素加1
        for s in seg_list:

            if accepted_chars.match(s) and s not in list:

                if s not in words.keys():

                    words[s] = [1,0]

                else:

                    words[s][0] += 1

    finally:

            file_object1.close()



    try:

        #读取文件二
        file_object2 = open(file2, 'r', encoding='utf-8')

        all_the_text = file_object2.read()

        #进行分词
        seg_list = jieba.cut(all_the_text, cut_all=True)

        #遍历循环该列表，将不在停用词列表中的中文字词作为键，值是只有两个初始元素为0的列表。如果该字词第一次出现，则这个键对应的值的第二个元素为1，如果不是第一次出现，这个列表值的第二个元素加1
        for s in seg_list:

            if accepted_chars.match(s) and s not in list:

                if s not in words.keys():

                    words[s] = [0,1]

                else:

                    words[s][1] += 1

    finally:

        file_object2.close()

    #用余弦算法计算相似率
    sum = 0

    sum1 = 0

    sum2 = 0

    for word in words.values():

        sum += word[0]*word[1]

        sum1 += word[0]**2

        sum2 += word[1]**2

        cos = sum/(sqrt(sum1*sum2))

    cos *= 100

    result = open('C:/test/result.txt', 'a+', encoding='utf-8')

    result.write("%s和%s的相似率为：%.2f%% \n" % (file1,file2,cos))

    result.close()

    print("结果已保存在result.txt,相似率为：%.2f%%" % cos)
compare()

