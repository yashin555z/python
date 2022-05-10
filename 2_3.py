import pandas
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', size=10)



data = pandas.read_csv('/Users/evgeny/Desktop/sndkv/INJ_FATL_SEX_MIG_RT_A.csv')



data=data[
    ['ref_area','indicator','sex','time','obs_value','classif1']
]
# print(data)

# data[data.sex == 'SEX_T'][
#     ['obs_value']].plot(title='Среднемесячная зарпалата в России по годам',kind='bar')





data_rus=data[(data.ref_area == 'RUS')&(data.time>=1990)]
data_rus=data_rus.set_index('time').sort_index()
data_rus[data_rus.sex == 'SEX_T'][
    ['obs_value']].plot(title='Количество смертельных исходов в России')

# print(data_rus)

pivot = data_rus.pivot_table(values='obs_value',
index='time',
columns='sex'
) 

pivot.plot(title='Количество смертельных исходов в России для разных полов')

pivot.loc[pivot.index>=1995].plot(title='Количество смертельных исходов в России для разных полов c 1995 года',subplots=True, kind='bar')

data_new = pandas.read_csv('/Users/evgeny/Desktop/sndkv/INJ_NFTL_SEX_MIG_RT_A.csv')


data_new = data_new[(data_new.sex=='SEX_T')&(data_new.ref_area=='RUS')&(data_new.time<2009)][['ref_area', 'time', 'obs_value']]
data_new = data_new.set_index(['ref_area', 'time'])
data_new= data_new.rename(columns={'obs_value': 'alive'})
# print(data_new)

data_1 = data[(data.sex=='SEX_T')][['ref_area', 'time', 'obs_value']]
data_1 = data_1.rename(columns={'obs_value': 'died'})
data_1 = data_1.set_index(['ref_area', 'time'])
data_new= data_new.join(data_1, on=['ref_area', 'time'])

data_new.plot(logy=True,kind='bar',title='Смертельные исходы и трудовой травматизм в России')

data_new.plot(subplots=True,kind='bar',title='Смертельные исходы и трудовой травматизм в России')



data_new1 = pandas.read_csv('/Users/evgeny/Desktop/sndkv/INJ_NFTL_SEX_MIG_RT_A.csv')
data_new1 = data_new1[(data_new1.ref_area=='RUS')&(data_new1.time>=1990)&(data_new1.time<2009)&(data_new1.sex!='SEX_T')][['ref_area', 'time', 'obs_value','sex']]
data_new1 = data_new1.rename(columns={'obs_value': 'alive'})

data_2 = data[['ref_area', 'time', 'obs_value']]
data_2 = data_2.rename(columns={'obs_value': 'died'})
data_2 = data_2.set_index(['ref_area', 'time'])
data_new1= data_new1.join(data_2, on=['ref_area', 'time'])

data_new1_pivot=data_new1.pivot_table(values=['alive','died'],
index='time',
columns='sex'
) 



print(data_new1_pivot)

data_new1_pivot.plot(subplots=True, title='Смертельные исходы и трудовой трвматизм в России с разбиением по полу')
data_new1_pivot.plot(logy=True,kind='bar', title='Смертельные исходы и трудовой трвматизм в России с разбиением по полу')

plt.show()