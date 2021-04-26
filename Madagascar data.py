#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[11]:


income_data = pd.read_excel('Localized (ranomafana) Households Income.xls')
crop=income_data.loc[4:8,['Income per year for a household into the Ranomafana region for 1 hecatre of land','Unnamed: 6']]


# In[12]:


labels_1 = crop.iloc[0:5,0]
sizes_1 = crop.iloc[0:5,1]
fig = plt.figure(dpi=300)
plt.bar(labels_1, sizes_1, color=('royalblue','royalblue','royalblue','royalblue','red'))
plt.title('Coffee Brings More Wealth to Local Residents')
plt.ylabel("Yearly Income per Household in $ ")
plt.show()


# In[13]:


xls = pd.ExcelFile('MDG.xlsx')
df1 = pd.read_excel(xls, 'Country tree cover loss')
df2 = pd.read_excel(xls, 'Country biomass loss')
df3 = pd.read_excel(xls, 'Country co2 emissions')


# In[14]:


arr1 = df1.iloc[4:5,-11:].values
arr2 = df2.iloc[4:5,-11:].values
arr3 = df3.iloc[4:5,-11:].values
l1= arr1.tolist()
l2= arr2.tolist()
l3= arr3.tolist()


# In[15]:


from itertools import chain
list1 = list(chain.from_iterable(l1))
print(list1)
list2 = list(chain.from_iterable(l2))
print(list2)
list3 = list(chain.from_iterable(l3))
print(list3)


# In[21]:


x2=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=x2,y=list1, name="Tree Cover Loss"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x2, y=list2, name="Biomass Loss"),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(x=x2, y=list3, name="CO2 Emissions"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Ecological Environment - Country Level"
)

fig.update_xaxes(title_text="Year")

fig.update_yaxes(title_text="Hectares", secondary_y=False)
fig.update_yaxes(title_text="Metric tonnes", secondary_y=True)

fig.show()


# In[22]:


df4 = pd.read_excel(xls, 'Subnational 1 tree cover loss')
df5 = pd.read_excel(xls, 'Subnational 1 biomass loss')
df6 = pd.read_excel(xls, 'Subnational 1 co2 emissions')


# In[23]:


df4_1 = df4[df4['threshold'].isin([30])]
df5_1 = df5[df5['threshold'].isin([30])]
df6_1 = df6[df6['threshold'].isin([30])]
l4_1 = df4_1.iloc[0:1, np.r_[14:25]].values.tolist()
l5_1 = df5_1.iloc[0:1, np.r_[15:26]].values.tolist()
l6_1 = df6_1.iloc[0:1, np.r_[14:25]].values.tolist()
list4_1 = list(chain.from_iterable(l4_1))
list5_1 = list(chain.from_iterable(l5_1))
list6_1 = list(chain.from_iterable(l6_1))


# In[24]:


fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=x2,y=list4_1, name="Tree Cover Loss"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x2, y=list5_1, name="Biomass Loss"),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(x=x2, y=list6_1, name="CO2 Emissions"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Ecological Environment - Antananarivo"
)

fig.update_xaxes(title_text="Year")

fig.update_yaxes(title_text="Hectares", secondary_y=False)
fig.update_yaxes(title_text="Metric tonnes", secondary_y=True)

fig.show()


# In[25]:


l4_2 = df4_1.iloc[1:2, np.r_[14:25]].values.tolist()
l5_2 = df5_1.iloc[1:2, np.r_[15:26]].values.tolist()
l6_2 = df6_1.iloc[1:2, np.r_[14:25]].values.tolist()
list4_2 = list(chain.from_iterable(l4_2))
print(list4_2)
list5_2 = list(chain.from_iterable(l5_2))
list6_2 = list(chain.from_iterable(l6_2))
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=x2,y=list4_2, name="Tree Cover Loss"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x2, y=list5_2, name="Biomass Loss"),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(x=x2, y=list6_2, name="CO2 Emissions"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Ecological Environment - Antsiranana"
)

