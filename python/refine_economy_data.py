import numpy as np
import pandas as pd
data = pd.read_csv("../data/WEO_Data.csv")
def convert_float(x) :
    try :
        return(float(x.replace(",","")))
    except :
        return(x)

data["2020"][[type(i)==str for i in data["2020"]]] = data["2020"][[type(i)==str for i in data["2020"]]].apply(convert_float)
data["2020"][data["Scale"]=="Billions"] = data["2020"][data["Scale"]=="Billions"]*1000

refined_data = pd.DataFrame() 

refined_data["Country"] = data["Country"].unique()
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Gross domestic product, current prices"],on="Country")
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Gross domestic product, constant prices"],on="Country")
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Gross domestic product per capita, current prices"],on="Country")
refined_data.columns = ["Country","GDP","GDPchange","GDPperCapita"]
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Inflation, average consumer prices"],on="Country")
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Volume of imports of goods and services"],on="Country")
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Volume of exports of goods and services"],on="Country")
refined_data.columns = ["Country","GDP","GDPchange","GDPperCapita","Inflation","Import","Export"]
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Population"],on="Country")
refined_data.columns = ["Country","GDP","GDPchange","GDPperCapita","Inflation","Import","Export","Population"]


data_country = pd.read_csv("../data/country_wise_latest.csv")
data_country.columns = ['Country/Region', 'Confirmed', 'Deaths', 'Recovered', 'Active',
       'New cases', 'New deaths', 'New recovered', 'Deathsper100Cases',
       'Recoveredper100Cases', 'Deathsper100Recovered',
       'Confirmed last week', '1 week change', '1 week_increase',
       'WHO Region']

data = pd.merge(refined_data,data_country,left_on="Country",right_on="Country/Region")

data.to_csv("../data/contrywise_economicdata.csv")