import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv',usecols=['Age','Fare','Survived'])

print(df.head())

df.isnull().mean() * 100

X = df.drop(columns=['Survived'])
y = df['Survived']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

print(X_train)

X_train['Age_imputed'] = X_train['Age']
X_test['Age_imputed'] = X_test['Age']

print(X_test.tail())

X_train.loc[X_train['Age_imputed'].isnull(), 'Age_imputed'] = \
    X_train['Age'].dropna().sample(
        X_train['Age'].isnull().sum(), random_state=2
    ).values

X_test.loc[X_test['Age_imputed'].isnull(), 'Age_imputed'] = \
    X_train['Age'].dropna().sample(
        X_test['Age'].isnull().sum(), random_state=2
    ).values

print(X_train['Age'].dropna().sample(X_train['Age'].isnull().sum()).values)

print(X_train['Age'].isnull().sum())

print(X_train)

print('Original variable variance: ', X_train['Age'].var())
print('Variance after random imputation: ', X_train['Age_imputed'].var())


# sampled_value = X_train['Age'].dropna().sample(1, random_state=int(observation['Fare']))