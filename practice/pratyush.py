def main():
    a = int(input("enter value of a: "))
    b = int(input("enter value of b:"))
    c = int(input("ener value of c: "))
    d = (3*(a+b+c))

    if a == b and b ==c :
        print(f"thrice the sum of a,b and c is {d}")
    
    elif a > b and a > c:
        print(f"a has the greatest value,{a}")

        if b > c:
            print(f"c is the smallest number,{c}")
        elif b == c:
            print(f"b and c are equal,{b}")
        else:
            print(f"b is the smallest number,{b}")

    elif b > c and b > a:
        print(f"b is the greatest number,{b}")

        if c > a:
            print(f"a is the smallest number,{a}")
        elif c == a:
            print(f"a and c are equal,{c}")
        else:
            print(f"c is the smallest number,{c}")

    else:
        print(f"c is the greatest number,{c}")
        
        if b > a:
            print(f"a is the smallest number,{a}")
        elif a == b:
            print(f"both a and b are equal,{b}")
        else:
            print(f"b is the smallest number,{b}")

main()

 
