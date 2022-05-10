import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data20 = pd.read_csv('/Users/evgeny/Downloads/archive/2020.csv')
data20=data20[
    ['Country name','Score','Explained by: Perceptions of corruption','Explained by: Generosity','Explained by: Freedom to make life choices','Explained by: Log GDP per capita','Social support','Explained by: Healthy life expectancy']]
data20= data20.rename(columns={'Explained by: Perceptions of corruption': 'corruption',
'Explained by: Generosity':'Generosity',
'Explained by: Freedom to make life choices':'Freedom',
'Country name':'Country',
'Explained by: Log GDP per capita':'economy',
'Explained by: Healthy life expectancy':'Healthy'})

data20['year']=2020
data20=data20.set_index('year').sort_index()


data19 = pd.read_csv('/Users/evgeny/Downloads/archive/2019.csv')
data19= data19.rename(columns={
    'Country or region':'Country',
    'GDP per capita':'economy',
    'Healthy life expectancy':'Healthy',
    'Freedom to make life choices':'Freedom',
    'Perceptions of corruption':'corruption'

})
data19['year']=2019
data19=data19.set_index('year').sort_index()



data18 = pd.read_csv('/Users/evgeny/Downloads/archive/2018.csv')
data18= data18.rename(columns={
    'Country or region':'Country',
    'GDP per capita':'economy',
    'Healthy life expectancy':'Healthy',
    'Freedom to make life choices':'Freedom',
    'Perceptions of corruption':'corruption'

})
data18['year']=2018
data18=data18.set_index('year').sort_index()
# data20=data20.join(data19,on=['year'])

data17 = pd.read_csv('/Users/evgeny/Downloads/archive/2017.csv')
data17=data17.rename(columns={'Country name':'Country',
'Happiness.Score':'Score',
'Economy..GDP.per.Capita.':'economy',
'Health..Life.Expectancy.':'Healthy',
'Trust..Government.Corruption.':'corruption'
})
    
data17['year']=2017
data17=data17.set_index('year').sort_index()

data16 = pd.read_csv('/Users/evgeny/Downloads/archive/2016.csv')
data16['year']=2016
data16=data16.set_index('year').sort_index()
data16=data16.rename(columns={
'Happiness Score':'Score',
'Health..Life.Expectancy.':'Healthy',
'Trust (Government Corruption)':'corruption',
'Economy (GDP per Capita)':'economy',
'Health (Life Expectancy)':'Healthy'

})

data15 = pd.read_csv('/Users/evgeny/Downloads/archive/2015.csv')
data15=data15.rename(columns={
'Happiness Score':'Score',
'Health..Life.Expectancy.':'Healthy',
'Trust (Government Corruption)':'corruption',
'Economy (GDP per Capita)':'economy',
'Health (Life Expectancy)':'Healthy'

})
data15['year']=2015
data15=data15.set_index('year').sort_index()

# print(data20)
# print(data15)

data20=pd.concat([data15,data16,data17,data18,data19,data20],ignore_index=False)
data20=data20[
    ['Country','Score','corruption','Generosity','Freedom','economy','Social support','Healthy']]
# print(data20)




# pivot=data20.pivot_table(
# values='Score',
# index='year',
# columns='Country') 
# print(pivot)
# pivot.plot(kind='bar',subplots=True)



pivot2=data20.pivot_table(
values=['Score'],
index='Country',
columns='year') 
pivot2.plot(subplots=True)
plt.show()

data20=data20.query("Country == ['Denmark','Argentina','Russia','Canada','Afghanistan','Rwanda','Switzerland','Turkey','Spain','Kazakhstan','Greece','Vietnam','Albania','Armenia']")
data20['Score'].plot(kind='bar')
data20.plot(kind='bar')

plt.show()

data20[(data20.Country=='Russia')].plot(kind='barh',subplots=True)


data20[(data20.Country=='Russia')].plot(logy=True,kind='bar')

# data20['Score'].plot(kind='bar',subplots=True)

pivot=data20.pivot_table(
values='Score',
index='year',
columns='Country') 
print(pivot)

pivot.plot()

pivot1=data20.pivot_table(
values=['Score'],
index='Country',
columns='year') 
pivot1.plot(subplots=True)
print(pivot1)


pivot3=data20.pivot_table(
values=['corruption','Freedom'],
index='Country'
) 
print(pivot3)

pivot3.plot(kind='bar')

pivot4=data20.pivot_table(
values=['corruption','Freedom'],
columns='Country'
) 
print(pivot4)

pivot4.plot(kind='bar')


plt.show()