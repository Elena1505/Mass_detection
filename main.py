from src.data_loader import load_data, cleaned_data, explore_data, visualize_sample_images

def main():
    csv_path = "/home/lelou1505/DS/mass_detection/data/train-small.csv"
    image_path = "/home/lelou1505/DS/mass_detection/data/image"
    output_path = "/home/lelou1505/DS/mass_detection/reports"
    df = load_data(file_path=csv_path)
    #df = cleaned_data(df=df)
    explore_data(df)
    visualize_sample_images(df=df, file_path=image_path, num_images=9, output_path=output_path)


if __name__ == "__main__":
    main()