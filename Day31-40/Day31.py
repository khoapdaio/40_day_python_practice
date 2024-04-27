#Day 31

# !pip install pandas
# !pip install pygwalker

import pygwalker as pyg
import pandas as pd

data = pd . read_csv ( "/content/drive/MyDrive/Colab Notebooks/menu.csv" )
pyg . walk ( data )

data = pd . read_csv ( "/content/drive/MyDrive/Colab Notebooks/advertising.csv" )
pyg . walk ( data )

data = pd . read_csv ( "/content/drive/MyDrive/Colab Notebooks/worldcities.csv" )
pyg . walk ( data )