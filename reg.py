import re
users  = dict([{"userName":'John','passwd':'john97'},
               {'userName':'Jane','passwd':'jane98'}])

name = input("Type your name")

while (re.match("^[ a-zA-Z0-9_.-]+$",name) == None):
    name = input("Type your name correctly")

passwd = input("Type your passwd")
while (re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', passwd) ==None):
    passwd = input("Type your passwd correctly")
changeVal = 0
Register = 0
Login = 1
flag = False
regOrLog = input("Registration or Login ? // if registration then type 0 ,else 1 ")
if(regOrLog):
    flag = True
    for i in users.get("userName"):
        if (i == name):
            for j in users.get("passwd"):
                if (j == passwd):
                    print("Congrats you've logged successfully!!")
                    flag = True
                    break
            if (flag):
                break
    print(flag)
    if(flag == False):
        print("Maybe you've enter wrong userName or passwd.Can I register you as new user ?")
        changeVal = input("enter yes or no ? ")
        if(changeVal == "yes"):
            regOrLog = 0
        while (changeVal!= "yes" & changeVal!= "no"):
            inp = input("your input is not correct")
            changeVal = input("enter yes or no ? ")
