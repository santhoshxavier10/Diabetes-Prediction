# -*- coding: utf-8 -*-
"""ML_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15Uk5Cu1lio4k1lGNhfG6i1fpPtMg4iPa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv("C:\Users\santh\Downloads\diabetes\diabetes_binary_5050split_health_indicators_BRFSS2015.csv")

df.head()

diabetes_df = pd.read_csv("C:\Users\santh\Downloads\diabetes\diabetes_binary_5050split_health_indicators_BRFSS2015.csv")
diabetes_df.info()

print("Dataset Shape (Rows, Columns):", diabetes_df.shape)

diabetes_df.columns

diabetes_df.Diabetes_binary.unique()

diabetes_df.nunique()

diabetes_df.duplicated().sum()

diabetes_df.drop_duplicates(inplace = True)

diabetes_df.duplicated().sum()

diabetes_df.isnull().sum()

diabetes_df.describe()

plt.figure(figsize=(8, 4))
sns.countplot(x=df['GenHlth'])
plt.xticks(rotation=0)
plt.title("Distribution of General Health Ratings")
plt.xlabel("General Health (1 = Excellent, 5 = Poor)")
plt.ylabel("Count")
plt.show()
labels = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']

data1 = df['GenHlth'].value_counts().sort_index().values
explode = [0.1, 0, 0, 0, 0]
plt.figure(figsize=(6,6))
plt.pie(data1, labels=labels, explode=explode, radius=1.2,
        autopct='%0.2f%%', shadow=True, textprops={'fontsize': 10})
plt.legend(loc='center left', shadow=True, fancybox=True)
plt.title("Distribution of General Health Ratings")
plt.show()

df.dropna(subset=['HighBP'], inplace=True)
plt.figure(figsize=(6,4))
sns.countplot(x=df['HighBP'], hue=df['Diabetes_binary'])
plt.xticks(rotation=0)
plt.xlabel("High Blood Pressure (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.title("High Blood Pressure vs. Diabetes Status")
plt.legend(title="Diabetes (0 = No, 1 = Yes)")
plt.show()

label_for_income = ['Lowest', 'Low', 'Lower-Middle', 'Middle', 'Upper-Middle', 'High', 'Higher', 'Highest']

data2 = df['Income'].value_counts().sort_index().values
plt.figure(figsize=(6,6))
plt.pie(data2, labels=label_for_income, radius=1.2, autopct='%0.2f%%',
        shadow=True, textprops={'fontsize': 12})
plt.legend(loc='upper right', shadow=True, fancybox=True, prop={'size': 8})

plt.title("Income Distribution")
plt.show()

label_for_GenHlth = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']
data3 = df['GenHlth'].value_counts().sort_index().values
print(df['GenHlth'].value_counts())
print(data3)
plt.figure(figsize=(6,6))
plt.title('General Health Rating', bbox={'facecolor':'0.8', 'pad':5})
plt.pie(data3, labels=label_for_GenHlth, radius=1.4, autopct='%0.2f%%',
        shadow=True, textprops={'fontsize': 12})
plt.legend(loc='center', shadow=True, fancybox=True, prop={'size': 10})
plt.show()

gp_by_income = df.groupby('Income')[['BMI', 'PhysHlth']].mean().reset_index()

plt.rcParams['figure.figsize'] = (6,4)
gp_by_income.plot(x="Income", y=["BMI", "PhysHlth"], kind="bar")
plt.title("Average BMI & Physical Health Days by Income Level")
plt.xlabel("Income Level (1 = Lowest, 8 = Highest)")
plt.ylabel("Average Value")
plt.legend(["BMI", "PhysHlth"])
plt.xticks(rotation=0)
plt.show()

label_for_GenHlth = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']

# Data for the pie chart
data3 = df['GenHlth'].value_counts().sort_index().values
plt.figure(figsize=(6,6))
plt.title('General Health Rating', bbox={'facecolor':'0.8', 'pad':5})
plt.pie(data3, labels=label_for_GenHlth, radius=1.4, autopct='%0.2f%%',
        shadow=True, textprops={'fontsize': 12})
plt.legend(loc='center', shadow=True, fancybox=True, prop={'size': 10})
plt.show()

df.dropna(subset=['HighBP'], inplace=True)

# Countplot of High Blood Pressure by Diabetes Status
plt.figure(figsize=(6,4))
sns.countplot(x=df['HighBP'], hue=df['Diabetes_binary'])
plt.xlabel("High Blood Pressure (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.title("High Blood Pressure vs. Diabetes Status")
plt.legend(title="Diabetes (0 = No, 1 = Yes)")
plt.xticks(rotation=0)
plt.show()

# Labels for General Health categories
label_for_GenHlth = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']


data4 = df['GenHlth'].value_counts().sort_index().values


plt.figure(figsize=(6,6))
plt.title('General Health Rating', bbox={'facecolor':'0.8', 'pad':5})
plt.pie(data4, labels=label_for_GenHlth, radius=1.4, autopct='%0.2f%%',
        shadow=True, textprops={'fontsize': 12})


plt.legend(loc='center', shadow=True, fancybox=True, prop={'size': 10})
plt.show()

df.dropna(subset=['PhysActivity'], inplace=True)

# Countplot of Physical Activity by Diabetes Status
plt.figure(figsize=(6,4))
sns.countplot(x=df['PhysActivity'], hue=df['Diabetes_binary'])
plt.xlabel("Physical Activity (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.title("Physical Activity vs. Diabetes Status")
plt.legend(title="Diabetes (0 = No, 1 = Yes)")
plt.xticks(rotation=0)
plt.show()

# Labels for Physical Health categories
label_for_PhysHlth = ['0 Days', '1-5 Days', '6-10 Days', '11-20 Days', '21-30 Days']

df['PhysHlth_Cat'] = pd.cut(df['PhysHlth'], bins=[-1,0,5,10,20,30], labels=label_for_PhysHlth)


data5 = df['PhysHlth_Cat'].value_counts().sort_index().values


plt.figure(figsize=(6,6))
plt.title('Physical Health Ratings', bbox={'facecolor':'0.8', 'pad':5})
plt.pie(data5, labels=label_for_PhysHlth, radius=1.4, autopct='%0.2f%%',
        shadow=True, textprops={'fontsize': 12})


plt.legend(loc='center', shadow=True, fancybox=True, prop={'size': 10})
plt.show()

df.dropna(subset=['Education'], inplace=True)

# Countplot of Education Levels by Diabetes Status
plt.figure(figsize=(6,4))
sns.countplot(x=df['Education'], hue=df['Diabetes_binary'])
plt.xlabel("Education Level (1 = Lowest, 6 = Highest)")
plt.ylabel("Count")
plt.title("Education Level vs. Diabetes Status")
plt.legend(title="Diabetes (0 = No, 1 = Yes)")
plt.xticks(rotation=0)
plt.show()

# Labels for Income categories (assuming 1 = Lowest, 8 = Highest)
label_for_income = ['Lowest', 'Low', 'Lower-Middle', 'Middle', 'Upper-Middle', 'High', 'Higher', 'Highest']
data6 = df['Income'].value_counts().sort_index().values
plt.figure(figsize=(6,6))
plt.title('Income Level Distribution', bbox={'facecolor':'0.8', 'pad':5})
plt.pie(data6, labels=label_for_income, radius=1.4, autopct='%0.2f%%',
        shadow=True, textprops={'fontsize': 12})
plt.legend(loc='center', shadow=True, fancybox=True, prop={'size': 10})
plt.show()

label_for_GenHlth = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']

data7 = df['GenHlth'].value_counts().sort_index().values
print(df['GenHlth'].value_counts())
plt.figure(figsize=(6,6))
plt.title('General Health Rating', bbox={'facecolor':'0.8', 'pad':5})
plt.pie(data7, labels=label_for_GenHlth, radius=1.4, autopct='%0.2f%%',
        shadow=True, textprops={'fontsize': 12})
plt.legend(loc='center', shadow=True, fancybox=True, prop={'size': 10})
plt.show()

df = pd.read_csv("C:\Users\santh\Downloads\diabetes\diabetes_binary_5050split_health_indicators_BRFSS2015.csv")
if "Diabetes_binary" not in df.columns:
    print("Column 'Diabetes_binary' is missing. Please check your dataset.")
else:
    print("Column 'Diabetes_binary' found. Proceeding...")
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
if "Diabetes_binary" in numerical_columns:
    numerical_columns.remove("Diabetes_binary")
def remove_outliers_iqr(df, column):
    """Removes outliers from a specified column using the IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
