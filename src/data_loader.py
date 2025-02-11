import pandas as pd 
import os 
import matplotlib.pyplot as plt 
import seaborn as sns 
from pandas import DataFrame


def load_data(file_path:str) -> DataFrame:
    train_df = pd.read_csv(file_path)
    print(f'The dataset contains: {train_df.shape[0]} lines et {train_df.shape[1]} columns.')
    return train_df


def cleaned_data(df:DataFrame) -> DataFrame:
    df = df.drop(columns=['Image','PatientId'])
    columns = df.keys()
    for column in columns:
        print(f'The class {column} has {df[column].sum()} samples.')
    return df


def explore_data(df:DataFrame): 
    print(df.info())
    print(df.head())


