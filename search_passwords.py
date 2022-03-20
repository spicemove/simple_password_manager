import pandas as pd

df_read = pd.read_json('data_json.json')
df = df_read.T


search = input("enter search value: ")

counter = 0

for value in df["name"]:
    if search == value:
        print("name: " , df.iloc[counter]['name'])
        print("username: " , df.iloc[counter]['username'])
        print("password: " , df.iloc[counter]['password'])
        print("\n")
    counter = counter+1




