#Question 1 calculator

def add(n1,n2):                       #here arguements can also be given of any other names like x,y etc.
    ans= n1+n2
    return ans
def sub(n1,n2):
    ans=n1-n2
    return ans
def mul(n1,n2):
    ans=n1*n2
    return ans
def div(n1,n2):
    ans=n1/n2
    return ans
while True:
    print("Enter to choose: 1)Addition\t2)Substraction\t3)Multiplication\t4)Divison")
    print("Enter 1 for Addition\tEnter 2 for Substraction\tEnter 3 for Multiplication\tEnter 4 for Division")
    op=int(input())
    n1=int(input("Enter first number"))
    n2=int(input("Enter second number"))
    if op==1:
        result=add(n1,n2)
        print("Addition of",n1,"and",n2,"is:", result)
        n=input("You want to continue? Y/N")
        if n=="N" or n=="n":
            print("\nThanks")
            break
    elif op==2:
        result=sub(n1,n2)
        print("Substraction of",n1,"and",n2,"is:", result)
        n=input("You want to continue? Y/N")
        if n=="N" or n=="n":
            print("\nThanks")
            break
    elif op==3:
        result=mul(n1,n2)
        print("Multiplication of",n1,"and",n2,"is:", result)
        n=input("You want to continue? Y/N")
        if n=="N" or n=="n":
            print("\nThanks")
            break
    elif op==4:
        result=div(n1,n2)
        print("Division of",n1,"and",n2,"is:", result)
        n=input("You want to continue? Y/N")
        if n=="N" or n=="n":
            print("\nThanks")
            break
