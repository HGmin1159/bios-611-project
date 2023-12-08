import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("../data/day_wise.csv")
data["Date"] = pd.to_datetime(data["Date"])

fig,ax = plt.subplots(1,2,figsize = (10,5))

sns.lineplot(x=data["Date"], y=data["New cases"], label="New Cases", color='r',ax=ax[0])
plt.ylabel("")
ax[0].set_title("The daily Case Report at 2020")

sns.lineplot(x=data["Date"], y=data["Deaths / 100 Cases"], label="Deaths / 100 Cases",ax=ax[1])
sns.lineplot(x=data["Date"], y=data["Recovered / 100 Cases"], label="Recovered / 100 Cases",ax=ax[1])

ax[0].tick_params(axis='x', rotation=45)
ax[1].tick_params(axis='x', rotation=45)

ax[1].set_title("Death and Recovered Statistics per 100 cases")
plt.ylabel("")
plt.legend()

plt.savefig("./figure/Covid_Daily_Report.png")