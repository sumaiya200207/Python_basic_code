num = int(input("Enter range: "))

for n in range(1, num+1):
    sum = 0
    for x in range(1, n):
        if (n % x) == 0:
            sum = sum + x
    if n == sum:
        print(n)
