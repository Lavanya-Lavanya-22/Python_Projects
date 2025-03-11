import random
print("press 0 for rock")
print("press 1 for paper")
print("press 2 for scissor")

img=["rock","paper","scissor"]

user=int(input("Enter Ur choice : "))

if user>=3 or user<0:
    print("Enter valid input")

else:
    print(f"Your choice is {img[user]}")
    play=random.randint(0,2)
    

    print(f"Computer choice is {img[play]}")
    if(user==play):
        print("Its draw")
    
    elif(play==1 and user==2) or(user==0 and play==1) or (user==2 and play==0):
        print("you lose")    

    else:
        print("You win")
