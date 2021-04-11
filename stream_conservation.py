# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:36:55 2021

@author: Yu Du
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
        st.write('Dear, **'+user_input+'**')
        st.write('')
        st.write('This is your story with **Conservation-360**')
        st.write('In **2020**, you donated ** $'+
                 str(list(donor[donor['Donor']==user_input]['Donation amount'])[0])+
                 '** to us. Your kind promoted the environment in Madagascar, and it was highly appreciated!')
        st.write('There are **%d** donors along with you in **2020**. '%len(donor['Donor'].unique())+
                 'They are as kind as you. Thanks to your warm-hearted donate, our world is getting better.'+
                 "A person's power may be limited. But when the power of many kind people is connected together, it is enough to have an impact on the world")
        st.write('Start your journey in **2021** with us **RIGHT NOW** by clicking the following link:')
        st.write('http://url.com')


        fig = px.scatter_mapbox(donor, lat='Latitude', lon='Longitude', hover_name="Donor",hover_data=['Date planted','Family','Genus','Species'],
                       zoom=17,color = 'label',title='Here is <b>your</b> tree!')
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"l":0,"b":0})
        fig.update_layout(width=1000,height=600)
    
        st.write(fig)
        
        
        
    if select_don == "Donor's trees":
        fig = px.scatter_mapbox(donor, lat='Latitude', lon='Longitude', hover_name="Donor",hover_data=['Date planted','Family','Genus','Species'],
                       zoom=17,color = 'Family',title='What kinds of <b>trees</b> do <b>donors</b> plant')
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(width=1000,height=600)
        
    
        st.write(fig)
        donor_agg = donor.groupby('Family').count()['Donor'].reset_index()
        fig = px.pie(donor_agg,values='Donor',names='Family',labels={'Donor':'Number of Donors'},
                     title="Donor's choice of diffrent trees")
        fig.update_traces(textposition='outside', textinfo='percent+label',marker_colors=['lightblue','purple','orange','blue','red','lightgreen'])
        fig.update_layout(showlegend=False,width=1000,title_x=0.5)
        
        st.write(fig)
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
        trees_agg = trees.groupby('Status').count()['Height_cm'].reset_index()
        trees_agg.columns=['Status','number of tree']
        fig = px.pie(trees_agg,values='number of tree',names='Status',
                     labels={'number of tree':'number of tree'},title = 'Status of trees planted in other years')
        fig.update_traces(textposition='inside', textinfo='percent+label',marker_colors=['green','lightgrey'])
        fig.update_layout(showlegend=False,width=1000,title_x=0.5)
        st.write(fig)
        

