from matplotlib import colors
import pandas
import matplotlib.pyplot as plt
import numpy as np

data = pandas.read_csv('/Users/evgeny/Desktop/2/CPI_NCYR_COI_RT_A.csv')
data1 = pandas.read_csv('/Users/evgeny/Desktop/2/RUSSIA-INF.csv')
data=data[data.classif1=='COI_COICOP_CP01T12']
data = data[
    ['ref_area', 'time','obs_value']
]



data_rus = data[(data.ref_area=='RUS')]


print(data1)

data1.obs_value1=data1.obs_value1-100
data_rus = data_rus.set_index(['time'])
data1 = data1.set_index(['time'])



data_rus= data_rus.join(data1, on=['time'])
data_rus = data_rus.rename(columns={'obs_value': 'ILO', 'obs_value1':'ROSSTAT'})

data_rus.plot(color=['plum','olive'])

data_rus.plot(kind='bar',logy=True,color=['plum','olive'])
print(data_rus)

data_rus.plot(kind='bar',logy=True,subplots=True,color=['plum','olive'])


plt.show()