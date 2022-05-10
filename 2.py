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
data_rus=data_rus.set_index('time').sort_index()

# print(data_rus[data_rus.classif2=='CUR_TYPE_USD'])



ax = data_rus[data_rus.classif2 == 'CUR_TYPE_USD'][
    ['obs_value']].plot(title='Среднемесячная зарпалата в России по годам',kind='bar')

ax.legend(['Среднемесячная зарплата в usd'])
  
data_rus[['obs_value']].plot(title='Среднемесячная зарплата в России по годам',kind='bar')

pivot = data_rus.pivot_table(values='obs_value',
index='time',
columns='classif2') 
pivot.loc[
    pivot.index<=1996,'CUR_TYPE_LCU']/=1000

pivot.plot(title='Среднемесячная зарплата в россии по годам',kind='bar',logy=True,subplots=True)

data_cpi = pandas.read_csv('/Users/evgeny/Desktop/2/CPI_NCYR_COI_RT_A.csv')
# print( data_cpi.classi f1.value_counts() )  

data_cpi=data_cpi[data_cpi.classif1=='COI_COICOP_CP01T12'][
    ['ref_area','time','obs_value']
]
data_cpi=data_cpi.rename(columns={'obs_value': 'cpi_change'})

data_cpi=data_cpi.set_index(['ref_area','time'])  

# print(data_cpi.loc['RUS'])



data_cpi.loc['RUS'].sort_index()[['cpi_change']].plot(
    title='ИНфляция в россии по годам', kind='bar'
)
data=data.join(data_cpi,on=['ref_area','time']) 

data[
    (data.ref_area=='RUS') & 
    (data.classif2=='CUR_TYPE_LCU') &
    (data.time>1992)].set_index('time').sort_index()[
        ['obs_value','cpi_change']].plot(title='Зарплата vs инфляция по годам', kind='bar',subplots=True)


data_cpi['cpi_value']=data_cpi.cpi_change+100

data_cpi['cpi_factor']=data_cpi.cpi_value/100

# DataFrame.groupby()=>GroupBy.op_on_group()=>DataFrame
# data.group_by(by='ref_area').max()

# data.group_by(by='ref_area').max().reset_index()

data_cpi_1993=data_cpi.loc[data_cpi.index.get_level_values(1) > 1992]

data_cpi_1993['cpi_factor_1992']=data_cpi_1993.sort_index().groupby(by=['ref_area'])['cpi_factor'].cumprod()

# print(data_cpi_1993.loc[['RUS','USA']])
data_cpi_1993.loc['RUS'].sort_index()[[
    'cpi_factor', 
    'cpi_factor_1992']].plot(title='Ежегодная инфляция и инфляция по отношению к 1992 в россии', kind='bar', subplots=True)
data=data.drop(columns=['cpi_change'])
data=data.join(data_cpi_1993,on=['ref_area','time'])

data['wage_corr_cpi_1992']=data.obs_value/data.cpi_factor_1992

data_rus_lcu_1993 = data[
    ( data.ref_area == 'RUS') &
    (data.classif2 == 'CUR_TYPE_LCU') &
    (data.time >= 1993)
]
# print(data)
data_rus_lcu_1993.set_index('time').sort_index()[['obs_value', 'wage_corr_cpi_1992']].plot(title='Номинальная зарплата vs реальное содержание зарплаты в ценах 1992 в России (ILO)',
        kind='bar', subplots=True)

data_rus_lcu_1993.loc[
      data_rus_lcu_1993.time >= 1997,
      ['obs_value', 'wage_corr_cpi_1992']
] *= 1000
data_rus_lcu_1993.set_index('time').sort_index()[
    ['obs_value', 'wage_corr_cpi_1992']].plot(title='Номинальная зарплата vs реальное содержание зарплаты в ценах 1992 в России (ILO)', kind='bar', subplots=True)

data[ (data.ref_area == 'USA') & (data.classif2 == 'CUR_TYPE_LCU') &
(data.time > 1992) ].set_index('time').sort_index()[['obs_value',
'wage_corr_cpi_1992']].plot(title='Зарплата в ценах 1992 в США (ILO)',
kind='bar')
data[ (data.ref_area == 'CHN') & (data.classif2 == 'CUR_TYPE_LCU') &
(data.time > 1992) ].set_index('time').sort_index()[['obs_value',
'wage_corr_cpi_1992']].plot(title='Зарплата в ценах 1992 в КНР (ILO)',
kind='bar')

data_cpi['cpi_retro_factor'] = 1 / data_cpi.sort_index(ascending=False).groupby(by=['ref_area'])['cpi_factor'].shift(fill_value=1)
data_cpi_2019_retro = data_cpi.loc[data_cpi.index.get_level_values(1) <= 2019]
data_cpi_2019_retro.loc[
    data_cpi_2019_retro.index.get_level_values(1) == 2019,
    'cpi_retro_factor'] = 1
data_cpi_2019_retro['cpi_retro_factor_2019'] =data_cpi_2019_retro.sort_index(ascending=False).groupby(by=['ref_area'])['cpi_retro_factor'].cumprod()
data = data.join(
    data_cpi_2019_retro[['cpi_retro_factor', 'cpi_retro_factor_2019']],
    on=['ref_area', 'time'])
data['wage_corr_retro_cpi_2019'] =data.obs_value / data.cpi_retro_factor_2019


data[ (data.ref_area == 'RUS') & (data.classif2 == 'CUR_TYPE_LCU') &
(data.time > 1996) & (data.time <= 2019) ].set_index('time').sort_index()[
    ['obs_value', 'wage_corr_retro_cpi_2019']].plot(title='Зарплата в ценах 2019 в России (ILO)', kind='bar')
data[ (data.ref_area == 'USA') & (data.classif2 == 'CUR_TYPE_LCU') &
(data.time <= 2019) ].set_index('time').sort_index()[['obs_value',
'wage_corr_retro_cpi_2019']].plot(title='Зарплата в ценах 2019 в США (ILO)', kind='bar')
data[ (data.ref_area == 'CHN') & (data.classif2 == 'CUR_TYPE_LCU') &
(data.time <= 2019) ].set_index('time').sort_index()[['obs_value',
'wage_corr_retro_cpi_2019']].plot(title='Зарплата в ценах 2019 в КНР (ILO)', kind='bar')

plt.show() 