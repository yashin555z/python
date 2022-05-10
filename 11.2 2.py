import pandas
data = pandas.read_csv('/Users/evgeny/Desktop/lb3/EAR_4MTH_SEX_ECO_CUR_NB_A.csv')
(row_count, col_count) = data.shape


data = data[['ref_area', 'sex', 'time', 'obs_value', 'classif1', 'classif2']]

data_ref_area = pandas.read_csv('/Users/evgeny/Desktop/lb3/2.csv', index_col = 'ref_area')

data_ref_area = data_ref_area.rename(
    columns={' ref_area.label': 'ref_area_label'}
)
data_ref_area=data_ref_area[['ref_area_label']]


data = data.join(data_ref_area, on = ['ref_area'])
data = data[['ref_area', 'ref_area_label', 'sex', 'classif1', 'classif2', 'time', 'obs_value']]

print(data)
print("Максимальная средняя зарплата для женщин: ")
print(data[
          (data.classif1 == 'ECO_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_F') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.max())


print("Максимальная средняя зарплата для мужчин: ")
print(data[
          (data.classif1 == 'ECO_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_M') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.max())


print("Минимальная средняя зарплата для женщин: ")
print(data[
          (data.classif1 == 'ECO_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_F') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.min())


print("Минимальная средняя зарплата для мужчин: ")
print(data[
          (data.classif1 == 'ECO_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_M') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.min())


print("средня зарплата для женщин: ")
print(data[
          (data.classif1 == 'ECO_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_F') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.mean())


print("средня зарплата для мужчин: ")
print(data[
          (data.classif1 == 'ECO_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_M') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.mean())


print("Медианная средняя зарплата для женщин")
print(data[
          (data.classif1 == 'ECO_AGGREGATE_TOTAL') &
          (data.sex == 'SEX_F') &
          (data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.median())


print("Максимальная зарплата для женщин в науке ")
print(data[
          (data.classif1 == 'ECO_ISIC4_M') &(data.sex == 'SEX_T') &(data.classif2 == 'CUR_TYPE_USD')
      ].obs_value.max())



