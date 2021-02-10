import re

users = [{"userName": 'John', 'passwd': 'johnjames97'}, {'userName': 'Jane', 'passwd': 'jane98'}];

name = input("Type your name")
while (re.match("^[ a-zA-Z0-9_.-]+$", name) == None):
    name = input("Type your name correctly")

passwd = input("Type your passwd")
while (re.match(r'[A-Za-z0-9@#$%^&+=]{5,}', passwd) == None):
    passwd = input("Type your passwd correctly")
changeVal = 0
#flag = False
regOrLog = input("Registration or Login ? // if registration then type 0 ,else 1 ")
print(regOrLog)
if regOrLog == '1':
    flag = False
    for i in users:
        if name in i.get('userName'):
            if passwd in i.get('passwd'):
                print("Congrats you've logged successfully!!")
                flag = True
                break
    print(flag)
    if (flag == False):
        print("Maybe you've enter wrong userName or passwd.Can I register you as new user ?")
        changeVal = input("enter yes or no ? ")
        while (changeVal not in ('yes', 'no')):
            print("your input is not correct")
            changeVal = input("enter yes or no ? ")
        if (changeVal == "yes"):
            regOrLog = 0
        if (changeVal == "no"):
            print("Byee!")
if regOrLog == '0':
    user1 = dict({'userName': name, 'passwd': passwd});
    users.append(dict(user1))
    [print(key, ':', value) for key, value in user1.items()]
