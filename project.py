#!/usr/bin/env python
# coding: utf-8

# In[301]:


import pandas as pd
import psycopg2


# In[302]:


def create_database():
    # Connect to the default 'postgres' database
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=root")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # Create a new database 'accounts2'
    #cur.execute("DROP DATABASE accounts2")
    cur.execute("CREATE DATABASE accounts15")

    # Close the connection to the default database
    conn.close()

    # Connect to the newly created 'accounts2' database
    conn = psycopg2.connect("host=localhost dbname=accounts15 user=postgres password=root")
    cur = conn.cursor()

    return cur, conn


# In[303]:


AccountsCountry = pd.read_csv("Wealth-AccountsCountry.csv")


# In[304]:


AccountsCountry.head()


# In[305]:


AccountsCountry=AccountsCountry[['Code','Short Name','Table Name','Long Name','Currency Unit']]


# In[306]:


AccountsCountry.head()


# In[307]:


AccountsData=pd.read_csv("Wealth-AccountData.csv")


# In[308]:


AccountsData=AccountsData[['Country Name','Country Code','Series Name']]


# In[309]:


AccountSeries=pd.read_csv("Wealth-AccountSeries.csv")


# In[310]:


AccountSeries.columns


# In[311]:


AccountSeries=AccountSeries[['Code','Topic','Indicator Name','Long definition']]


# In[312]:


AccountSeries.head()


# In[313]:


cur,conn=create_database()


# In[314]:


songplay_table_create = ("""CREATE TABLE IF NOT EXISTS accountsdata(
country_name VARCHAR,
country_code VARCHAR,
indicator_name VARCHAR
)""")


# In[315]:


try:
    cur.execute(songplay_table_create)
    conn.commit()  # Commit to make the changes permanent
    print("Table 'accountsdata' created successfully!")
except Exception as e:
    print("Error creating table:", e)


# In[316]:


accounts_datatable_create = ("""CREATE TABLE IF NOT EXISTS accountscountry(
country_code VARCHAR,
short_name VARCHAR,
long_name VARCHAR,
table_name VARCHAR,
currency_unit VARCHAR
)""")

cur.execute(accounts_datatable_create)
conn.commit()


# In[317]:


accounts_seriestable_create = ("""CREATE TABLE IF NOT EXISTS accountseries(
code VARCHAR,
topic VARCHAR,
indicator_name VARCHAR,
long_definition VARCHAR
)""")

cur.execute(accounts_seriestable_create)
conn.commit()


# In[318]:


accounts_country_table_insert=("""
INSERT INTO accountscountry(
country_code,
short_name,
long_name,
table_name,
currency_unit)
VALUES (%s,%s,%s,%s,%s)
""")


# In[319]:


for i,row in AccountsCountry.iterrows():
    cur.execute(accounts_country_table_insert,list(row)) 


# In[320]:


conn.commit()


# In[321]:


accounts_series_table_insert = """
INSERT INTO accountseries(
    code,
    topic,
    indicator_name,
    long_definition)
VALUES (%s, %s, %s, %s)
"""


# In[322]:


for i,row in AccountSeries.iterrows():
    cur.execute(accounts_series_table_insert,list(row))


# In[323]:


conn.commit()


# In[324]:


accounts_data_table_insert=("""
INSERT INTO accountsdata(
country_name,
country_code,
indicator_name
)
VALUES (%s,%s,%s)
""")


# In[325]:


for i,row in AccountsData.iterrows():
    cur.execute(accounts_data_table_insert,list(row))


# In[326]:


AccountsData.head()


# In[327]:


conn.commit()


# In[ ]:




