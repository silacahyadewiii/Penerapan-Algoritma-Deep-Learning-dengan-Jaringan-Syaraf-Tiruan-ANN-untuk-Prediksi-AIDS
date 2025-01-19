# Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from imblearn.over_sampling import SMOTE

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import streamlit as st

@st.cache()
def load_data():
    #load dataset
    aids_df = pd.read_csv('AIDS_Classification.csv')

    x = aids_df[["time", "trt" "age", "wtkg", "hemo", "homo", "drugs", "karnof",
                 "oprior", "z30", "preanti", "race","gender", "str2", "strat", "symptom",
                 "treat", "offtrt", "cd40", "cd420", "cd80", "cd820"]]
    y = aids_df[['infected']]

    return aids_df, x, y

@st.cache()
def train_model(x,y):
    model = Sequential()
    model.add(Dense(64, activation='relu', input_dim=X_train.shape[1]))
    model.add(Dropout(0.3))  # Regularisasi untuk mencegah overfitting
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(1, activation='sigmoid'))  # Output untuk klasifikasi biner
    
    model.fit(x,y)

    score = model.score(x,y)

    return model, score

def predict(x,y, features):
    model, score = train_model(x,y)

    prediction = model.predict(np.array(features).reshape(1,-1))

    return prediction, score

