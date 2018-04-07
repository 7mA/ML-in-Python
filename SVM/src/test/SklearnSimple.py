from sklearn import svm
from numpy import *

X = [[1, 1], [2, 0], [0, 1.5], [2, 3], [3, 0]]
y = [0, 0, 0, 1, 0]
clf = svm.SVC(kernel = 'linear')
clf.fit(X, y)

print(str(clf))

print(str(clf.support_vectors_))

print(str(clf.support_))

print(str(clf.n_support_))

print(str(clf.predict(array([2, 0]).reshape(1, -1))))