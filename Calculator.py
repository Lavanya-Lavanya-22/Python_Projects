def add(a,b):
    return a+b
     
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

operation_dict={"+":add,
           "-":sub,
           "*":mul,
           "/":div
}
def calculator():
  
    first=float(input("Enter the first number : "))
    for i in operation_dict:
        print(i)
        
    flag=True

    while flag:
        oper=(input("Pick an operation : "))
        second=float(input("Enter the next number : "))

        cal=operation_dict[oper]
        result=cal(first,second)

        print(f"{first}{oper}{second}={result}")

        again=input(f"Enter 'y'  to continue with {result}   or 'n' to start new calculation  or 'x'  to exit :  ").lower()        
        if again =='y':
            first=result
        elif again == 'n':
            flag=False
            calculator()
        
        elif again =='x':
            flag=False
            print("Bye")
            
calculator()