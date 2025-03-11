
#write a program to check the validity of the passeord entered by the user
"""
minimum 7 characters
maximum 20 characters
Atleast 1 letter between[A-z] and letter between[a-z]
Atleast 1 number
Atleast 1 character from[$#@!]
"""
import re

pwd=input("enter the paassword : ")
pwd_len=len(pwd)
is_valid=False
while True:
    if pwd_len < 7 or pwd_len>20:
        print("Password must be at least 7 characters long")
        break 
    elif not re.search('[A-Z]',pwd):
        print("Password must contain at least one uppercase letter")
        break
    elif not re.search('[a-z]',pwd):
        print("Password must contain at least one lowercase letter")
        break
    elif not re.search('[0-9]',pwd):
        print("Password must contain at least one digit")
        break
    elif not re.search('[$#@!%^&*]',pwd):
        print("Password must contain at least one special character (@, #, $, %, ^, &, or !)")
        break
    elif re.search('\s',pwd):#check whitespace
        print("Password should not contain spaces.")
        break
        #or
    elif pwd==" ":#also to check whitespace 
        print("Password should not contain spaces.")
        break
    else:
        is_valid=True
        break
if is_valid==True:
    print("Password is valid")
else:
    print("Password is not valid")
    

