import pandas as pd
import json

users = int(input("enter no.of passcodes: "))
lst = []
dict = {}
fields = ["name","username","password"]
df = pd.DataFrame(columns = fields)


def validate_name():
    name = input("enter name:")
    name = check_empty_name(name)

    # names_list = []
    if df.empty:
        return name
    else:
        lst_temp = []
        for value in df.values:
            if name == value[0]:
                lst_temp.append(name)
        if name in lst_temp:
            print("Name already exists.Please enter different name..!")
            name = validate_name()
        # return name
        else:
            # print("new name:" + name)
            return name
    return name

def check_empty_name(name_input):
    var1 = name_input
    # print(var1)
    if var1 is not None and var1 != '':
        return var1
    else:
        print("name cannot be empty please enter valid name")
        var1 = check_empty_name(input("enter name:"))
    return var1

for user in list(range(users)):
    # print(user)
    dict = {'name': validate_name(), 'username': input("enter username:"), 'password': input("enter password:")}
    # dict["name"] = validate_name()
    df = df.append(dict, ignore_index=True)
# print(df)


result = df.to_json(orient="index")
data = json.loads(result)

with open('data_json.json', 'w+') as f:
    json.dump(data,f, indent=4)