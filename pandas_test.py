import pandas as pd


def load_csv(file_path):
    return pd.read_csv(file_path)


def save_to_active_dict(dataframe):
    active = {}
    for index in dataframe["Active Minutes"].index:
        if dataframe["Active Minutes"].iloc[index] > 100:
            active[index] = dataframe["Active Minutes"].iloc[index]
    return active


def main():
    df = load_csv("dataset.csv")
    print(df.head(50))
    print(df[["Date", "Calories (kcal)", "Distance (m)"]])
    active = save_to_active_dict(df)
    print(active)


if __name__ == "__main__":
    main()
