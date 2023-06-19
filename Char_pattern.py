n = input("Enter a string:" )
len = len(n)
for i in range(len):
    for j in range(i+1):
       print(n[j], end="")
    print()