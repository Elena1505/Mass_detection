import pandas as pd 
import os 
import matplotlib.pyplot as plt 
import seaborn as sns 
from pandas import DataFrame


def load_data(file_path:str) -> DataFrame:
    train_df = pd.read_csv(file_path)
    print(f'Le dataset contient: {train_df.shape[0]} lignes et {train_df.shape[1]} colonnes.')
    return train_df


def explore_data(df:DataFrame): 
    print(df.info())
    print(df.head())

    