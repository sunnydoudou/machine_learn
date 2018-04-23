# -*- coding:utf-8 -*-
import re

wordcount = {}
stopwords=[]
# stopwords = [u'好',u'一',u'的',u'了']

with open('F:\\tlbb.txt','r') as  files:
	text = files.read().decode('gb18030')
	text = text.strip('\n').strip('\t').strip(' ')
	string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[：“”+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),text)
	for word in string:
		if word in stopwords:
			continue
		wordcount[word] = wordcount.get(word,0)+1
	wordcount = sorted(wordcount.items(),key=lambda d:d[1],reverse=True)
	print len(wordcount)
	for x in xrange(20):
		print wordcount[x][0]+':'+str(wordcount[x][1])
files.close()