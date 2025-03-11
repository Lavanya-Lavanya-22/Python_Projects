

#password generator symbols,alphabets,numbers

    
import random
print("welcome to passord generator...")

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'A','B','C','D','E','F','G','H','I','J','K','L','M']

numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['!','@','#','$','%','^','&']


num=int(input("enter how many  numbers you want : "))#4

alpha=int(input("enter how many aphabets you want : "))#4

symb=int(input("enter how many symbols you want : "))#4

password=[]


for i in range(1,alpha+1):
    char=random.choice(letters)
    password+=char


for j in range (1,num+1):
    char=random.choice(numbers)
    password+=str(char)


for k in range (1,symb+1):
    char=random.choice(symbols)
    password+=char


passw=""
for char in password:
    passw+=char
print(passw)

#output-bdge2908#$#%


random.shuffle(password)


passw=""
for char in password:
    passw+=char
print(passw)

#output-b20g9#8e#$d%