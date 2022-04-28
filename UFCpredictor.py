import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
dataset = pd.read_csv('D:/ufc.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
print('SPLITTED DATASET')
print(X_train)
print(y_train)
print(X_test)
print(y_test)
print('-------')
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print('SCALING')
#print(X_train)
#print(X_test)
print('-------')
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
#print('Predicting')
#print(classifier.predict(sc.transform([[883,3,0,0,0,10.5167]])))

print('Predicting the Test set results')

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
cm = confusion_matrix(y_test, y_pred)
print('Confusion Matrix')
print(cm)
print('ACCURACY SCORE:',accuracy_score(y_test, y_pred))
