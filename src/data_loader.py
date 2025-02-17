import pandas as pd 
import os 
import matplotlib.pyplot as plt 
import numpy as np 
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


def visualize_sample_images(df:DataFrame, file_path:str, num_images:int, output_path:str):
    images = df['Image'].values
    random_images = [np.random.choice(images) for i in range(num_images)]
    
    plt.figure(figsize=(20, 10))
    for i in range(num_images):
        plt.subplot(3, 3, i+1)
        image = plt.imread(os.path.join(file_path, random_images[i]))
        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.tight_layout()
    plt.savefig(os.path.join(output_path, "sample_image"))

