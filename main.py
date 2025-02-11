from src.data_loader import load_data, explore_data

def main():
    csv_path = "/home/lelou1505/DS/mass_detection/data/train-small.csv"
    df = load_data(file_path=csv_path)
    explore_data(df)


if __name__ == "__main__":
    main()