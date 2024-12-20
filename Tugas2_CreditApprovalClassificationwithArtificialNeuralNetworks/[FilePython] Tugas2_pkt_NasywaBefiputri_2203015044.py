# -*- coding: utf-8 -*-
"""PKT_Pertemuan10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TfmdvJs3CQw9JSIomuOmVBEXQLtCsVUO

#TUGAS 2 - Credit Approval Classification with Artificial Neural Networks
MK Pengantar Kecerdasan Tiruan

Nasywa Befiputri - 2203015044

#Import seluruh library yang di butuhkan
"""

import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

"""#import data frame"""

client_df = pd.read_csv('https://drive.google.com/uc?id=1_FXPTX8ap2LfgKKVF2zjShieopWDqHwL')
client_df.head()

"""#pilih fitur dan target"""

x = client_df.iloc[:, 3:-1].values
y = client_df.iloc[:, -1].values

"""#ubah atribut gender untuk menjadi nomerik
Male : 1
Female : 0
"""

le = LabelEncoder()

x[:, 2] = le.fit_transform(x[:, 2])

print(x)

"""#ubah  atribut Geography menjadi 3 kolom dan terletak di kolom 0 hingga 2

Frace = (1,0,0)
Germany = (0,1,0)
Spain = (0,0,1)
"""

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

print (x)

"""#split dataset jadi training dan testing"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

"""#Scaling atribut menggunakan Standard Scaler. Setelah itu tampilkan data setelah dilakukan scaling"""

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

print(x_train)

print(x_test)

"""# Proses Training dan Evaluasi menggunakan perhitungan accuracy."""

for nh in range (2,11):
  ann = MLPClassifier(hidden_layer_sizes=(nh,),max_iter=10000, random_state=1)
  ann.fit(x_train, y_train)
  acc = 100*ann.score(x_test,y_test)
  print('Neuron in hidden layer: %g, accuracy %.2f %%'  %(nh,acc))

"""# Gunakan model ANN dengan jumlah neuron dalam hidden layer berjumlah 3 dikarenakan memiliki akurasi yang terbaik untuk menentukan apakah nasabah di tolak atau diterima

##Anomali

###cek train shape untuk memastikan jumlah input input
"""

print(x_train.shape)

c= np.array([[600, 'France', 'Male', 40, 3, 60000, 2, 1, 1, 50000]])

c[:, 2] = le.transform(c[:, 2])
c = ct.transform(c)
c = sc.transform(c)
pred = ann.predict(c)

if (pred == 0):
    print('tolak')
else:
  print('terima')

"""ada ke anehan di output, di modul harusnya 'ditolak', dan kalo kita pertahatihan features itu ad 12, sedangkan ke tidak sesuai dengan data yang tersedia 10, kita cek lagi

##Improve, untuk memaksimalkan akurasi presiksi
"""

c= np.array([[600, 'France', 'Male', 40, 3, 60000, 2, 1, 1, 50000]])
if c.shape[1] == x_train.shape[1]:
    c[:, 2] = le.transform(c[:, 2])
    c = ct.transform
    c = sc.transform(c)
    pred = ann.predict(c)

    if (pred == 0):
        print('tolak')
    else:
      print('terima')
else:
  if (c.shape[1] == 0):
    print("Ditolak, tidak ada data terinput")
  elif (c.shape[1] < x_train.shape[1]):
    print("Ditolak karena data belum lengkap")
  elif (c.shape[1] > x_train.shape[1]):
    print("Ditolak karena data terlalu banyak")
  else:
    print("Ditolak karena data invalid")