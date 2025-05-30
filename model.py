# -*- coding: utf-8 -*-
"""UTS Praktikum Machine Learning_1227050131_Syifa Arifah Nurbayani .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NiJ-UIUQ3QSiGpWKpD5MOzFx4360zuMd

Import library
"""

# %%
# Loading library
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files

"""Load dataset"""

uploaded = files.upload()

df = pd.read_csv('dataset_buys _comp.csv')
df.head()

print("Informasi Dataset")
df.info()

"""2. Melakukan pembagian data (Training dan Testing)

pemisahan fitur dan target
"""

X = df[['Age', 'Income', 'Student', 'Credit_Rating']]
y = df['Buys_Computer']

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
for col in X.columns:
    X[col] = le.fit_transform(X[col])

"""Split Dataset"""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

"""4. Membuat Model Klasifikasi"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Buat dan latih model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(x_train, y_train)

# Lakukan prediksi
y_pred = model.predict(x_test)

"""3. Membuat Report Hasil Klasifikasi"""

print("Akurasi Model:")
print(accuracy_score(y_test, y_pred))

print("\nLaporan Klasifikasi:")
print(classification_report(y_test, y_pred))

"""4. Melakukan Evaluasi"""

#%%
# Confusion matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()

"""5. Menampilkan visualisasi Tree (Decision Tree)"""

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(16, 10))
plot_tree(model, feature_names=X.columns, class_names=le.classes_, filled=True)
plt.show()

"""6. Ujicoba data diluar Data Testing"""

# Contoh prediksi satu data baru
sample = pd.DataFrame([{
    'Age': 'Paruh Baya',
    'Income': 'Sedang',
    'Student': 'Tidak',
    'Credit_Rating': 'Buruk'
}])

for col in sample.columns:
    sample[col] = le.fit_transform(sample[col])

# Prediksi
prediction = model.predict(sample)
print("Prediksi (0 = Tidak Beli, 1 = Beli):", prediction[0])