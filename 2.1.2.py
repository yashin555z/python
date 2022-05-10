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

data['time1']=data.time

data_usa1=data[(data.ref_area == 'USA')&(data.time<=1997)]


data_usa1=data_usa1.set_index('time').sort_index()


n= data_usa1[data_usa1.time1==1969].obs_value.mean()



data_usa1['obs_value']=(1000000/data_usa1['obs_value'])*n

ax = data_usa1[data_usa1.classif2 == 'CUR_TYPE_USD'][
    ['obs_value']].plot(title='Миллион из 1969 года до 1997 года',kind='bar',color='k')

ax.legend(['Миллион из 1969 года'])
  


data_cpi = pandas.read_csv('/Users/evgeny/Desktop/2/inflation_usa.csv')
# print(data_cpi)
data_cpi=data_cpi[data_cpi.classif1=='COI_COICOP_CP01T12'][
    ['time','obs_value','ref_area',]
]


data_cpi=data_cpi.rename(columns={'obs_value': 'cpi_change'})
data_cpi=data_cpi.set_index(['ref_area','time'])  
data=data.join(data_cpi,on=['ref_area','time']) 


data_cpi['cpi_value']=abs(data_cpi.cpi_change-100)

data_cpi['cpi_factor']=data_cpi.cpi_value/100



data_cpi_1970=data_cpi.loc[data_cpi.index.get_level_values(1) <1998]

data_cpi_1970['cpi_factor_1969']=data_cpi_1970.sort_index().groupby(by=['ref_area'])['cpi_factor'].cumprod()*1000000


data_cpi_1970.loc['USA'].sort_index()[[
    'cpi_factor_1969']].plot(title='Миллион $ из 1969', kind='bar', subplots=True,color='indigo')



#2_часть лабы

data_usa2=data[(data.ref_area == 'USA')&(data.time<=1997)]


data_usa2=data_usa2.set_index('time').sort_index()

# print(data_cpi)
n1= data_usa2[data_usa2.time1==1997].obs_value.mean()
# print(n)
data_usa2['obs_value']=(100000000000/data_usa2['obs_value'])*n1

ax = data_usa2[data_usa2.classif2 == 'CUR_TYPE_USD'][
    ['obs_value']].plot(title='100 миллиардов из 1997 исходя из зарплат',kind='bar',color='k')

ax.legend(['100 Миллиардов'])



data_cpi_1998=data_cpi.loc[data_cpi.index.get_level_values(1) <1998]

data_cpi_1998['cpi_factor_1997']=data_cpi_1998.sort_index().groupby(by=['ref_area'])['cpi_factor'].cumprod()
# print(data_cpi_1998)
n2=data_cpi_1998[data_cpi_1998.cpi_change==1.70].cpi_factor_1997.mean()
data_cpi_1998['cpi_factor_1997']=data_cpi_1998.cpi_factor_1997*100000000000/n2
data_cpi_1998.loc['USA'].sort_index()[[
    'cpi_factor_1997']].plot(title='100 миллиардов исходя из инфляции', kind='bar', subplots=True,color='indigo')




#  3 часть лабы

data_usa3=data[(data.ref_area == 'USA')&(data.time>=1997)]


data_usa3=data_usa3.set_index('time').sort_index()

# print(data_usa3)
data_usa3['obs_value']=(100000000000/data_usa3['obs_value'])*n1  


ax = data_usa3[data_usa3.classif2 == 'CUR_TYPE_USD'][
    ['obs_value']].plot(title='100 Миллиардов из 1997 года в 2020',kind='bar',color='k')

ax.legend(['100 Миллиардов'])


data_cpi_1998=data_cpi.loc[data_cpi.index.get_level_values(1) >1996]

data_cpi_1998['cpi_factor_1997']=data_cpi_1998.sort_index().groupby(by=['ref_area'])['cpi_factor'].cumprod()*100000000000


data_cpi_1998.loc['USA'].sort_index()[[
    'cpi_factor_1997']].plot(title='100 Миллиардов $ из 1998', kind='bar', subplots=True,color='indigo')




data_usa4=data[(data.ref_area == 'USA')&(data.time<=2021)]
data_usa4=data_usa4.set_index('time').sort_index()


data_usa4['obs_value']=(1000000/data_usa4['obs_value'])*n

ax = data_usa4[data_usa4.classif2 == 'CUR_TYPE_USD'][
    ['obs_value']].plot(title='Миллион из 1969 года до 2020 года',kind='bar',color='k')

ax.legend(['Миллион из 1969 года'])





plt.show() 