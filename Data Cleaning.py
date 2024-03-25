#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\shekh\Desktop\documents\Sales Insight Project\amazon.csv")

# Data cleaning steps
# Example: Handling missing values
df.dropna(inplace=True)

# Example: Removing duplicates
df.drop_duplicates(inplace=True)

# Save the cleaned dataset
cleaned_file_path = 'cleaned_dataset.csv'
df.to_csv(cleaned_file_path, index=False)

# Download the cleaned dataset
from IPython.display import FileLink
display(FileLink(cleaned_file_path))


# In[ ]:




