import pandas as pd

data = pd.read_csv(
    "/home/tansen/my files/dataScienceLab/GCP_COVID19_MERGED.csv"
)
print("**********************************")
data = data.fillna(0)
for col in data.columns:
    print(col)