# -*- coding:utf-8 -*-
import pandas as pd

class dataload():
    '''
    input: target: list[],'zip_train.csv'
    return: data(num,257) 返回全是target的向量
    '''
    def __init__(self,target=None,path=None):
        self.target=target
        self.path=path
    def loaddata(self):
        dataset=pd.read_csv(self.path)
        df=pd.DataFrame(dataset)
        index=self.target
        dfdata=df.iloc[:,1:][df['V1'].isin(index)]
        return dfdata

class newdata(dataload):
    '''
    :input:target:list[],zip_train.csv
    :return:阈值化处理data(num,257)
    '''
    def loaddata(self):
        dataset = pd.read_csv(self.path)
        df = pd.DataFrame(dataset)
        index = self.target
        dfdata = df.iloc[:, 1:][df['V1'].isin(index)]
        # 阈值化处理
        dfdata[dfdata < 0.8] = -1
        return dfdata

loader=dataload(target=[5,6],path='zip_train.csv')
datatrain=loader.loaddata()
loadertest=dataload(target=[5,6],path='zip_test.csv')
datatest=loadertest.loaddata()


if __name__=='__main__':
    print(datatrain)
