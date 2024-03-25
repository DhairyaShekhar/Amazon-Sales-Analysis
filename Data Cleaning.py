# Import pandas library for data cleaning
import pandas as pd

# Load the dataset you want to clean
df = pd.read_csv(r"<<Enter the path to your dataset here>>")

# Data cleaning 
df.dropna(inplace=True)  #Handles missing values
df.drop_duplicates(inplace=True) #Removes any duplicate values

# Saving the cleaned dataset
cleaned_file_path = '<<Enter the name you want to save the cleaned dataset as>>'
df.to_csv(cleaned_file_path, index=False)

# Downloading the cleaned dataset
from IPython.display import FileLink
display(FileLink(cleaned_file_path))
