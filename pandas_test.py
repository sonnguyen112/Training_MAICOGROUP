import pandas as pd


def csv_process():
    df = pd.read_csv("dataset.csv")
    print(df.head(50))
    print(df[["Date", "Calories (kcal)", "Distance (m)"]])
    active = {}
    for index in df["Active Minutes"].index:
        if df["Active Minutes"].iloc[index] > 100:
            active[index] = df["Active Minutes"].iloc[index]

    print(active)


csv_process()
