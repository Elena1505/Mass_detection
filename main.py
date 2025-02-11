from src.data_loader import load_data

def main():
    csv_path = "/home/lelou1505/DS/mass_detection/data/train-small.csv"
    df = load_data(csv_path=csv_path)


if __name__ == "__main__":
    main()