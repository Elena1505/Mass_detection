from tensorflow.keras.preprocessing.image import ImageDataGenerator
from pandas import DataFrame

def get_image_generator(): 
    return ImageDataGenerator(
        samplewise_center=True, 
        samplewise_std_normalization=True)


def preprocess_images(df:DataFrame, file_path:str):
    image_generator = get_image_generator()
    generator = image_generator.flow_from_dataframe(
        dataframe = df, 
        directory = file_path, 
        x_col = 'Image',
        y_col = ['Mass'],
        class_mode = 'raw',
        batch_size = 1,
        shuffle = False, 
        target_size = (320, 320)
    )
    return generator


