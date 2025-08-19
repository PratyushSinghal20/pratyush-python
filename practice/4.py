# factorial of a number using for and while loop
n = int(input("enter the number : "))
fact = 1

for i in range (1,n+1) :
    fact*=i 

    print("factorial of a number is :" ,  fact)