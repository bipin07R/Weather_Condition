#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd #Loaded the pandas libery


# In[4]:


data = pd.read_csv("C:/Users/Bipin Rajput/Downloads/1. Weather Data.csv") #data file loaded


# In[5]:


data.head()


# In[6]:


data.shape # its shows the total no of rows and no. of columns of the datafreme


# In[7]:


data.index # This attribute provides the index of the dataframe


# In[57]:


data.columns # It shows the name of each column


# In[9]:


data.dtypes # it shows the data type of each column


# In[10]:


data['Weather'].unique() #In a Column, it shows all the unique values. It can be applied on a 
#single column only, not on the whole dataframe.


# In[11]:


data.nunique() #It shows the total no of unique values in each column. It can be on a single column as well as on whole dataframe.


# In[12]:


data.count() # it shows the total no. of non-values in each column. It can be applied on a single column as well as on whole dataframe.


# In[13]:


data['Weather'].value_counts() # in a cloumn, it shows all the values with their count. It can be applied on single column only.


# In[14]:


data.info() # provides basic information about the dataframe


# In[ ]:





# # Find the all unique Wind Speed Value in the data.

# In[15]:


data.head(2)


# In[16]:


data.nunique()


# In[17]:


data['Wind Speed_km/h'].nunique()


# In[18]:


data['Wind Speed_km/h'].unique() #Anwer


# # Find the number of times when the "weather is exactly clear"

# In[19]:


data.head(1)


# In[20]:


data['Weather'].value_counts()


# In[21]:


#Filtering method
data[data.Weather == 'Clear']


# In[22]:


# groupby()
data.groupby('Weather').get_group('Clear')


# # Find the number of times when the wind speed was exactly 4 km/h

# In[23]:


data.head(1)


# In[24]:


data['Wind Speed_km/h'].nunique()


# In[25]:


data['Wind Speed_km/h'].value_counts()


# In[26]:


data[data['Wind Speed_km/h'] == 4] #answer


# # Find our all the null values in the data

# In[59]:


data.isnull().sum() # There is no any null values in data 


# In[28]:


data.notnull().sum()


# # Rename the column name Weather of the dataframe to Weather Condition.

# In[29]:


data.head(1)


# In[30]:


data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True) # rename the column name


# In[31]:


data.head(1)


# # What is the mean Visibility ?

# In[32]:


data['Visibility_km'].mean()


# # What is the Standard Deviation of presure in this data.

# In[33]:


data['Press_kPa'].std()


# # What is the variance of relative humadity in this data ? 

# In[34]:


data['Rel Hum_%'].var()


# # Find all instances when snow was recorded.

# In[35]:


#values_counts()
data['Weather Condition'].value_counts()


# In[36]:


#Filtering
data[data['Weather Condition'] == 'Snow']


# In[37]:


#str.contains
data[data['Weather Condition'].str.contains('Snow')]


# In[38]:


data


# # Find the instances when Wind speed is above 24 and visibility is 25'.

# In[39]:


data.head(1)


# In[40]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] ==25)]


# # what is the mean value of each of column against each weather condition ?

# In[41]:


data.head(1)


# In[43]:


data.groupby('Weather Condition').mean()


# # What is the Minumumvalue of each column against each Weather condition ?

# In[44]:


data.groupby('Weather Condition').max()


# In[45]:


data.groupby('Weather Condition').min()


# # Show all the records when weather condition is fog.

# In[48]:


data[data['Weather Condition'] == 'Fog']


# # Find the all instances when Weather is clear or visibility is above  40

# In[52]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40 )].head(10)


# # Find all instances when a Weather is clear and relative humidity is grater than 50 or visibility is above 40

# In[53]:


data.head(2)


# In[56]:


data[((data['Weather Condition'] == "Clear") & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




