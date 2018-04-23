# -*- coding:utf-8 -*-

#天龙八部分词统计
import jieba
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

s={}e
with open('F:\\tlbb.txt','r') as  files:
	fid = files.read()
	fc = jieba.cut(fid)   #用jieba分词

	for words in fc:
		if len(words)>1:
			s[words] = s.get(words,0)+1

	word = sorted(s.items(),key=lambda (word,count):count,reverse=True)
	word = dict(word[1:100])
	# for x in word:
	# 	print x ,
	wordcloud = WordCloud(font_path = 'C:/Windows/Fonts/msyh.ttf',		# 设置字体格式，如不设置显示不了中文
						  background_color="black",		 # 设置背景颜色
						  stopwords=STOPWORDS,  # 设置停用词
						  max_font_size=100,		# 设置字体最大值
						  random_state=30,	# 设置有多少种随机生成状态，即有多少种配色方案
						  relative_scaling=.5
						  ).fit_words(word)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()
files.close()


