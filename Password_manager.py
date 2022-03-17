users = int(input("enter no.of passcodes: "))
lst = []
dict = {}

for user in list(range(users)):
    # print(user)
    dict = {'Name': input("enter name:"), 'username': input("enter username:"), 'password': input("enter password:")}
    lst.append(dict)

search = input("enter search value: ")

for value in lst:
    if search in value["Name"]:
        print("Name: " , value['Name'])
        print("username: " , value['username'])
        print("password: " , value['password'])
        print("\n")


