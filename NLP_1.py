""" @author: NIHARIKA PENTAPATI
    @id: PES1201700215"""

from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/telemonitoring/parkinsons_updrs.data'
df = pd.read_csv(filename)
shape = df.shape
print("Before deletion:",shape)
del df['motor_UPDRS']
shape = df.shape
print("After deletion:",shape)
df.boxplot()
df.hist()
df = df.values
mean = np.mean(df, axis=0)
total = np.sum(df, axis=0)
min = np.min(df,axis=0)
max = np.max(df,axis=0)

print("Mean of each column:",mean)
print("Total of each column:",total)
print("Minimum of each column:",min)
print("Maximum of each column:",max)
