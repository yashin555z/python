import pandas
import matplotlib.pyplot as plt
import numpy as np


plt.rc('font', size=10)

data = pandas.read_csv('/Users/evgeny/Desktop/lb3/EAR_4MTH_SEX_ECO_CUR_NB_A.csv')
data = data[
    (data.ref_area != 'BLR') & (data.ref_area != 'ZWE')
]
data = data[
    ['ref_area','sex','classif1','classif2', 'time','obs_value']
]
data = data[
    (data.classif1== 'ECO_AGGREGATE_TOTAL')&(data.sex=='SEX_T')]

# data[
#     (data.ref_area=='RUS')&(data.classif2=='CUR_TYPE_USD')] [
#         ['time', 'obs_value']].plot(kind='bar')

data_rus=data[data.ref_area == 'RUS']
# data_rus['kurs']=(data.obs_value[data.classif2=='CUR_TYPE_LCU'])

data_rus=data_rus.set_index('time').sort_index()

n= data[(data.time==1997)&(data.classif2 == 'CUR_TYPE_USD')&(data.ref_area == 'RUS')].obs_value.mean()

data_rus['obs_value']=data_rus.obs_value*200/n

ax = data_rus[data_rus.classif2 == 'CUR_TYPE_USD'][
    ['obs_value']].plot(title='Цена ружья исходя из зарплаты',kind='bar')


ax.legend(['Средняя цена ружья в $'])




data_cpi = pandas.read_csv('/Users/evgeny/Desktop/2/CPI_NCYR_COI_RT_A.csv')


data_cpi=data_cpi[data_cpi.classif1=='COI_COICOP_CP01T12'][
    ['ref_area','time','obs_value']
]
print(data_cpi)
data_cpi['time1']=data_cpi.time
data_cpi['ref']=data_cpi.ref_area
data_cpi=data_cpi.rename(columns={'obs_value': 'cpi_change'})

data_cpi=data_cpi.set_index(['ref_area','time'])  


data=data.join(data_cpi,on=['ref_area','time']) 


data_cpi['cpi_value']=data_cpi.cpi_change+100


data_cpi['cpi_factor']=data_cpi.cpi_value/100
# print(data_cpi)

data_cpi_1997=data_cpi.loc[data_cpi.index.get_level_values(1) > 1996]

n1= data_cpi[(data_cpi.ref=='RUS')&(data_cpi.time1==1997)].cpi_factor.mean()
# print(n1)
data_cpi_1997['cpi_factor_1996']=data_cpi_1997.sort_index().groupby(by=['ref_area'])['cpi_factor'].cumprod()*200/n1


data_cpi_1997.loc['RUS'].sort_index()[[
    'cpi_factor_1996']].plot(title='цена ружья относительно инфляции', kind='bar', subplots=True)

plt.show() 