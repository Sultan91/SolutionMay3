from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import svm


ds = pd.read_pickle("train_data.pkl")

feature = np.array(list(ds['feature']))
#print(feature)
labels = np.array(ds['class'])
train_features, test_features, train_labels, test_labels = train_test_split(feature, labels)
#clf = RandomForestClassifier(max_depth=10, random_state=42)
clf = svm.SVC(gamma=0.001, C=100.0)
clf.fit(train_features, train_labels)

for i, f in enumerate(test_features):
    print('Sentence prediction: ', clf.predict(f.reshape(1, -1)))
    print("Actual label: ", test_labels[i])
    print("------------------------------------")
