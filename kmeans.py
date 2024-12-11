import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data=pd.read_csv('diabetes.csv')
x=data.iloc[:,:4]
print(x.head())
km=KMeans(n_clusters=3)
km.fit(x)
y=km.predict(x)
print(y)


