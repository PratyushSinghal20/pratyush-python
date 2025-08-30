n = int(input("Enter a number: "))

sum_even = 0
sum_odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("Sum of Even numbers up to", n, "=", sum_even)
print("Sum of Odd numbers up to", n, "=", sum_odd)
