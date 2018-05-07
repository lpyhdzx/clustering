##作业：
![image](https://note.youdao.com/yws/api/personal/file/7DA97FA40D4243FD89A8FD58F2555171?method=download&shareKey=44d38448d9b9e0187276e9e7ce74b3fb)<p>

####1.对数据集中的数字5和数字6使用2-均值聚类

kmeans train accuracy : 0.8114754098360656
kmeans test accuracy : 0.8333333333333334
####2.使用混合正态2-EM来计算聚类

GaussianMixture train accuracy: 0.8065573770491803
GaussianMixture test accuracy : 0.796969696969697
####3.使用阈值来重新聚类并比较效果

在data.py中使用newdata()对数据做阈值化处理，将数值中小于0.8的颜色统一归为-1，这么做相当于是对原始图像当中不是很亮的颜色直接归为黑色，对手写数字做了锐化处理。<p>
kmeans train accuracy : 0.8106557377049181<p>
kmeans test accuracy : 0.8333333333333334