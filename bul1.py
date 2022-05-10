import pandas
data = pandas.read_csv('/Users/evgeny/Desktop/lb3/EAR_4MTH_SEX_ECO_CUR_NB_A.csv')

data = data[['ref_area', 'sex', 'time', 'obs_value', 'classif1', 'classif2']]  

data = data[
    (data.ref_area != 'BLR') & (data.ref_area != 'ZWE')
]

print('Максимум для Турецких женщин в сфере лечения',data[  
          (data.classif1 == 'ECO_ISIC4_N') &
          (data.sex == 'SEX_F') &
          (data.ref_area=='TUR')&
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.max())

 

print('Минимум для мужчин в конструировании',data[   
          (data.classif1 == 'ECO_ISIC3_F') &
          (data.sex == 'SEX_M') &
          (data.classif2 == 'CUR_TYPE_USD')&
          (data.time==2015)
      ].obs_value.min())

   

print('Среднее значение для женщин в рыболовле',data[
          (data.classif1 == 'ECO_ISIC3_B') &
          (data.sex == 'SEX_F') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.mean())

   

print('медианное значение для мужчин в ресторанах и отелях',data[
          (data.classif1 == 'ECO_ISIC3_H') &
          (data.sex == 'SEX_M') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.median())

print('Максимум для Французских женщин в сфере автоторговли',data[  
          (data.classif1 == 'ECO_ISIC4_G') &
          (data.sex == 'SEX_F') &
          (data.ref_area=='FRA')&
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.max())

 

   
print('медианное значение для мужчин в сфере образования',data[
          (data.classif1 == 'ECO_ISIC3_M') &
          (data.sex == 'SEX_M') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.median())

print('Минимум для мужчин в сфере коммуникаций c 2018',data[   
          (data.classif1 == 'ECO_ISIC3_E') &
          (data.sex == 'SEX_M') &
          (data.classif2 == 'CUR_TYPE_USD')&
          (data.time>2018)
      ].obs_value.min())

   

print('Среднее значение для женщин в бизнесе',data[
          (data.classif1 == 'ECO_ISIC3_K') &
          (data.sex == 'SEX_F') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.mean())