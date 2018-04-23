# -*- coding:utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt

class Kmeans():
	def __init__(self,dataSet,k):
		self.dataSet = dataSet
		self.k = k    #质点数
		self.numSamples = dataSet.shape[0]    #矩阵的行数
		self.dim = dataSet.shape[1]     #矩阵的列数
		self.signData  = mat(zeros((self.numSamples,2)))  #标签矩阵

#计算欧氏距离
	def euclDistance(self,vector1,vector2):
		return sqrt(sum(power(vector1 - vector2 ,2)))


	def dataCount(self):
		print u"开始质心选取"
		# centroids = zeros((self.k,self.dim))
		tem = [int(random.uniform(0,self.numSamples)) for i in xrange(self.k)]
		centroids = self.dataSet[tem]

		print u'初始化质点点完成\n'
		print centroids

		clusterChanged = True

		print u"开始分类"
		count = 0
		while clusterChanged:
			clusterChanged = False
			for i in xrange(self.numSamples):
				minDist = 1000000000
				index = 0

				for j in xrange(self.k):
					distance = self.euclDistance(centroids[j,:],self.dataSet[i,:])
					if distance < minDist:
						minDist = distance
						index = j

				#检查标签
				if self.signData[i,0] != index:
					clusterChanged = True
					self.signData[i,:] = index,minDist**2

			#更新质点
			for i in range(self.k):
				pointsInCluster = self.dataSet[nonzero(self.signData[:,0].A==i)[0]]
				centroids[i,:] = mean(pointsInCluster,axis=0)
			count +=1
			print u"第{}轮更新质点完成\n".format(count)
			print centroids
			print '*'*200  #分隔

		print u"已完成数据分类"

		print u'开始绘图'
		if self.dim !=2:
			print u"无法绘制2纬图"
			return 1
		mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  #设置绘图颜色
		if k > len(mark):
			print u"选择的类别数太大，请重新确认类别数"
			return 1

		for i in xrange(self.numSamples):
			markIndex = int(self.signData[i,0])
			plt.plot(self.dataSet[i,0],self.dataSet[i,1],mark[markIndex])  #绘制分类图形

		mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb'] #设置质心绘图颜色
		for i in range(self.k):
			plt.plot(centroids[i,0],centroids[i,1],mark[i],markersize=12)

		plt.show()


if __name__=='__main__':

	print u'开始读取数据'
	dataSet = []
	with open('D:/datajl.txt') as files:
		for line in files.readlines():
			line = line.strip().split(',')
			# print line,type(line)
			dataSet.append([float(line[0]),float(line[1])])
	dataSet = mat(dataSet)

	print u'绘制散点图'
	for x in xrange(dataSet.shape[0]):
		plt.plot(dataSet[x,0],dataSet[x,1],'ob')
	plt.show()
	k = 4
	print u'开始进行数据聚类'
	Kmeans = Kmeans(dataSet,k)
	Kmeans.dataCount()

















