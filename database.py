#!/usr/bin/env python
# coding: utf-8

# # Saving Data to CSV and Excel

# In[7]:


import urllib.request
from urllib.request import urlopen 
from bs4 import BeautifulSoup as soup
import csv


# In[8]:


filename = 'music.csv'
f = open(filename,'w',newline = '')
music = csv.writer(f)


html = urlopen('https://en.wikipedia.org/wiki/List_of_largest_recorded_music_markets')
bsobj = soup(html.read())
tbody = bsobj('table',{'class':'wikitable plainrowheaders sortable'})[0].findAll('tr')
xl = []
for row in tbody:
    cols = row.findChildren(recursive = False)
    cols = [element.text.strip() for element in cols]
    music.writerow(cols)
    xl.append(cols)
    print(cols)


# In[6]:


import os
os.getcwd()


# In[9]:


xl


# ## Creating pandas dataframe and saving to excel

# In[10]:


import pandas as pd
df = pd.DataFrame(data = xl)
df


# In[11]:


df.to_excel('world_music.xlsx', index=False,header = False)
print('Spreadsheet saved.')