if select=='Conservation-360':
    st.markdown('## Conservation-360')
    st.markdown('### Conservation-360 always work with you!!')
    select_con = st.selectbox(
    'See our accomplishment',
    ('natural observation','seed collection process', 'transplanting process')
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
                       zoom=10,color='taxon_kingdom_name',title='Natural Observations in this Region')
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
        st.write(naturalist_data.head())
        
        st.write('**Step1:Input the common name, get the scientific name**')
        user_input0 = st.text_input("Please input the common name", 'Small-toothed Sportive Lemur')
        st.write('Scientific name of %s'%user_input0+' is '+"**'"+list(naturalist_data['scientific_name'][naturalist_data['common_name']==user_input0])[0]+"'**")
        st.write('**Step2:Copy its name and paste in the below box to show it!!**')
        user_input = st.text_input("Please input the scientific name", 'Lepilemur microdon')
        st.write('See **%s** in the following link!'%user_input)
        for i in naturalist_data['image_url'][naturalist_data['scientific_name']==user_input]:
            st.write(i)
            if '?' in i:
                st.image(i[:i.find('?')])
            else:
                st.image(i)
        
    if select_con == 'seed collection process':
        st.markdown(seed_txt)
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
    select_mdg = st.selectbox('About Mdagascar',('Income','Environment'))
    if select_mdg == 'Income':
        wdbincome = pd.read_csv(r'./madagascar/Income per capita WB.csv').iloc[:2,[0]+list(range(4,22))]
        wdbincome.columns = ['country']+[i[i.find('20'):i.find('20')+4] for i in wdbincome.columns[1:]]
        wdbincome = wdbincome.set_index('country').T
        fig = go.Figure(data=[
            go.Scatter(name='United States', x=wdbincome.index, y=wdbincome['United States']),
            go.Scatter(name='Madagascar', x=wdbincome.index, y=wdbincome['Madagascar'])
            ])
        fig.update_layout(title='National Income of USA and Madagascar per Capita(USD)',title_x=.5,width=1000,xaxis_title='Year')
        st.write(fig)
        income = pd.read_excel(r'./madagascar/Localized (ranomafana) Households Income.xls').iloc[3:9,1:7]
        income = income.reset_index()
        income.columns = list(income.iloc[0][:-1])+['Yearly Income(USD)']
        income = income.iloc[1:,1:].sort_values(by='Yearly Income(USD)',ascending=False)
        fig = px.bar(income, x='Crops', y='Yearly Income(USD)',title='Localized (ranomafana) household income mainly depends on <b>coffee')
        fig.update_traces(marker_color=['red','blue','blue','blue','blue'])
        fig.update_layout(title_x=0.5,width=1000)
        st.write(fig)
    if select_mdg == 'Environment':
        mdg = [pd.read_excel(r'./madagascar/MDG.xlsx',sheet_name=i) for i in range(1,7)]
        mdg = [i[i['threshold']==10] for i in mdg]
        mdg_con = mdg[:3]
        con_select = [0]+list(range(6,len(mdg_con[0].columns)))
        mdg_con = [i.iloc[:,con_select] for i in mdg_con]
        mdg_sub = mdg[3:]
        sub_select = [i+1 for i in con_select]
        mdg_sub = [i.iloc[:,sub_select] for i in mdg_sub]
        mdg = mdg_sub+mdg_con
        col_name = ['Area']+[i[i.find('20'):i.find('20')+4] for i in mdg_sub[0].columns[1:]]
        for i in mdg:
            i.columns = col_name
        mdg = [i.set_index('Area').T for i in mdg]
        mdg = [pd.concat([mdg[i],mdg[i+3]],axis=1) for i in range(3)]
        mdg_region = {i:pd.concat([mdg[0][i],mdg[1][i],mdg[2][i]],axis=1) for i in mdg[0].columns}
        for i in mdg_region:
            mdg_region[i].columns = ['Hectares of tree cover loss','Metric tonnes of aboveground biomass loss','Metric tonnes of CO2 emissions']
            mdg_region[i]['Tree cover loss index'] = round(100*mdg_region[i]['Hectares of tree cover loss']/mdg_region[i]['Hectares of tree cover loss'][0],2)
            mdg_region[i]['Biomass loss index'] = round(100*mdg_region[i]['Metric tonnes of aboveground biomass loss']/mdg_region[i]['Metric tonnes of aboveground biomass loss'][0],2)
            mdg_region[i]['CO2 emission index'] = round(100*mdg_region[i]['Metric tonnes of CO2 emissions']/mdg_region[i]['Metric tonnes of CO2 emissions'][0],2)
        region_list = list(mdg_region.keys())
        region = st.selectbox('The Region You Want to Compare with',region_list)
        fig = make_subplots(rows=1, cols=2,subplot_titles=['Fianarantsoa',region])
        for i in mdg_region['Fianarantsoa'].columns[-3:-1]:
            fig.add_trace(
                go.Scatter(x=mdg_region['Fianarantsoa'].index,y= mdg_region['Fianarantsoa'][i],name=i),
                row=1, col=1)

        for i in mdg_region[region].columns[-3:-1]:
            fig.add_trace(
                go.Scatter(x=mdg_region[region].index,y= mdg_region[region][i],name=i),
                row=1, col=2)
        fig.update_layout(title='Comparison of <b>Fianarantsoa</b> and <b>'+region,legend=dict(orientation="h",x=0.1),
            xaxis=dict(title='Year',nticks=5),xaxis2=dict(title='Year',nticks=5),
            yaxis_title='Index',yaxis2_title='Index',width=1000)
        st.write(fig)
    
    




