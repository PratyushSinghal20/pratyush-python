# find sum of all odd and even no upto  a number specified by the user

n = int(input("enter a number : "))

sum_even = 0
sum_odd = 0

for i in range(0, n+1) :
    if i % 2 == 0 :
        sum_even += i

    else :
        sum_odd += i

        print("sum of even no is : ",sum_even )

