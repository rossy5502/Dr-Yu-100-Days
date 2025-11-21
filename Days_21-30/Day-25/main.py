import pandas as pd

data=pd.read_csv("weather_data.csv")
temp_list=data["temp"].to_list()
average_temp=round(data["temp"].mean(),2)


monday=data[data.day=="Monday"]
monday_temp=monday.temp * 9/5 + 32
print(monday_temp)