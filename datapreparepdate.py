import pandas as pd

import seaborn as sns

data = pd.read_csv('/home/tansen/my files/dataScienceLab/gcp_covid19_countrylevel.csv',
                   usecols=["key","date","country_name","total_hospitalized", "current_hospitalized", "new_intensive_care", "total_intensive_care","area",
                       "hospital_beds","nurses","physicians","health_expenditure","out_of_pocket_health_expenditure"
                    ]
                   )
main_data = data

print(data.shape)

##########remove a field 

df = data.drop(data[data.area <= 10000].index)

#######show loss 

totalnull_df = df.isnull().sum()
percentnull = totalnull_df/len(df)*100
display(percentnull)

######## shows country 

df[df.total_hospitalized.notnull()].country_name.unique()

########shows missing values

df = data
totalnull_df = df.isna().sum()
percentnull = totalnull_df/len(df)*100
display(percentnull)

########formet the dates mssing values 

data['year'] = pd.DatetimeIndex(data['date']).year
data['month'] = pd.DatetimeIndex(data['date']).month
data['day'] = pd.DatetimeIndex(data['date']).day
df = data[data.month <= 1]
totalnull_df = df.isna().sum()
percentnull = totalnull_df/len(df)*100
display(percentnull)

######## formet the date and missing values

data['year'] = pd.DatetimeIndex(data['date']).year
data['month'] = pd.DatetimeIndex(data['date']).month
data['day'] = pd.DatetimeIndex(data['date']).day
df = data[data.month <= 11]
totalnull_df = df.isna().sum()
percentnull = totalnull_df/len(df)*100
display(percentnull)

#formet the dates and missing vlaues
data['year'] = pd.DatetimeIndex(data['date']).year
data['month'] = pd.DatetimeIndex(data['date']).month
data['day'] = pd.DatetimeIndex(data['date']).day
df = data[data.month <= 3]
totalnull_df = df.isna().sum()
percentnull = totalnull_df/len(df)*100
display(percentnull)

#formet and missing values

data['year'] = pd.DatetimeIndex(data['date']).year
data['month'] = pd.DatetimeIndex(data['date']).month
data['day'] = pd.DatetimeIndex(data['date']).day
df = data[data.month <= 4]
totalnull_df = df.isna().sum()
percentnull = totalnull_df/len(df)*100
display(percentnull)

# dates and missing values
data['year'] = pd.DatetimeIndex(data['date']).year
data['month'] = pd.DatetimeIndex(data['date']).month
data['day'] = pd.DatetimeIndex(data['date']).day
df = data[data.month <= 5]
totalnull_df = df.isna().sum()
percentnull = totalnull_df/len(df)*100
display(percentnull)

#check null values 
print(data.key.isna().sum())

print(data.key.isnull().sum())

print(data.date.isna().sum())

print(data.date.isnull().sum())

print(data.country_name.isna().sum())

print(data.country_name.isnull().sum())

print(data.total_hospitalized.isna().sum())

print(data.total_hospitalized.isnull().sum())

print(data.total_hospitalized.max())

print(data.total_hospitalized.min())

print(data.current_hospitalized.isna().sum())

print(data.current_hospitalized.isnull().sum())

print(data.current_hospitalized.max())

print(data.current_hospitalized.min())

print(data.new_intensive_care.isna().sum())

print(data.new_intensive_care.min())

print(data.new_intensive_care.max())

print(data.total_intensive_care.isna().sum())

print(data.total_intensive_care.max())

print(data.total_intensive_care.min())

print(data.hospital_beds.isnull().sum())

print(data.hospital_beds.max())

print(data.hospital_beds.min())

print(data.nurses.isna().sum())

print(data.nurses.max())

print(data.nurses.min())

print(data.physicians.isna().sum())

print(data.physicians.max())

print(data.physicians.min())

print(data.health_expenditure.isna().sum())

print(data.health_expenditure.max())

print(data.health_expenditure.min())

print(data.out_of_pocket_health_expenditure.isna().sum())

print(data.out_of_pocket_health_expenditure.max())

print(data.out_of_pocket_health_expenditure.min())

############show the box plot

sns.boxplot(x = data['total_hospitalized'])

sns.boxplot(x = data['current_hospitalized'])
############# show bar chat

sns.set_theme(style="whitegrid")
data['year'] = pd.DatetimeIndex(data['date']).year
data['month'] = pd.DatetimeIndex(data['date']).month
data['day'] = pd.DatetimeIndex(data['date']).day
ax = sns.barplot(x = data['month'], y="total_hospitalized", data=data)

ax = sns.barplot(x = 'month', y = data.new_intensive_care, data=data)


ax = sns.barplot(x = data['month'], y="current_hospitalized", data=data)

ax = sns.barplot(x = 'month', y = data.total_intensive_care, data=data)

ax = sns.barplot(x = 'month', y = data.hospital_beds, data=data)

ax = sns.barplot(x = 'month', y = data.physicians, data=data)

ax = sns.barplot(x = 'month', y = data.health_expenditure, data=data)

ax = sns.barplot(x = 'month', y = data.out_of_pocket_health_expenditure, data=data)
##########groupBy 

print(data.groupby(['month','total_hospitalized','country_name']).size())

print(data.groupby(['country_name','month','total_hospitalized','current_hospitalized']).size())

print(data.groupby(['country_name','date','new_intensive_care']).size())

print(data.groupby(['country_name','month','total_intensive_care']).size())

print(data.groupby(['country_name','date','hospital_beds']).size())

print(data.groupby(['country_name','date','physicians']).size())

print(data.groupby(['country_name','date','health_expenditure']).size())

print(data.groupby(['country_name','date','out_of_pocket_health_expenditure']).size())

###########filter

print(data[data.month == 1][['country_name','total_hospitalized','current_hospitalized']])

print(data[data.month == 2][['country_name','total_hospitalized','current_hospitalized']])

print(data[data.month == 3][['country_name','total_hospitalized','current_hospitalized']])

print(data[data.month == 4][['country_name','total_hospitalized','current_hospitalized']])

print(data[(data.month == 1) & (data.country_name == 'China')])

print(data[(data.month == 2) & (data.country_name == 'China')])

print(data[(data.month <= 4) & (data.country_name == 'China') & (data.total_hospitalized.isna())])