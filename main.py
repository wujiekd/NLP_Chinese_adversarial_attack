# 加载Python自带 或通过pip安装的模块
import random
import jieba
import json
# ----------------------------------------
# 本地调试时使用的路径配置
#inp_path = '/Users/harry/tianchi_docs/benchmark_texts.txt'
#out_path = 'adversarial.txt'
# ----------------------------------------

# ----------------------------------------
# 提交时使用的路径配置（提交时请激活）
raw_path = 'raw.txt'
change_path = 'change.txt'
inp_path = '/tcdata/benchmark_texts.txt'
out_path = 'adversarial.txt'
# ----------------------------------------


with open(inp_path, 'r') as f:
    inp_lines = f.readlines()

with open(raw_path, 'r') as f:
    raw_lines = f.readlines()
raw_word_dict = [line.replace('\n', '').split(":") for line in raw_lines]
#The words are arranged in order of weight from large to small
raw_word = [line[0] for line in raw_word_dict]
#The weight of all values adds up to 1
raw_word_weight =[float(line[1]) for line in raw_word_dict]

with open(change_path, 'r') as f:
    change_lines = f.readlines()
change_word = [line.replace('\n', '') for line in change_lines]


def transform(line):
    """转换一行文本。

    :param line: 对抗攻击前的输入文本
    :type line: str
    :returns: str -- 对抗攻击后的输出文门
    """

    alpha = 0
    value = 0
    mark = 0
    statistics = []
    num1 = random.random()
    num2 = random.random()

    #Add noise to the text
    list_line = list(line)
    out_line = '3' + '3'.join(list_line)

    #Count the number of key characters, the characters are still sorted by weight, from large to small
    for ch in raw_word:
        if ch in out_line:
            statistics.append(ch)
            value += raw_word_weight[raw_word.index(ch)]

    #Random selection of a replacement character, of course, the greater the probability that the preceding word will be replaced
    for ch in statistics:
        num1 = num1 - raw_word_weight[raw_word.index(ch)]/value
        if num1 > 0:
            mark +=1

    #Set a threshold whether to replace
    if num2 >alpha:
        if statistics != []:
            out_line = out_line.replace(statistics[mark], change_word[raw_word.index(statistics[mark])])

    out_line = out_line.replace("\n", "")

    return out_line

out_lines = [transform(_line) for _line in inp_lines]
target = json.dumps({'text': out_lines}, ensure_ascii=False)

with open(out_path, 'w') as f:
 f.write(target)
