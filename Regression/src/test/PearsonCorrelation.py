import numpy as np
from astropy.units import Ybarn
import math

def computeCorrelation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR = 0
    varX = 0
    varY = 0
    for i in range(0, len(X)):
        diffXXbar = X[i] - xBar
        diffYYbar = Y[i] - yBar
        SSR += (diffXXbar * diffYYbar)
        varX += diffXXbar ** 2
        varY += diffYYbar ** 2
    
    SST = math.sqrt(varX * varY)
    return SSR / SST

def polyfit(x, y, degree):
    results = {}
    
    coeffs = np.polyfit(x, y, degree)
    
    results['polynomial'] = coeffs.tolist()
    
    p = np.poly1d(coeffs)
    
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat - ybar) ** 2)
    print("ssreg:" + str(ssreg))
    sstot = np.sum((y - ybar) ** 2)
    print("sstot:" + str(sstot))
    results['determination'] = ssreg / sstot
    
    print("results:" + str(results))
    return results

testX = [1, 3, 8, 7, 9]
testY = [10, 12, 24, 21, 34]

print("r:" + str(computeCorrelation(testX, testY)))
print("r^2:" + str(computeCorrelation(testX, testY) ** 2))
print(str(polyfit(testX, testY, 1)['determination']))