for column in numerical_columns:
    df = remove_outliers_iqr(df, column)
X = df.drop(columns=["Diabetes_binary"])
y = df["Diabetes_binary"]
print("\n Outliers removed. Cleaned dataset info:")
print(df.info())
print("\n Sample cleaned data:")
print(df.head())
cleaned_filename = "cleaned_diabetes_data.csv"
df.to_csv(cleaned_filename, index=False)
print(f"\n Cleaned dataset saved as '{cleaned_filename}'")

df = pd.read_csv("C:\Users\santh\Downloads\diabetes\diabetes_binary_5050split_health_indicators_BRFSS2015.csv")
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

if "Diabetes_binary" in numerical_columns:
    numerical_columns.remove("Diabetes_binary")
def remove_outliers_iqr(df, column):
    """Removes outliers from a specified column using the IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
for column in numerical_columns:
    df = remove_outliers_iqr(df, column)


def plot_boxplots(df, numerical_columns):
    plt.figure(figsize=(12, 10))
    for i, column in enumerate(numerical_columns, 1):
        plt.subplot((len(numerical_columns) + 1) // 2, 2, i)
        plt.boxplot(
            df[column],
            vert=False,
            patch_artist=True,
            showmeans=True,
            boxprops=dict(facecolor="lightblue", color="blue"),
            whiskerprops=dict(color="blue"),
            capprops=dict(color="blue"),
            flierprops=dict(markerfacecolor="red", marker="o", markersize=5),
            meanprops=dict(markerfacecolor="green", marker="D", markersize=7)
        )
        plt.title(f'Boxplot for {column}', fontsize=12)
        plt.xlabel(column, fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
plot_boxplots(df, numerical_columns)

X = df.drop(columns=['Diabetes_binary'])
y = df['Diabetes_binary']

from sklearn.preprocessing import LabelEncoder
categorical_columns = X.select_dtypes(include=['object']).columns
if len(categorical_columns) > 0:
    le = LabelEncoder()
    for col in categorical_columns:
        X.loc[:, col] = le.fit_transform(X[col].astype(str))
print(f"Encoded {len(categorical_columns)} categorical columns: {list(categorical_columns)}")

X.fillna(0, inplace=True)

y = df['Diabetes_binary']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print("Shape of Features (X):", X.shape)
print("Shape of Target (y):", y.shape)
print("Shape of Training Features (X_train):", X_train.shape)
print("Shape of Testing Features (X_test):", X_test.shape)
print("Shape of Training Labels (y_train):", y_train.shape)
print("Shape of Testing Labels (y_test):", y_test.shape)

!pip install xgboost

from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report


# Scale the training data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Scale the test data using the same scaler
X_test_scaled = scaler.transform(X_test)

# Train an XGBoost model
xgb_model = XGBClassifier(n_estimators=200, learning_rate=0.1, max_depth=6, random_state=42)
xgb_model.fit(X_train_scaled, y_train)
y_pred_xgb = xgb_model.predict(X_test_scaled)
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
report_xgb = classification_report(y_test, y_pred_xgb)
print(f"XGBoost Accuracy: {accuracy_xgb * 100:.2f}%")
print("Classification Report:\n", report_xgb)

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler # Import StandardScaler

# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the training data and transform it
X_train_scaled = scaler.fit_transform(X_train)

# Transform the test data using the fitted scaler
X_test_scaled = scaler.transform(X_test)

# Now you can proceed with model training
log_class = LogisticRegression(max_iter=2000, solver='saga', class_weight='balanced', random_state=42)
log_class.fit(X_train_scaled, y_train)
y_pred = log_class.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Balanced Logistic Regression Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", report)

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
param_grid = {
    'C': [0.01, 0.1, 1, 10],
    'solver': ['saga'],
    'class_weight': ['balanced', None]
}
log_class = GridSearchCV(LogisticRegression(max_iter=2000, random_state=42), param_grid, cv=5, scoring='accuracy')
log_class.fit(X_train_scaled, y_train)
best_model = log_class.best_estimator_
y_pred = best_model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Improved Accuracy: {accuracy * 100:.2f}%")
print("Best Parameters:", log_class.best_params_)
print("Classification Report:\n", report)

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'solver': ['saga'],
    'class_weight': ['balanced', None]
}


log_class = GridSearchCV(LogisticRegression(max_iter=2000, random_state=42), param_grid, cv=5, scoring='accuracy')
log_class.fit(X_train_scaled, y_train)

best_model = log_class.best_estimator_
y_pred = best_model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Optimized Accuracy: {accuracy * 100:.2f}%")
print("Best Parameters:", log_class.best_params_)
print("Classification Report:\n", report)