fig.update_xaxes(title_text="Year")

fig.update_yaxes(title_text="Hectares", secondary_y=False)
fig.update_yaxes(title_text="Metric tonnes", secondary_y=True)

fig.show()


# In[26]:


l4_3 = df4_1.iloc[2:3, np.r_[14:25]].values.tolist()
l5_3 = df5_1.iloc[2:3, np.r_[15:26]].values.tolist()
l6_3 = df6_1.iloc[2:3, np.r_[14:25]].values.tolist()
list4_3 = list(chain.from_iterable(l4_3))
list5_3 = list(chain.from_iterable(l5_3))
list6_3 = list(chain.from_iterable(l6_3))
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=x2,y=list4_3, name="Tree Cover Loss"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x2, y=list5_3, name="Biomass Loss"),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(x=x2, y=list6_3, name="CO2 Emissions"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Ecological Environment - Fianarantsoa"
)

fig.update_xaxes(title_text="Year")

fig.update_yaxes(title_text="Hectares", secondary_y=False)
fig.update_yaxes(title_text="Metric tonnes", secondary_y=True)

fig.show()


# In[27]:


l4_4 = df4_1.iloc[3:4, np.r_[14:25]].values.tolist()
l5_4 = df5_1.iloc[3:4, np.r_[15:26]].values.tolist()
l6_4 = df6_1.iloc[3:4, np.r_[14:25]].values.tolist()
list4_4 = list(chain.from_iterable(l4_4))
list5_4 = list(chain.from_iterable(l5_4))
list6_4 = list(chain.from_iterable(l6_4))
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=x2,y=list4_4, name="Tree Cover Loss"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x2, y=list5_4, name="Biomass Loss"),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(x=x2, y=list6_4, name="CO2 Emissions"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Ecological Environment - Mahajanga"
)

fig.update_xaxes(title_text="Year")

fig.update_yaxes(title_text="Hectares", secondary_y=False)
fig.update_yaxes(title_text="Metric tonnes", secondary_y=True)

fig.show()


# In[28]:


l4_5 = df4_1.iloc[4:5, np.r_[14:25]].values.tolist()
l5_5 = df5_1.iloc[4:5, np.r_[15:26]].values.tolist()
l6_5 = df6_1.iloc[4:5, np.r_[14:25]].values.tolist()
list4_5 = list(chain.from_iterable(l4_5))
list5_5 = list(chain.from_iterable(l5_5))
list6_5 = list(chain.from_iterable(l6_5))
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=x2,y=list4_5, name="Tree Cover Loss"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x2, y=list5_5, name="Biomass Loss"),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(x=x2, y=list6_5, name="CO2 Emissions"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Ecological Environment - Toamasina"
)

fig.update_xaxes(title_text="Year")

fig.update_yaxes(title_text="Hectares", secondary_y=False)
fig.update_yaxes(title_text="Metric tonnes", secondary_y=True)

fig.show()


# In[29]:


l4_6 = df4_1.iloc[5:6, np.r_[14:25]].values.tolist()
l5_6 = df5_1.iloc[5:6, np.r_[15:26]].values.tolist()
l6_6 = df6_1.iloc[5:6, np.r_[14:25]].values.tolist()
list4_6 = list(chain.from_iterable(l4_6))
list5_6 = list(chain.from_iterable(l5_6))
list6_6 = list(chain.from_iterable(l6_6))
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=x2,y=list4_6, name="Tree Cover Loss"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x2, y=list5_6, name="Biomass Loss"),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(x=x2, y=list6_6, name="CO2 Emissions"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Ecological Environment - Toliary"
)

fig.update_xaxes(title_text="Year")

fig.update_yaxes(title_text="Hectares", secondary_y=False)
fig.update_yaxes(title_text="Metric tonnes", secondary_y=True)

fig.show()


# In[ ]:




