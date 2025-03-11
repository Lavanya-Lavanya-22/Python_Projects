alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text,shift_num):
    cipher_text=""
    for i in plain_text:
        if i in alpha:
            pos=alpha.index(i)
            new_pos=(pos+shift_num)%26
            cipher_text+=alpha[new_pos]   
        else:
            cipher_text+=i
    print(f" here is the text after encryption : '{cipher_text}'")
           
def decryption(cipher_text,shift_num):
    plain_text=""
    for i in cipher_text:
        if i in alpha:
            pos=alpha.index(i)
            new_pos=(pos-shift_num)%26
            plain_text+=alpha[new_pos]   
        else:
            plain_text+=i
    print(f" here is the text after dencryption : '{plain_text}'")
flag=False
while not flag:
    ask=input("Type 'encrypt' for encryption Type 'decrypt' for decryption :  ")   
    user=input("enter the message : ")
    shift=int(input("enter the shift number : "))
    if ask.lower()=="encrypt":
        encryption(plain_text=user,shift_num=shift)
    elif ask.lower()=="decrypt":
        encryption(user,shift)
    play_again=input("'Yes' to continue ,'No to exit  : ")
    if play_again.lower()=='no':
        flag=True
        print("Bye")
