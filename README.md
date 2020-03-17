## F-LAB-sparrow(the fourth finalist of the competition) overall scheme - Competition submission code

The contest's website:https://tianchi.aliyun.com/competition/entrance/231762/introduction

Official model download link:http://aliyuntianchiresult.cn-hangzhou.oss.aliyun-inc.com/file/race/documents/231762/securityAI3_materials.zip?Expires=1584531462&OSSAccessKeyId=LTAILBoOl5drlflK&Signature=mKjYVanPXOdn3KkMgRohrY30t3M%3D&response-content-disposition=attachment%3B%20

### Document describing

#### README.md         
This explanatory document

#### vocab.txt
7,000 Chinese characters are commonly used

#### sort.py           
The Chinese characters of vocab.txt were sorted by using the officially provided model

#### sort.txt          
The generated sorted Chinese character table selects the alternate Chinese characters in choose.py

#### choose.py
Filter for substituted homophones

#### raw.txt
The substituted word is used in the main function

#### change.txt
The substitution is used in the main function

#### main.py
Main function that generates the adversarial text
