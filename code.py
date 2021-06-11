# --------------
#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 

#Code for categorical variable
def categorical(df):

    categorical_var= df.select_dtypes(include='object').columns.tolist()
    return categorical_var


#Code for numerical variable
def numerical(df):

    numerical_var = df.select_dtypes(include='number').columns.tolist()
    return numerical_var


#code to check distribution of variable
def clear(df,col,val):

    value_counts = df[col].value_counts()[val]
    return value_counts


#Code to check instances based on the condition
def instances_based_condition(df,col1,val1,col2,val2):
   
    
    instance = df[(df[col1] > val1) & (df[col2]== val2)]
    return instance


# Code to calculate different aggreagted values according to month

def agg_values_ina_month(df,date_col,agg_col, agg):
 
    df[date_col] = pd.to_datetime(df[date_col])
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min,'sum':np.sum,'len':len}
    aggregated_value = df.pivot_table(values=[agg_col], index=df[date_col].dt.month,aggfunc={agg_col:aggregate[agg]})
    return aggregated_value


# Code to group values based on the feature
def group_values(df,col1,agg1):

    
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min,'sum':np.sum,'len':len}
    grouping = df.groupby(col1).agg(aggregate[agg1])
    return grouping


# function for conversion 
def convert(df,celsius):
 
    centigrade_temps = df[celsius]
    converted_temp =  1.8*centigrade_temps + 32
    return converted_temp



weather = pd.read_csv(path)
weather.head()


print(categorical(weather))
print(numerical(weather))




print(clear(weather,"Weather",'Clear'))
print(clear(weather,"Wind Spd (km/h)", 4))




wind_speed_35_vis_25 = instances_based_condition(weather,'Wind Spd (km/h)',35,'Visibility (km)',25)

 

agg_values_ina_month(weather,'Date/Time','Dew Point Temp (C)','mean')



mean_weather = group_values(weather,"Weather",'mean')


# You have a temperature data and wanted to convert celsius temperature into fahrehheit temperatures you can call the function convert.

weather_fahrehheit = convert(weather,"Temp (C)")



