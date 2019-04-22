
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import atlite

import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


h = pd.read_csv('data/jrc-hydro-power-plant-database.csv')


# In[3]:


h.type.unique()


# In[4]:


h.head()


# In[5]:


h['Coordinates'] = list(zip(h.lon, h.lat))

h['Coordinates'] = h['Coordinates'].apply(Point)

g = gpd.GeoDataFrame(h, geometry='Coordinates')


# In[6]:


g.plot()


# In[7]:


g[h.type=='HDAM'][h.country_code=='ES'].plot()


# In[8]:


cutout = atlite.Cutout('europe-2011-01')

inflow = cutout.hydro(h[h.country_code=='ES'], 'hydroBASINS/hybas_eu_lev07_v1c.shp')


# In[9]:


inflow


# In[10]:


inflow.data.shape


# In[11]:


inflow.data[-1,:]

