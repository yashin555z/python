
import pandas
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', size=12)

pd = pandas.read_csv('/Users/evgeny/Desktop/2/EMP_PIFL_SEX_STE_RT_Abulav.csv')



pd = pd[
    ['ref_area','sex','classif1', 'time','obs_value']
]

pd_alb=pd[pd.ref_area=='ALB']
# print(pd_bgd)

pd_alb=pd_alb.set_index('time').sort_index()

# 
pd_alb.plot(title='Значения для Албании',kind='bar', color='aqua')

print(pd_alb[pd_alb.sex=='SEX_M'])
pd_alb[pd_alb.sex=='SEX_M'].plot(title='Значения для Албанских мужчин',kind='bar', color='aqua')

pivot=pd_alb.pivot_table(
    columns='classif1',
    values='obs_value',
    index='time'
)
print(pivot)

pivot.plot(kind='bar')

pd_alb[(pd_alb.sex=='SEX_M')&(pd_alb.classif1=='STE_AGGREGATE_SLF')].plot(title='Значения для Албанских самозанятых мужчин ',kind='bar', color='aqua')


# pd_1=pd_alb
# pd_1['pd_1']=pd.sort_index().groupby(by=['sex'])['obs_value'].groupby()
# print(pd_1)

pd1=pd_alb.pivot_table(
    columns=['sex'],
    values='obs_value',
    index='time'
)
pd_alb1=pd_alb[pd_alb.sex!='SEX_T']
pd1.plot(title='Значения для Албании с разбиением по полу', kind='bar',color=['aqua','g','tan'])
pd2=pd_alb1.pivot_table(
    columns=['classif1','sex'],
    values='obs_value',
    index='time'
)



pd2.plot(title='Значения для Албании с разбиением по полу и типу занятости', kind='bar',color=['aqua','g','gold','r','m','tan'])

print(pd2)


pd_t=pd[(pd.time==2018)&(pd.sex=='SEX_T')&(pd.classif1=='STE_AGGREGATE_EES')]
pd_t=pd_t.set_index('ref_area').sort_index()
# print(pd_t)
pd_t[['obs_value']].plot(title='Значения для сотрудников всех стран с усреднением по полу в 2018 году',color='gold',kind='bar')

pd_t1=pd[(pd.time==2015)&(pd.sex=='SEX_F')&(pd.classif1=='STE_AGGREGATE_SLF')]
pd_t1=pd_t1.set_index('ref_area').sort_index()
# print(pd_t)


pd_t1[['obs_value']].plot(title='Значения для самозанятых женщин всех стран в 2015 году',color='g',kind='bar')

pd_t1=pd[(pd.time==2013)&(pd.sex!='SEX_T')&(pd.classif1=='STE_AGGREGATE_SLF')]
pd_t1=pd_t1.set_index('ref_area').sort_index()
pd_piv=pd_t1.pivot_table(
    columns=['sex'],
    values='obs_value',
    index='ref_area'
)
# print(pd_piv)
pd_piv.plot(subplots=True,title='Значения для самозанятых всех стран в 2013 году',color=['tan','aqua'],kind='bar')
plt.show()