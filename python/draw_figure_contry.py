import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

countrywise = pd.read_csv("./data/country_wise_latest.csv")

temp_data = countrywise.iloc[:,[8,9,14]].groupby("WHO Region").agg(np.mean)
fig, ax1 = plt.subplots(figsize=(12,6))

sns.barplot(x = temp_data.index.to_list(), y=temp_data.iloc[:,1].to_list(),  alpha=0.5, ax=ax1,label="Recovered/100 cases")
sns.barplot(x = temp_data.index.to_list(), y=temp_data.iloc[:,0].to_list(), color = "black", alpha=0.5, ax=ax1,label="Death/100 cases")

plt.legend()
plt.title("Death and Recovered Statistics per 100 Cases",fontsize=20)
plt.savefig("./result/Death_Recovered_record_contrywise.png")
