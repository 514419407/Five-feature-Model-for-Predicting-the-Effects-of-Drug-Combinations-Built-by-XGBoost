import pandas as pd;import xgboost;from xgboost import plot_importance;from sklearn.linear_model import LogisticRegression ;from sklearn.naive_bayes import GaussianNB ;from sklearn.ensemble import RandomForestClassifier;from sklearn.cross_validation import train_test_split;from sklearn.cross_validation import StratifiedKFold  ;from sklearn.metrics import roc_curve, auc  ;from sklearn.metrics import accuracy_score;import numpy as np  ;from scipy import interp;import matplotlib.pyplot as plt 

X = np.array(dataset[columns_name])
y = np.array(dataset['judge'])
model = XGBClassifier()
accuracy=[]
for i in range(50):
	cv = StratifiedKFold(y, n_folds=6,shuffle=True)
	for j, (train, test) in enumerate(cv):
		model.fit(train_x, train_y)
		pred_y=model.predict(test_x)
		predictions = [round(value) for value in pred_y]
		accuracy.append(accuracy_score(test_y, predictions))

sum(accuracy)/250
