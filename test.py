

# 模块功能：
# 一个保存了400W条分词后的中文文本数据的文件，每条数据大概200-400个词，
# 现在需要统计输出总共的词汇量。
import os
from collections import Counter
from tqdm import tqdm


def get_sentence_words(path):
    files = os.listdir(path)  #os.listdir() 用于返回指定的文件夹包含的文件
    for file in files:
        file_path = os.path.join(path, file) # 将多个路径组合后返回
        with open(file_path, 'r',encoding='utf-8') as f:
            for line in tqdm(f, desc='read sentence_cuts'):# tqdm可以不用
                line = line.strip().split('\t')
                words = line[1]
                for word in words:
                    # print(word)
                    yield word

if __name__ == '__main__':
    words_gen = get_sentence_words('D:\\trans')
    weight_dict = Counter(words_gen)  #counter() 计数，统计词频
    print(weight_dict)
    print('len(weight_dict)',len(weight_dict))
    total = 0
    for v in weight_dict.values():
        total += v
    print('total words is %d'% total)
