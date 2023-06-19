n = int(input("Enter a number to check: "))
if n>1:
    for x in range(2, n):
        if n % x == 0:
            print("Not prime")
            break
    else:
        print("Yes prime")
else:
    print("Not prime")
