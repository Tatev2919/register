import re

users = {1: {"userName": 'John', 'passwd': 'johnjames97'},
         2: {'userName': 'Jane', 'passwd': 'jane9815'}};

name = input("Type your name")
while (re.match("^[ a-zA-Z0-9_.-]+$", name) == None):
    name = input("Type your name correctly")

passwd = input("Type your passwd")
while (re.match(r'[A-Za-z0-9@#$%^&+=]{5,}', passwd) == None):
    passwd = input("Type your passwd correctly")
changeVal = 0

regOrLog = input("Registration or Login ? // if registration then type 0 ,else 1 ")
print("enter 0 or 1")
while(regOrLog not in ('0','1')):
    regOrLog = input("Registration or Login ? // if registration then type 0 ,else 1 ")

if regOrLog == '1':
    flag = False
    for key in users.keys():
        print(users[key])
        print(users[key].get("userName"))
        if name == users[key].get('userName'):
            if passwd == users[key].get('passwd'):
                print("Congrats you've logged successfully!!")
                flag = True
                break
    if (flag == False):
        print("Maybe you've enter wrong userName or passwd.Can I register you as new user ?")
        changeVal = input("enter yes or no ? ")
        while (changeVal not in ('yes', 'no')):
            print("your input is not correct")
            changeVal = input("enter yes or no ? ")
        if (changeVal == "yes"):
            regOrLog = '0'
        if (changeVal == "no"):
            print("Byee!")
if regOrLog == '0':
    user1 = dict({'userName': name, 'passwd': passwd});
    users['4'] = (dict(user1))
    for key1 in users.keys():
        print(users[key1])
