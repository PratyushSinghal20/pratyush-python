
def maximum():


  a = (int(input("enter the number 1 :")))
  b = (int(input("enter the number 2 :")))
  c = (int(input("enter the number 3 :")))


  if(a > b and a > c):
    return a 

  elif(b > a and b > c):
    return b  
  else:
    return c
  
print("the max no is:" , maximum())

