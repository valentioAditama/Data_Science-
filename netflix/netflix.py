import pandas as pd

df = pd.read_csv('./netflix_titles.csv')
get_money = pd.Series(["money heist"], name="title")
print(get_money)