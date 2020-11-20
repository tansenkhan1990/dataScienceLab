import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

import torch as torch

# data = pd.read_csv(
#     "https://storage.googleapis.com/covid19-open-data/v2/main.csv",
#     usecols=["urban_area","life_expectancy","infant_mortality_rate","adult_male_mortality_rate",
#     "adult_female_mortality_rate","pollution_mortality_rate","comorbidity_mortality_rate","hospital_beds",
#     "nurses","physicians","health_expenditure","out_of_pocket_health_expenditure","emergency_investment_in_healthcare",
#     "stringency_index","average_temperature","relative_humidity"
#     ],
# )
data = pd.read_csv(
    "/home/tansen/my files/dataScienceLab/GCP_COVID19_MERGED.csv"
)
print("**********************************")
data = data.fillna(0)

# print(data['urban_area'].dtype)
data = data[data['urban_area'] <= 200000]
#print(data[data['urban_area'] < 0])
# sns.boxplot(x=data['urban_area'])

#print(data['life_expectancy'].dtype)
data = data[data['life_expectancy'] <= 2000]
#print(data[data['life_expectancy'] < 0])
# sns.boxplot(x=data['life_expectancy'])



# print(data['hospital_beds'].dtype)
# data = data[data['hospital_beds']<=10]
# sns.boxplot(x=data['hospital_beds'])


print(data['nurses'].dtype)
#sns.boxplot(x=data['nurses'])
# print(data[data['nurses'] < 0])


print(data['physicians'].dtype)
data = data[data['physicians'] <= 8]
# sns.boxplot(x=data['physicians'])
# print(data[data['physicians'] < 0])


print(data['health_expenditure'].dtype)
data = data[data['health_expenditure'] <= 7000]
# sns.boxplot(x=data['health_expenditure'])
# print(data[data['health_expenditure'] < 0])


print(data['out_of_pocket_health_expenditure'].dtype)
#sns.boxplot(x=data['out_of_pocket_health_expenditure'])
# print(data[data['out_of_pocket_health_expenditure'] < 0])



print(data['emergency_investment_in_healthcare'].dtype)
#data = data[data['emergency_investment_in_healthcare'] <= 3]
#sns.boxplot(x=data['emergency_investment_in_healthcare'])
# print(data[data['emergency_investment_in_healthcare'] < 0])


print(data['stringency_index'].dtype)
#sns.boxplot(x=data['stringency_index'])
# print(data[data['stringency_index'] < 0])


print(data['average_temperature'].dtype)
#sns.boxplot(x=data['average_temperature'])
# print(data[data['average_temperature'] < 0])
