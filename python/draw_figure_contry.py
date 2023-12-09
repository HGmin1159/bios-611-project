import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

countrywise = pd.read_csv("./data/country_wise_latest.csv")

temp_data = countrywise.iloc[:,[8,9,14]].groupby("WHO Region").agg(np.mean)

fig, ax = plt.subplots(1,2,figsize=(12,6))
sns.barplot(x = temp_data.index, y=temp_data.iloc[:,1], alpha=0.5, ax=ax[0],label = "Recovered per 100 cases")
ax[0].set_title("Recovered per 100 cases")
ax[0].set_ylim((50,80))
sns.barplot(x = temp_data.index, y=temp_data.iloc[:,0], alpha=0.5, ax=ax[1],label = "Deaths per 100 cases")
ax[1].set_title("Deaths per 100 cases")

ax[0].tick_params(axis='x', rotation=30)
ax[1].tick_params(axis='x', rotation=30)

fig.suptitle("Recovered and Deaths per 100 cases", fontsize=20)
plt.savefig("./figure/Death_Recoverd_record_contrywise.png")