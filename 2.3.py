import pandas
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', size=10)

data = pandas.read_csv('/Users/evgeny/Desktop/lb3/EAR_4MTH_SEX_ECO_CUR_NB_A.csv')
data = data[
    ['ref_area','sex','classif1','classif2', 'time','obs_value','indicator','source']
]
data = data[
    (data.classif1== 'ECO_AGGREGATE_TOTAL')&(data.sex=='SEX_T')]
data_rus = data[
    (data.ref_area == 'RUS')&(data.classif2 == 'CUR_TYPE_USD')
]
# print(data_rus)

data_une = pandas.read_csv('/Users/evgeny/Desktop/2/UNE_2EAP_SEX_AGE_RT_A.csv')

data_une = data_une[data_une.ref_area=='RUS']

data_une=data_une[
    ['ref_area','sex','classif1','time','obs_value']
]
data_une1=data_une[(data_une.classif1!='AGE_YTHADULT_YGE15')]

# print(data_une1)

# data_une1[data_une1.ref_area=='RUS'][
#     ['classif1']].plot(title='100 миллиардов из 1997 исходя из зарплат',kind='pie',color='k')
n=2018
while n<2021:
    labels = ['Безработные Мужчины 25+','Безработные Женщины 25+','работные']
    workers=100-data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_M')&(data_une1.classif1=='AGE_YTHADULT_YGE25')].obs_value.min()-data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_F')&(data_une1.classif1=='AGE_YTHADULT_YGE25')].obs_value.max()


    values = [data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_M')&(data_une1.classif1=='AGE_YTHADULT_YGE25')].obs_value.min(),
    data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_F')&(data_une1.classif1=='AGE_YTHADULT_YGE25')].obs_value.max(),
    workers]

    colors = ['plum','darkslateblue','lightgray']
    explode = [0.2,0.2,0.3]
    plt.figure('25+')
    plt.title(n)
    plt.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)
    plt.axis('equal')
    
    # plt.show()

    labels = ['Безработные Мужчины до 25','Безработные Женщины до 25','Работные']
    workers=100-data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_M')&(data_une1.classif1=='AGE_YTHADULT_Y15-24')].obs_value.min()-data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_F')&(data_une1.classif1=='AGE_YTHADULT_Y15-24')].obs_value.max()

    values = [data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_M')&(data_une1.classif1=='AGE_YTHADULT_Y15-24')].obs_value.min(),
    data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_F')&(data_une1.classif1=='AGE_YTHADULT_Y15-24')].obs_value.max(),
    workers]

    colors = ['olive','green','lightgray']
    explode = [0.1,0.1,0.2]
    plt.figure('15-24')
    plt.title(n)
    plt.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)
    plt.axis('equal')
    


    n=n+1
    plt.show()





data_une1=data_une1.set_index('time').sort_index()
data_rus=data_rus.set_index('time').sort_index()
# data_une1[data_une1.ref_area == 'RUS'][
#     ['obs_value']].plot(title='Миллион из 1969 года до 1997 года',kind='bar')



# pivot=data_une1.pivot_table(values='obs_value',index=['time','classif1'],columns='classif1')
# pivot.plot(title='Миллион из 1969 года до 1997 года',kind='bar',subplots=True)
# print(pivot)
pd=pandas.pivot_table(data_une1,index=["time"], values=["obs_value"],columns=["classif1","sex"])
# print(pd.obs_value)

pd.plot(title='Уровень безработицы в России',kind='bar',subplots=True)

# print(data_rus.obs_value.mean())
pd['new_col']=data_rus.obs_value/100
# print(pd)

pd.plot(title='Уровень безработицы в России',kind='bar',logy=True)




plt.show()






