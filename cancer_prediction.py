import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
df = pd.read_csv("cancer patient data sets.csv")
print(df.columns)
X = df.drop("Level", axis=1) 
y = df["Level"]               

plt.hist(X["Alcohol use"], bins=20)
plt.xlabel("Alcohol use")
plt.ylabel("Chances of Dieseas")
plt.title("Histogram of Alcohol use")
plt.show()

X = df[["Age", "Smoking","Alcohol use","Chest Pain","chronic Lung Disease"]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# cm = confusion_matrix(y_test, y_pred)
# print(cm)

# # age=40, smoking=1, alcohol=0
new_data = np.array([[20, 7, 7,8,4]])

result = model.predict(new_data)
print("newest_data:",result)  # 0 ya 1











