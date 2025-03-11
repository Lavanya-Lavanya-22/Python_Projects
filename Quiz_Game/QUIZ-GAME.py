
import QUIZ_DATABASE

print("\nWelcome to my Quiz Game\n\n*****************************************")

def check_answer(user,correct_answer):
    
        if correct_answer==user:
            return True
        else:
            return  False  

questions=(QUIZ_DATABASE.question_bank)
score=0     
for i in range(len(questions)):
    print(questions[i]["text"])
    user=input("Enter Your answer (a/b/c/d):  ")
    is_correct=check_answer(user,questions[i]["answer"])
    if is_correct==True:
        score+=1
        print(f"\nCorrect answer \nThe current score is : {score}/5 \n")
    else:
        print(f"\nIncorrect Answer \nThe correct answer is :{questions[i]["answer"]} ")
        
    print("\n*************************************************************************\n")

print("Your Score is ",{score})
total_score=(score/5)*100
print(f"Total score is :{total_score}")
        
    

