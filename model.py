# -*- coding:utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture as gm
from data import datatrain,datatest
from sklearn import metrics

class kmeans():
    def __init__(self,datatrain,datatest):
        self.datatrain=datatrain
        self.datatest=datatest
        self.s=None
    def train(self):
        #训练阶段
        clf=KMeans(n_clusters=2)
        label=self.datatrain.iloc[:,0]
        label=6-label
        self.datatrain=self.datatrain.iloc[:,1:]
        self.s=clf.fit(self.datatrain.values)
        prd=self.s.predict(self.datatrain.values)
        score = metrics.accuracy_score(label, prd)
        print('kmeans train accuracy : %s'%score)
    def test(self):
        # 测试阶段
        self.train()
        labelt=self.datatest.iloc[:,0]
        labelt=6-labelt
        self.datatest=self.datatest.iloc[:,1:]
        prdt=self.s.predict(self.datatest.values)
        score=metrics.accuracy_score(labelt,prdt)
        print('kmeans test accuracy : %s'%score)
class em():
    def __init__(self,datatrain,datatest):
        self.datatrain=datatrain
        self.datatest=datatest
        self.s=None
    def train(self):
        clf=gm(n_components=2,covariance_type='full')
        label = self.datatrain.iloc[:, 0]
        label = 6-label
        self.datatrain = self.datatrain.iloc[:, 1:]
        self.s = clf.fit(self.datatrain.values)
        prd = self.s.predict(self.datatrain.values)
        score = metrics.accuracy_score(label, prd)
        print('GaussianMixture train accuracy: %s'%score)
    def test(self):
        # 测试阶段
        self.train()
        labelt = self.datatest.iloc[:, 0]
        labelt = 6-labelt
        self.datatest = self.datatest.iloc[:, 1:]
        prdt = self.s.predict(self.datatest.values)
        score = metrics.accuracy_score(labelt, prdt)
        print('GaussianMixture test accuracy : %s'%score)

if __name__=='__main__':
    # k-means
    # k=kmeans(datatrain,datatest)
    # k.test()
    # EM分类
    g=em(datatrain,datatest)
    g.test()



