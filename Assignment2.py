
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d13/3f77d14c3d1fa1ac997d5414f38e394eeb9a734db495693c70daab1f.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Dubai, Dubai, United Arab Emirates**, and the stations the data comes from are shown on the map below.

# In[1]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(13,'3f77d14c3d1fa1ac997d5414f38e394eeb9a734db495693c70daab1f')


# In[2]:

get_ipython().magic('matplotlib notebook')


# In[ ]:




# In[3]:

import pandas as pd
from datetime import datetime
import numpy as np
df=pd.read_csv('data/C2A2_data/BinnedCsvs_d13/3f77d14c3d1fa1ac997d5414f38e394eeb9a734db495693c70daab1f.csv')
df.head()
df['Date_Act']=pd.to_datetime(df['Date'])

df_2005_2014=df[((df['Date_Act'].dt.year>=2005) & (df['Date_Act'].dt.year<=2014)) & ((df['Date_Act'].dt.day!=29) | (df['Date_Act'].dt.month!=2)) ]
df_2015=df[(df['Date_Act'].dt.year==2015) &((df['Date_Act'].dt.day!=29) | (df['Date_Act'].dt.month!=2))]
df_2005_2014['daymonth']=pd.to_numeric(df_2005_2014['Date_Act'].dt.month*100+df_2005_2014['Date_Act'].dt.day)
df_2005_2014_max=pd.DataFrame(df_2005_2014.groupby(df_2005_2014['daymonth'])['Data_Value'].max())
df_2005_2014_max['Daynumber']=range(1,len(df_2005_2014_max)+1)
df_2005_2014_min=pd.DataFrame(df_2005_2014.groupby(df_2005_2014['daymonth'])['Data_Value'].min())
df_2005_2014_min['Daynumber']=range(1,len(df_2005_2014_min)+1)
df_2005_2014_max=df_2005_2014_max.rename(columns={'Data_Value':'2005-2014_Max_temp'})
df_2005_2014_min=df_2005_2014_min.rename(columns={'Data_Value':'2005-2014_Min_temp'})
plt.plot(df_2005_2014_max['Daynumber'],df_2005_2014_max['2005-2014_Max_temp'])
plt.plot(df_2005_2014_min['Daynumber'],df_2005_2014_min['2005-2014_Min_temp'])
len(df_2005_2014_min.index)
df_2015['daymonth']=df_2015['Date_Act'].dt.month*100+df_2015['Date_Act'].dt.day
plt.gca().fill_between(range(len(df_2005_2014_min.index)), 
                       df_2005_2014_min['2005-2014_Min_temp'], df_2005_2014_max['2005-2014_Max_temp'], 
                       facecolor='blue', 
                       alpha=0.25)

df_2015_max=pd.DataFrame(df_2015.groupby(df_2015['daymonth'])['Data_Value'].max())
df_2015_max['Daynumber']=range(1,len(df_2015_max)+1)
df_2015_max['Day']=df_2015_max.index
df_2015_min=pd.DataFrame(df_2015.groupby(df_2015['daymonth'])['Data_Value'].min())
df_2015_min['Daynumber']=range(1,len(df_2015_min)+1)
df_2015_max=df_2015_max.rename(columns={'Data_Value':'2015_Max_temp'})
df_2015_min=df_2015_min.rename(columns={'Data_Value':'2015_Min_temp'})

df_2015_temp=pd.merge(df_2015_max,df_2015_min,how='left',on=['Daynumber'])
df_2015_temp2=pd.merge(df_2015_temp,df_2005_2014_max,how='left',on=['Daynumber'])
df_2015_temp3=pd.merge(df_2015_temp2,df_2005_2014_min,how='left',on=['Daynumber'])
df_2015_temp3['check']=np.where((df_2015_temp3['2015_Max_temp']>df_2015_temp3['2005-2014_Max_temp']),1,0)
df_2015_temp4=df_2015_temp3[df_2015_temp3['check']==1]
df_2015_temp3['check2']=np.where((df_2015_temp3['2015_Min_temp']<df_2015_temp3['2005-2014_Min_temp']),1,0)
df_2015_temp5=df_2015_temp3[df_2015_temp3['check2']==1]
df_2015_hilo=pd.merge(df_2015_temp4,df_2015,how='left',left_on=['Day'],right_on=['daymonth'])

plt.scatter(df_2015_temp4['Daynumber'],df_2015_temp4['2015_Max_temp'],c='r')
plt.scatter(df_2015_temp5['Daynumber'],df_2015_temp5['2015_Min_temp'],c='g')
plt.legend(prop={'size':6})


# In[4]:

plt.xlabel('Day of the Year')
# add a label to the y axis
plt.ylabel('Temperature')
# add a title
plt.title('Maximum and minimum temperatures per day across the years ')


# In[5]:

plt.tick_params(left='off',bottom='off')
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.savefig('Temperature variation between 2005-2015.png', bbox_inches='tight')


# In[6]:

df_2005_2014=
df_Tmax=df[df['Element']=='TMAX']
df_Tmax.head()


# In[ ]:




# In[ ]:




# In[ ]:



