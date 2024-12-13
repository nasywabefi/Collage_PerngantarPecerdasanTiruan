# -*- coding: utf-8 -*-
"""Modul1_PengantarAI_NasywaBefiputri_2203015044.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11d_K8mtimBSicTlxtGbAor5iluVyl31t

#Tugas Pengantar Kecerdasan tiruan 5A - Modul 1
Nasywa Befiputri (2203015044)

## Import Library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

"""##import data set ke data frame df_boston"""

url = "https://raw.githubusercontent.com/nasywabefi/HomePriceRegresion_Modul1/main/HousingData.csv"
df_boston = pd.read_csv(url, encoding='ISO-8859-1')
df_boston.head()

"""##cek semua info yang ada di df_boston"""

df_boston.info()

""" ## memilih features (input) dan target (output)"""

# Pilih fitur dan target
features = ["DIS", "NOX", "RM", "TAX"]  # Lokasi, lingkungan, rumah, pajak
target = "MEDV"

X = df_boston[features]
y = df_boston[target]

"""## train dan test set"""

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.4, random_state=1)

#print ukuran set
print(xtrain.shape)
print(xtest.shape)
print(ytrain.shape)
print(ytest.shape)

"""## pastikan fitur input berada dalam rentang yang sama"""

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""## melatih model regresi linier"""

lr = LinearRegression()
lr.fit(xtrain, ytrain)

"""##mencetak nilai intercept (konstanta)"""

print ('constant term :', lr.intercept_)
print ('coefficient :', lr.coef_)

"""##menghitung dan menilai kinerja model regresi linier"""

ypred=lr.predict(xtest)
mse=mean_squared_error(ytest,ypred)
r2=lr.score(xtest,ytest)
print ('mse :', mse)
print ('r2 :', r2)

"""## menunjukkan perbandingan antara nilai target yang sebenarnya dan nilai prediksi yang dihasilkan oleh model"""

plt.figure()
plt.scatter(ytest,ypred)
plt.xlabel('Target Output')
plt.ylabel('Prediksi target')
plt.show()