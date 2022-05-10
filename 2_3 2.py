import pandas
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', size=10)



data = pandas.read_csv('/Users/evgeny/Desktop/INJ_FATL_SEX_MIG_RT_A.csv')



data=data[
    ['ref_area','indicator','sex','time','obs_value','classif1']
]
# print(data)

# data[data.sex == 'SEX_T'][
#     ['obs_value']].plot(title='Среднемесячная зарпалата в России по годам',kind='bar')





data_rus=data[data.ref_area == 'RUS']
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

data_new = pandas.read_csv('/Users/evgeny/Desktop/INJ_NFTL_SEX_MIG_RT_A.csv')


data_new = data_new[(data_new.sex=='SEX_T')&(data_new.ref_area=='UKR')][['ref_area', 'time', 'obs_value']]
data_new = data_new.set_index(['ref_area', 'time'])
# print(data_new)

data_1 = data[data.sex=='SEX_T'][['ref_area', 'time', 'obs_value']]
data_1 = data_1.rename(columns={'obs_value': 'died'})
data_1 = data_1.set_index(['ref_area', 'time'])
data_new= data_new.join(data_1, on=['ref_area', 'time'])

data_new.plot(logy=True,kind='bar',title='Смертельные исходы и трудовой травматизм')

data_new.plot(subplots=True,kind='bar',title='Смертельные исходы и трудовой травматизм')
# print(data_new)

data_new1 = pandas.read_csv('/Users/evgeny/Desktop/INJ_NFTL_SEX_MIG_RT_A.csv')




print(pivot)




plt.show()