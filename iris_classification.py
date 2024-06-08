# -*- coding: utf-8 -*-
"""IRIS CLASSIFICATION

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JZ1PpgvpgmIZf2iuw2oM8XOcIVhkpHew
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('iris.csv')
df

df.describe()

df.shape

df.columns

df.rename(columns = {'sepal.length':'0','sepal.width':'1','petal.length':'2','petal.width':'3','variety':'4'}, inplace = True)

df.columns=['0','1','2','3','4']

df.columns

df

"""IDENTIFYING INDEPENDENT AND DEPENDENT FEATURES"""

print(df['4'].value_counts())

X=df.iloc[:,:4]
Y=df.iloc[:,4]
print("X:\n---------------------\n{}".format(X))
print("Y:\n---------------------\n{}".format(Y))

"""SPLITTING TRAINING AND TESTING DATASET"""

from pandas.core.common import random_state
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=0)

print("X_train :\n{}".format(X_train))
print("X_train Shape:{}".format(X_train.shape))

print("X_test :\n{}".format(X_test))
print("X_test Shape:{}".format(X_test.shape))

print("Y_train :\n{}".format(Y_train))
print("Y_train Shape:{}".format(Y_train.shape))

print("Y_test :\n{}".format(Y_test))
print("Y_test Shape:{}".format(Y_test.shape))

"""APPLYING THT MODEL

FITTING KNN MODEL TO THE DATA SET
"""

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,Y_train)
Y_pred=knn.predict(X_test)

print("Y_pred:\n------------------------\n{}".format(Y_pred))

print("Y_test:\n------------------------\n{}".format(Y_test))

"""CONFUSION MATRIX"""

from sklearn.metrics import accuracy_score,confusion_matrix
print(confusion_matrix(Y_test,Y_pred))
accuracy=accuracy_score(Y_test,Y_pred)*100
print("Accuracy of the model is {:.2f}".format(accuracy))

"""NEW FEATURE"""

X_new=np.array([[2.3,2.9,5.0,1.9]])
print("X_new.shape: {}".format(X_new.shape))

Y_new=knn.predict(X_new)

print("Prediction : {}".format(Y_new))
print("Predicted Target Name : {}".format(Y_new))