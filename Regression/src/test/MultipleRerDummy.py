from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model

dataPath = r"D:\Machine Learning\python\Regression\src\test\Delivery.csv"
deliveryData = genfromtxt(dataPath, delimiter=',')

print("data")
print(str(deliveryData))

X = deliveryData[:, :-1]
Y = deliveryData[:, -1]

print("X:")
print(str(X))
print("Y:")
print(str(Y))
 
regr = linear_model.LinearRegression()
  
regr.fit(X, Y)
  
print("coefficients")
print(str(regr.coef_))
print("intercept:")
print(str(regr.intercept_))
 
# xPred = [[102, 6]]
# yPred = regr.predict(xPred)
# print("predicted y:")
# print(str(yPred))