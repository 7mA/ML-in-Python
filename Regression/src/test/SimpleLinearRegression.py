import numpy as np

def fitSLR(x, y):
    n = len(x)
    denominator = 0
    numerator = 0
    for i in range(0, n):
        numerator += (x[i] - np.mean(x)) * (y[i] - np.mean(y))
        denominator += (x[i] - np.mean(x)) ** 2
    
    print("numerator:" + str(numerator))
    print("denominator:" + str(denominator))
    b1 = numerator / float(denominator)
    b0 = np.mean(y) - float(np.mean(x)) * b1
    
    return b0, b1

def predict(x, b0, b1):
    return b0 + x * b1

x = [1, 3, 2, 1 ,3]
y = [14, 24, 18, 17, 27]

b0, b1 = fitSLR(x, y)

print("intercept:" + str(b0) + " slope:" + str(b1))

x_test = 6

y_test = predict(6, b0, b1)

print("y_test:" + str(y_test))