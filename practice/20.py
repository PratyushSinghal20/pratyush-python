num = int(input("Enter a number: "))

# Factorial using for loop
fact_for = 1
for i in range(1, num + 1):
    fact_for *= i
print("Factorial of", num, "using for loop =", fact_for)

# Factorial using while loop
fact_while = 1
i = 1
while i <= num:
    fact_while *= i
    i += 1
print("Factorial of", num, "using while loop =", fact_while)
