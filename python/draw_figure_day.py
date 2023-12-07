import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./data/day_wise.csv")
data["Date"] = pd.to_datetime(data["Date"])

fig,ax = plt.subplots()
sns.lineplot(x=data["Date"],y=data["Deaths / 100 Cases"],label="Deaths / 100 Cases")
sns.lineplot(x=data["Date"],y=data["Recovered / 100 Cases"],label="Recovered / 100 Cases")
plt.title("Death and Recovered Statistics per 100 cases")
plt.ylabel("")
plt.legend()
plt.savefig("./result/Death_Recovered_record_daywise.png")