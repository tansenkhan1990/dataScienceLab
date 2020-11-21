import pandas as pd

import seaborn as sns

data = pd.read_csv('/home/tansen/my files/dataScienceLab/gcp_covid19_countrylevel.csv',
                   usecols=["key","date","country_name","total_hospitalized", "current_hospitalized", "new_intensive_care", "total_intensive_care",
                       "hospital_beds","nurses","physicians","health_expenditure","out_of_pocket_health_expenditure"
                    ]
                   )

sns.boxplot(x=data['total_hospitalized'])
