# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:36:55 2021

@author: Yu Du
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import pandas as pd
from datetime import datetime
import plotly.express as px
###loading work
with open('seed.txt','r') as f:
    seed_txt=f.read()

df1 = pd.read_excel('Seed collections.xlsx')
df1 = df1.dropna(how='all')[:-1]
df1['Year'] = df1['Year'].astype(int).astype(str)
df1['Month'] = df1['Month'].astype(int).astype(str)
df1['date']= (df1['Year']).apply(lambda x:datetime.strptime(x,'%Y'))


#
st.set_page_config(layout="wide")
image = Image.open('logo.png')
st.image(image,width=1000)
st.markdown('# Conservation360  DashBoard')

select = st.sidebar.selectbox(
    '',
    ('Donors', 'Conservation-360', 'Madagascar')
)
if select=='Donors':
    st.markdown('## Donors')
    select_don = st.selectbox(
    'Donors',
    ('Your story', "Donor's trees","Trees planted in other years")
    )
    donor = pd.read_excel(r'./donor/demo donor data for U of R.xlsx')
    trees = pd.read_excel(r'./donor/2019 treesurvey data.xlsx')
    
    if select_don == 'Your story':
        donor['label']="Others'"
        st.write('Sample data')
        st.write(donor.head()[1:])
        user_input = st.text_input("Please input your name", 'Mamie Hope')
        donor['label'][donor['Donor']==user_input]='Your tree'


        fig = px.scatter_mapbox(donor, lat='Latitude', lon='Longitude', hover_name="Donor",hover_data=['Date planted','Family','Genus','Species'],
                       zoom=17,color = 'label',title='Here is your tree!')
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"l":0,"b":0})
        fig.update_layout(width=1000,height=600)
    
        st.write(fig)
        st.write('There are %d donors along with you in 2020'%len(donor['Donor'].unique()))
        
        
    if select_don == "Donor's trees":
        fig = px.scatter_mapbox(donor, lat='Latitude', lon='Longitude', hover_name="Donor",hover_data=['Date planted','Family','Genus','Species'],
                       zoom=17,color = 'Family',title='What kind of tree do donors plant')
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(width=1000,height=600)
        
    
        st.write(fig)
        fig = plt.figure()
        donor.groupby('Family').count()['Donor'].plot(kind='pie',ylabel=' ',
        title='Category of tree planted',autopct="%1.0f%%",ax=plt.gca(),
        colors = ['lightblue','purple','orange','blue','red','lightgreen'])
        st.pyplot(fig,width=1)
        seemore = st.button('see more')
        if seemore:
            st.write('hello')
    if select_don == "Trees planted in other years":
        trees['Year of planting']=trees['Year of planting'].astype(str)
        trees['Year of planting']=[i[i.find('20'):i.find('20')+4] for i in trees['Year of planting']]
        trees['Year of planting'] = trees['Year of planting'].apply(lambda x:int(x) if x!='n' else np.nan)

        trees_t = pd.concat([trees.groupby(['Latitude1','Longitude1']).count()['Year'],
                         trees[trees['Status']=='Dead'].groupby(['Latitude1','Longitude1']).count()['Status'],
                         trees[trees['Status']=='Alive'].groupby(['Latitude1','Longitude1']).count()['Year'],
                         trees.groupby(['Latitude1','Longitude1']).mean()['Year of planting']],axis=1)

        trees_t=trees_t.fillna(0)
        trees_t.columns = ['Total trees','Dead','Alive','Year of planting']
        trees_t['Dead']=trees_t['Dead'].astype(int)
        trees_t['Year of planting']=trees_t['Year of planting'].astype(int).astype(str)
        trees_t['Year of planting'][trees_t['Year of planting']=='0']=np.nan
        trees_t = trees_t.reset_index()
        trees_t['alive rate'] = round(trees_t['Alive']/trees_t['Total trees'],2)
        fig = px.scatter_mapbox(trees_t, lat='Latitude1', lon='Longitude1', hover_name='Year of planting',
                        hover_data= ['Total trees','Dead','Alive'],
                       zoom=11,size = 'Total trees',color='alive rate',
                       title= 'Trees planted across years',
                       color_continuous_scale='Rainbow',
                       range_color=[0,1])
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(width=1000,height=600)
        st.write(fig)
        fig = plt.figure()
        trees.groupby('Status').count()['Height_cm'].plot(kind='pie',ylabel=' ',
        title='Status of Trees',autopct="%1.0f%%",ax=plt.gca(),
        colors=['red','blue'])
        st.write(fig)
        

