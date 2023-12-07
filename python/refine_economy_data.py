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
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Gross domestic product based on purchasing-power-parity (PPP) share of world total"],on="Country")
refined_data = pd.merge(refined_data,data[["Country","2020"]][np.array(data["Subject Descriptor"]=="Inflation, average consumer prices")*np.array(data["Units"]=="Percent change")],on="Country")
refined_data.columns = ["Country","GDP","GDP(PPP)","Inflation Rate"]
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Volume of imports of goods and services"],on="Country")
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Volume of exports of goods and services"],on="Country")
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Unemployment rate"],on="Country")
refined_data.columns = ["Country","GDP","GDP(PPP)","Inflation Rate","Import","Export","Unemployment rate"]
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Employment"],on="Country")
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="Population"],on="Country")
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="General government revenue"],on="Country")
refined_data.columns = ["Country","GDP","GDP(PPP)","Inflation Rate","Import","Export","Unemployment rate","Employment","Population","Goverment Revenue"]
refined_data = pd.merge(refined_data,data[["Country","2020"]][data["Subject Descriptor"]=="General government total expenditure"],on="Country")
refined_data.columns = ["Country","GDP","GDP(PPP)","Inflation Rate","Import","Export","Unemployment rate","Employment","Population","Goverment Revenue","Goverment Expenditure"]
refined_data.to_csv("../data/contrywise_economicdata.csv")
