import pandas as pd


def check_uniqueness(df: pd.DataFrame, columns: list[str]) -> bool:
    return df[columns].duplicated().any()

dataset = pd.read_csv("dataset.csv")

columns = list()
current = "-"
while current.lower() != "end" and current != "":
    if current != "-": columns.append(current)
    current = input("Enter a column name: ")

print(check_uniqueness(dataset, columns))
