# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:17:57 2019

@author: khushal
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
#ax=plt.gca()
#plt.figure(dpi=250,figsize=(250,200))

pd.set_option('display.max_columns',1000)
path_of_input_file = "C:/Users/khushal/Documents/Python Scripts/Rape_cases_in_India_2015.xlsx"
input_data_df = pd.read_excel(path_of_input_file,sheet_name='Rape_cases_in_India_2015')
indian_states_df = pd.read_excel(path_of_input_file,sheet_name='States')
input_data_df.sort_values(by='Number of Victims (Total Rape Cases) - Total Victims')

print(input_data_df)

print("--" * 50)
india_crime_data_by_state = pd.merge(left=input_data_df,right=indian_states_df,left_on='State/UT',right_on='State/UT')
state_df = india_crime_data_by_state['State/UT']

#incest_rape_case_reported_df = input_data_df['Incest Rape - Number of Cases Reported']
Number_of_Victims_under_Incest_Rape_Cases = india_crime_data_by_state['Number of Victims under Incest Rape Cases - Total Victims']
Number_of_Victims_under_Other_than_Incest_Rape_Cases = india_crime_data_by_state['Number of Victims under Other than Incest Rape Cases - Total Victims']
Number_of_Victims_Total_Rape_Cases_Total_Victims = india_crime_data_by_state['Number of Victims (Total Rape Cases) - Total Victims']

#print("india_crime_data_by_state = \n",india_crime_data_by_state,"\n --" * 60)
#print(Number_of_Victims_Total_Rape_Cases_Total_Victims)

ax = input_data_df.plot(kind='bar',x='State/UT',y='Number of Victims (Total Rape Cases) - Total Victims',label='Rape_cases_in_India_2015')

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.grid()
plt.show()
#plt.savefig('C:/Users/khushal/Documents/Python Scripts/Rape_cases_in_India_2015.png',dpi=500)

path_of_input_file1 = "C:/Users/khushal/Documents/Python Scripts/datafile.xls"
df = pd.read_excel(path_of_input_file1,sheet_name='Worksheet')
print(df)
print("--" * 50)

max_2014 = max(df['Year-2014'])
max_2015 = max(df['Year-2015'])
max_2016 = max(df['Year-2016'])

max_2014_row = df.loc[df['Year-2014'] == max_2014]
max_2015_row = df.loc[df['Year-2015'] == max_2015]
max_2016_row = df.loc[df['Year-2016'] == max_2016]

print(max_2014_row,'\n',max_2015_row,'\n',max_2016_row)

# Setting the positions and width for the bars
pos = list(range(len(df['Year-2014']))) 
width = 0.25 
    
# Plotting the bars
fig, ax = plt.subplots(figsize=(20,40))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos, 
        #using df['pre_score'] data,
        df['Year-2014'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.9, 
        # with color
        color='#EE3224', 
        # with label the first value in first_name
        label=df['State/UT'][0]) 

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        #using df['mid_score'] data,
        df['Year-2015'],
        # of width
        width, 
        # with alpha 0.5
        alpha=0.9, 
        # with color
        color='#F78F1E', 
        # with label the second value in first_name
        label=df['State/UT'][1]) 

plt.bar([p + width*2 for p in pos], 
        #using df['post_score'] data,
        df['Year-2016'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.9, 
        # with color
        color='#FFC222', 
        # with label the third value in first_name
        label=df['State/UT'][2]) 

# Set the y axis label
ax.set_ylabel('Number of Rape Cases')

# Set the chart's title
ax.set_title('State/UTwise rape cases from 2014 to 2016')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['State/UT'],rotation=90)

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)

if max_2014 > max_2015 and max_2014 > max_2016:
    plt.ylim([0, max(df['Year-2014'])])# + df['Year-2015'] + df['Year-2016'])] )
elif max_2015 > max_2014 and max_2015 > max_2016:
    plt.ylim([0, max(df['Year-2015'])])# + df['Year-2015'] + df['Year-2016'])] )
else:
    plt.ylim([0, max(df['Year-2016'])])# + df['Year-2015'] + df['Year-2016'])] )

# Adding the legend and showing the plot
plt.legend(['Year-2014', 'Year-2015', 'Year-2016'], loc='upper left')

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.025, p.get_height() * 1.005))

 
plt.grid()
plt.show()
#plt.savefig('C:/Users/khushal/Documents/Python Scripts/Rape_cases_in_India_2014_to_2016.png',dpi=500)