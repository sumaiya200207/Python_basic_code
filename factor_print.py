num = int(input("Enter an integer number: "))

for x in range(1, num+1):
    if num % x == 0:
        print(x)
