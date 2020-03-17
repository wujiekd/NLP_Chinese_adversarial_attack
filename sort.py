import fasttext
import re


f1 = open("./vocab.txt","r")
goodlines = f1.readlines()
REGEX_TO_REMOVE = re.compile(r"[^\u4E00-\u9FA5a-zA-Z0-9\!\@\#\$\%\^\&\*\(\)\-\_\+\=\`\~\\\|\[\]\{\}\:\;\"\'\,\<\.\>\/\?\ \t，。！？]")
model = fasttext.load_model('reference_model/mini-explicit-labels.ftz')

goodline_s = [REGEX_TO_REMOVE.sub(r'', line) for line in goodlines]


strs=""
for ch in goodline_s:
    strs =strs +ch

dict = {}
for st in strs:
    sss = model.predict(st, k=2)
    if (sss[0][0] == '__label__辱骂'):
        num = sss[1][0]
    else:
        num = sss[1][1]
    dict[st]= num

ss = sorted(dict.items(), key=lambda item:item[1], reverse=True)



out=open("./sort.txt",'w')
lists = [sentence[0]+"："+str(sentence[1]) + "\n"  for sentence in ss]
out.writelines(lists)
