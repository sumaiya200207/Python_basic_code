from fractions import gcd

num1 = int(input("Number1 = "))
num2 = int(input("Number2 = "))

if gcd(num1, num2) == 1:
    print("The numbers are coprime")
else:
    print("Not coprime")
