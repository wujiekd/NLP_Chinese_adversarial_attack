## F-LAB-sparrow（线上第五名）整体方案-镜像源码

### 文件说明
./
├── README.md                           | 这篇说明文档
├── vocab.txt                        		 | 常用中文汉字大约7000个
├── sort.py                                	 | 对vocab.txt的汉字使用官方提供模型进行排序
├── sort.txt                              | 生成的排序汉字表，将在choose.py中挑选替换的汉字
├── choose.py                                | 筛选替换的同音字
├──  raw.txt                                     | 被替换的字，在主函数中用到
├── change.txt                                | 替换的字，在主函数中用到
└── main.py                                    |主函数，生成对抗文本


