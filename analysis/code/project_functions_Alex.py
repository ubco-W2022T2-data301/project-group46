import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_process(url_or_path_to_csv_file):
    yearRating_NF=(
    pd.read_csv(url_or_path_to_csv_file)
    .loc[lambda x: x['rating']!='66 min']
    .loc[lambda x: x['rating']!='74 min']
    .loc[lambda x: x['rating']!='84 min']
    .loc[lambda x: x['rating']!='UR']
    .loc[lambda x: x['rating']!='NR']
    .loc[lambda x: x['rating']!='NC-17']
    .loc[lambda x: x['rating']!='TV-Y7-FV'] 
    .drop(['show_id','type','title','director','cast','country','date_added','duration','listed_in','description'],axis=1)
    .dropna()) 
    return yearRating_NF