import numpy as np
import random
from numpy import gradient

def logistic(x):
    return 1/(1 + np.exp(-x))

def errin(x):
    return np.log(1 + np.exp(x))

def gradientDescent(x, y, theta, alpha, m, numIterations):
    for i in range(0, numIterations):
        err = 0
        for j in range(0, m):
            err += errin(-y[j] * np.dot(theta, x[j]))
        print("Iteration " + str(i) + "|" + "Err " + str(err))
        gradient = 0
        for j in range(0, m):
            gradient += logistic(-y[j] * np.dot(theta, x[j])) * (-y[j] * x[j])
        gradient /= m
        theta = theta - alpha * gradient
        print(theta)
    return theta

def genData(numPoints, bias, variance):
    x = np.zeros(shape = (numPoints, 2))
    y = np.zeros(shape = numPoints)
    for i in range(0, numPoints):
        x[i][0] = 1
        x[i][1] = i
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y

old_settings = np.seterr(over='ignore')
x, y = genData(100, 25, 10)
# print("x:")
# print(x)
# print("y:")
# print(y)
m, n = np.shape(x)
n_y = np.shape(y)

print("x shape:" + str(m) + " " + str(n))
print("y length:" + str(n_y)) 

numIterations = 10000
alpha = 0.00005
theta = [0, -1]
theta = gradientDescent(x, y, theta, alpha, m, numIterations)
print(theta)