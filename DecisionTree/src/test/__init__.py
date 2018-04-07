from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz

# 从csv文件中读取
allElectronicsData = open('../../datasource.csv', 'r')
reader = csv.reader(allElectronicsData)
header = next(reader)
  
print(header)
 
featureList = []
labelList = []
 
#将featrue和label部分格式化，注意因为上面调用过一次next，所以循环从第二行开始。
for row in reader:  
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[header[i]] = row[i]
    featureList.append(rowDict)
      
print(featureList)
 
#将feature部分二进制向量化 
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
  
print("dummyX:" + str(dummyX))
print(vec.get_feature_names())
  
print("labelList:" + str(labelList))

#将label部分二进制向量化 
lb = preprocessing.LabelBinarizer();
dummyY = lb.fit_transform(labelList);
print("dummyY:" + str(dummyY))

#生成决策树  
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf:" + str(clf))
  
#生成dot文件
with open("allElectronicInformationGainOri.dot",'w') as f:
    f = tree.export_graphviz(clf, feature_names = vec.get_feature_names(), out_file = f)

#调用predict函数预测  
oneRowX = dummyX[0, :]
print("oneRowX:" + str(oneRowX))
  
newRowX = oneRowX;
  
newRowX[0] = 1
newRowX[2] = 0
print("newRowX:" + str(newRowX))
  
predictedY = clf.predict(newRowX)
print("predictedY:" + str(predictedY))