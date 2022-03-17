users = int(input("enter no.of passcodes: "))
lst = []
dict = {}

def validate_name():
    name = input("enter name:")
    name = check_empty_name(name)

    # names_list = []
    if len(lst) == 0:
        return name
    else:
        lst_temp = []
        for value in lst:
            if name == value["Name"]:
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
    dict = {'Name': validate_name(), 'username': input("enter username:"), 'password': input("enter password:")}
    # dict["name"] = validate_name()
    lst.append(dict)
print(lst)



search = input("enter search value: ")

for value in lst:
    if search in value["Name"]:
        print("Name: " , value['Name'])
        print("username: " , value['username'])
        print("password: " , value['password'])
        print("\n")


