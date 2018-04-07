from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz

# ��csv�ļ��ж�ȡ
allElectronicsData = open('../../datasource.csv', 'r')
reader = csv.reader(allElectronicsData)
header = next(reader)
  
print(header)
 
featureList = []
labelList = []
 
#��featrue��label���ָ�ʽ����ע����Ϊ������ù�һ��next������ѭ���ӵڶ��п�ʼ��
for row in reader:  
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[header[i]] = row[i]
    featureList.append(rowDict)
      
print(featureList)
 
#��feature���ֶ����������� 
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
  
print("dummyX:" + str(dummyX))
print(vec.get_feature_names())
  
print("labelList:" + str(labelList))

#��label���ֶ����������� 
lb = preprocessing.LabelBinarizer();
dummyY = lb.fit_transform(labelList);
print("dummyY:" + str(dummyY))

#���ɾ�����  
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf:" + str(clf))
  
#����dot�ļ�
with open("allElectronicInformationGainOri.dot",'w') as f:
    f = tree.export_graphviz(clf, feature_names = vec.get_feature_names(), out_file = f)

#����predict����Ԥ��  
oneRowX = dummyX[0, :]
print("oneRowX:" + str(oneRowX))
  
newRowX = oneRowX;
  
newRowX[0] = 1
newRowX[2] = 0
print("newRowX:" + str(newRowX))
  
predictedY = clf.predict(newRowX)
print("predictedY:" + str(predictedY))