def factorial(n):
    if(n == 0 or n == 1):
        return 1  
    
    return n * factorial(n - 1) 

n = (int(input("Enter a number to find its factorial: ")))

print(f"the factorial of this number is:", factorial(n))