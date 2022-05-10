import pandas
import matplotlib.pyplot as plt
import numpy as np



kef1=1.0006
kef2=0.1483
data_cpi = pandas.read_csv('/Users/evgeny/Desktop/2/CPI_NCYR_COI_RT_A.csv')
data = pandas.read_csv('/Users/evgeny/Desktop/2/CPI_NCYR_COI_RT_A.csv')
data1 = pandas.read_csv('/Users/evgeny/Desktop/2/RUSSIA-INF.csv')




# лаба 2.1.1
data_cpi=data_cpi[data_cpi.classif1=='COI_COICOP_CP01T12'][
    ['ref_area','time','obs_value']
]
# data_cpi=data_cpi[data_cpi.ref_area=='RUS']
# print(data_cpi)
data_cpi['time1']=data_cpi.time

data_cpi=data_cpi.set_index(['ref_area','time'])  

data_cpi['cpi_value']=data_cpi.obs_value+100

data_cpi['cpi_factor']=data_cpi.cpi_value/100

data_cpi_1997=data_cpi.loc[data_cpi.index.get_level_values(1) > 1996]
print(data_cpi[(data_cpi.time1==1997)]['cpi_factor'].min())
data_cpi_1997['cpi_factor_1996']=data_cpi_1997.sort_index().groupby(by=['ref_area'])['cpi_factor'].cumprod()*200/kef1

data_cpi_1997.loc['RUS'].sort_index()[[
    'cpi_factor_1996']].plot(title='Ружье и инфлянция', color='b',kind='barh' )


# лаба  2.1.2



data_cpi['cpi_value']=abs(data_cpi.obs_value-100)

data_cpi['cpi_factor']=data_cpi.cpi_value/100
data_cpi_1970=data_cpi.loc[data_cpi.index.get_level_values(1) <1997]
data_cpi_1970=data_cpi.loc[data_cpi.index.get_level_values(1) >1968]
data_cpi_1970=data_cpi_1970[data_cpi_1970.time1<1997]
data_cpi_1970['cpi_factor_1969']=data_cpi_1970.sort_index().groupby(by=['ref_area'])['cpi_factor'].cumprod()*1000000

(data_cpi_1970.loc['USA'].sort_index())[[
    'cpi_factor_1969']].plot(title='1000000 из 1969 в 1997 году',color='g',kind='barh' )




data_cpi_1998=data_cpi.loc[(data_cpi.index.get_level_values(1) <1998)]


data_cpi_1998['cpi_factor_1997']=data_cpi_1998.sort_index().groupby(by=['ref_area'])['cpi_factor'].cumprod()


print(data_cpi_1998.loc['USA'])
data_cpi_1998=data_cpi_1998[(data_cpi_1998.time1>1968)&(data_cpi_1998.time1<1999)]

data_cpi_1998['cpi_factor_1997']=data_cpi_1998.cpi_factor_1997*100000000000/kef2
data_cpi_1998.loc['USA'].sort_index()[[
    'cpi_factor_1997']].plot(title='100 млрд из 1997 года в 1969',  subplots=True,color='g',kind='barh')


data_cpi_1998=data_cpi.loc[data_cpi.index.get_level_values(1) >1997]

data_cpi_1998['cpi_factor_1997']=data_cpi_1998.sort_index().groupby(by=['ref_area'])['cpi_factor'].cumprod()*100000000000
data_cpi_1998.loc['USA'].sort_index()[[
    'cpi_factor_1997']].plot(title='100 млрд долларов из 1998 в 2020 году',color='g',kind='barh')




# лаба  2.2

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
data_rus.plot(title='Росстат vs lio',logy=True,color=['g','b'])
data_rus.plot(title='Росстат vs lio',logy=True,color=['g','b'],subplots=True)


plt.show() 

