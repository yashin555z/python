from plotly import tools
import plotly.offline as py
import plotly.graph_objs as go
import pandas
import matplotlib.pyplot as plt
import numpy as np
import time
plt.rc('font', size=10)

data = pandas.read_csv('/Users/evgeny/Desktop/lb3/EAR_4MTH_SEX_ECO_CUR_NB_A.csv')
data = data[
    ['ref_area','sex','classif1','classif2', 'time','obs_value','indicator','source']
]
data = data[
    (data.classif1== 'ECO_AGGREGATE_TOTAL')&(data.sex=='SEX_T')]
data_usa = data[
    (data.ref_area == 'USA')&(data.classif2 == 'CUR_TYPE_USD')
]
# print(data_rus)

data_une = pandas.read_csv('/Users/evgeny/Desktop/2/UNE_2EAP_SEX_AGE_RT_A.csv')

data_une = data_une[data_une.ref_area=='USA']

data_une=data_une[
    ['ref_area','sex','classif1','time','obs_value']
]
data_une1=data_une[(data_une.classif1!='AGE_YTHADULT_YGE15')&(data_une.sex!='SEX_T')]

# print(data_une1)


n=1991
while n<=2021:
    workers=100-data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_M')&(data_une1.classif1=='AGE_YTHADULT_YGE25')].obs_value.min()-data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_F')&(data_une1.classif1=='AGE_YTHADULT_YGE25')].obs_value.max()
    trace1 = go.Pie(
        values=[data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_M')&(data_une1.classif1=='AGE_YTHADULT_YGE25')].obs_value.min(),
    data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_F')&(data_une1.classif1=='AGE_YTHADULT_YGE25')].obs_value.max(),
    workers],
        labels=['Безработные Мужчины 25+','Безработные Женщины 25+','Работающие'],
        
        domain=dict(x=[0, 0.4]),
        name="25+",
        hoverinfo="label+percent+name",
    )
    workers=100-data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_M')&(data_une1.classif1=='AGE_YTHADULT_Y15-24')].obs_value.min()-data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_F')&(data_une1.classif1=='AGE_YTHADULT_Y15-24')].obs_value.max()
    trace2 = go.Pie(
        values=[data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_M')&(data_une1.classif1=='AGE_YTHADULT_Y15-24')].obs_value.min(),
    data_une1[(data_une1.time==n)&(data_une1.sex=='SEX_F')&(data_une1.classif1=='AGE_YTHADULT_Y15-24')].obs_value.max(),
    workers],
        labels=['Безработные Мужчины до 25','Безработные Женщины до 25','Работающие'],
        domain=dict(x=[0.6, 1]),
        name="15-24",
        hoverinfo="label+percent+name",
    )
    layout = go.Layout(title=n)
    data = [trace1, trace2]
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='simple-pie-subplot')
    n=n+1
    if(n==2020):
        break

    time.sleep(0.05)

plt.show()


data_usa=data_usa.set_index('time').sort_index()

pd=pandas.pivot_table(data_une1,index=["time"], values=["obs_value"],columns=["classif1","sex"])


pd.plot(title='Уровень безработицы в США',kind='bar',subplots=True)

pd['salary']=data_usa.obs_value/100


pd.plot(title='Уровень безработицы в США относительно зарплаты',kind='bar',logy=True)

plt.show()



n=1991
while n<2021:
    labels = ['Безработные Мужчины 25+','Безработные Женщины 25+','Работающие']
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

    plt.show()

    labels = ['Безработные Мужчины до 25','Безработные Женщины до 25','Работающие']
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


# data_rus=data_rus.set_index('time').sort_index()

# pd=pandas.pivot_table(data_une1,index=["time"], values=["obs_value"],columns=["classif1","sex"])


# pd.plot(title='Уровень безработицы в США',kind='bar',subplots=True)


# pd['salary']=data_rus.obs_value/100


# pd.plot(title='Уровень безработицы в США относительно зарплаты',kind='bar',logy=True)

# plt.show()






