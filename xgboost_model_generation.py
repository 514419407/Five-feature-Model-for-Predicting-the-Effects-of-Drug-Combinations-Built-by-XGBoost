import pandas as pd;import xgboost;from xgboost import plot_importance;from sklearn.linear_model import LogisticRegression ;from sklearn.naive_bayes import GaussianNB ;from sklearn.ensemble import RandomForestClassifier;from sklearn.cross_validation import train_test_split;from sklearn.cross_validation import StratifiedKFold  ;from sklearn.metrics import roc_curve, auc  ;from sklearn.metrics import accuracy_score;import numpy as np  ;from scipy import interp;import matplotlib.pyplot as plt 
dataset = pd.read_csv(r"Table S5_training.txt")
X = np.array(dataset[columns_name])
y = np.array(dataset['judge'])
model = XGBClassifier()
