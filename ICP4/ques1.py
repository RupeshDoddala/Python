import numpy as np
import pandas as pd
from matplotlib import pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
iris= pd.read_csv('iris.csv')
X_train,X_test = train_test_split(iris,test_size=0.2)
X_train1=X_train
X_train1=X_train1.drop(['class'],axis=1)
clf=GaussianNB()
clf.fit(X_train1,X_train['class'])
X_test1=X_test
X_test1=X_test1.drop(['class'],axis=1)
predicted=clf.predict(X_test1)
print("train accuracy",clf.score(X_train1,X_train['class']))
print("test accuracy",clf.score(X_test1,X_test['class']))