if select=='Conservation-360':
    st.markdown('## Conservation-360')
    st.markdown('### Conservation-360 always work with you!!')
    select_con = st.selectbox(
    'See our accomplishment',
    ('natural observation','seed collection', 'transplanting process')
    )
    if select_con == 'natural observation':
        naturalist_data = pd.read_csv("iNaturalist - observations-131984.csv")
        naturalist_data['taxon_kingdom_name'][pd.isnull(naturalist_data['taxon_kingdom_name'])] = 'Other'
        unique_class = list(naturalist_data['taxon_class_name'].unique())
        select_class = st.sidebar.multiselect('Taxon Class',unique_class,unique_class)
        naturalist_data = naturalist_data[naturalist_data['taxon_class_name'].isin(select_class)]
        unique_family = list(naturalist_data['taxon_family_name'].unique())
        select_family = st.sidebar.multiselect('Taxon Family',unique_family,unique_family)
        naturalist_data = naturalist_data[naturalist_data['taxon_family_name'].isin(select_family)]
        fig = px.scatter_mapbox(naturalist_data, lat='latitude', lon='longitude', hover_name='common_name',
                        hover_data=[ 'scientific_name','taxon_family_name','taxon_genus_name', 'taxon_species_name'],
                       zoom=10,color='taxon_kingdom_name',title='Natural Observations')
        fig.update_layout(mapbox_style="open-street-map")
        #fig.update_layout(margin={"r":5,"t":5,"l":5,"b":5})
        fig.update_traces(marker_size=3)
        fig.update_layout(width=1000,height=600)

        st.write(fig)
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write('Now you must be curious about what does this specy look like')
        st.write('**Following below steps to reveal its mask**')
        st.write('sample data')
        st.write(naturalist_data.loc[:,['common_name','scientific_name']].head())
        
        st.write('**Step1:Input the common name, get the scientific name**')
        user_input0 = st.text_input("Please input the common name", 'Small-toothed Sportive Lemur')
        st.write('Scientific name of %s'%user_input0+' is '+"'"+list(naturalist_data['scientific_name'][naturalist_data['common_name']==user_input0])[0]+"'")
        st.write('**Step2:Copy its name and paste in the below box to show it!!**')
        user_input = st.text_input("Please input the scientific name", 'Lepilemur microdon')
        st.write('See %s in the following link!'%user_input)
        for i in naturalist_data['image_url'][naturalist_data['scientific_name']==user_input]:
            st.write(i)
            if '?' in i:
                st.image(i[:i.find('?')])
            else:
                st.image(i)
        
    if select_con == 'seed collection':
        st.markdown('### '+seed_txt)
        fig = plt.figure(figsize=(6, 3))
        df1.groupby('date').sum()['QuantityOfSeeds (Kg)'][:-1].plot(kind='line',xlabel='',ylabel='QuantityOfSeeds (Kg)',title='Quantity of Seeds Collected Each Year',ax=plt.gca())
        st.write(fig)
        #fig1 = plt.figure(figsize=(6,3))
        #df1.groupby('Species').sum()['QuantityOfSeeds (Kg)'].sort_values(ascending=False)[:-4].plot(kind='bar',rot=60,ylabel='Quantity of Seeds (Kg)',title='The most collected seeds are Racemosa ',xlabel='',ax = plt.gca())
        #st.write(fig1)
        
    if select_con == 'transplanting process':
        st.write('''Despite some trees are planted by villagers without Conservation-360's
        staff, most trees are planted in a normal process. We'are improving to track
        every tree's information''')
        df2 = pd.read_excel('Transplanting sessions.xlsx')
        df2 = df2.dropna(how='all',axis=1)
        df2['Notes'] = df2['Notes'].fillna('Regular')
        df2['notes'] = 'Transplangting without Conservation-360 engagement'
        df2['notes'][df2['Notes']=='Regular'] = 'Transplangting with Conservation-360 engagement'
        fig = plt.figure(dpi=100)
        df2.groupby('notes').sum()['NumberOfTrees'].plot(kind='pie',ylabel=' ',
                                                 title='Most Trees are Transplanted with Conservation-360 engagement',
                                                 autopct="%1.0f%%",ax=plt.gca(),
                                                colors=['orange','grey'],
                                                textprops={'fontsize': 8},
                                                labeldistance =0.8)
        st.write(fig)
        
    


if select=='Madagascar':
    st.markdown('## Madagascar')
    
    




