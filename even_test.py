number = int(input("Enter a number: "))
count = 0
for x in range(2, number+2, 2):
    count = count + 1
    print(x)
print("We have " +str(count)+ " even numbers")