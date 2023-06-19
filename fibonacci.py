n = int(input("Enter range: "))
a = 0
b = 1
print(0)
print(1)
for x in range(3, n+1):
    r = a + b
    print(r)
    a = b
    b = r
print("Fibonacci done!")
