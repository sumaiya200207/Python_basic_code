num = input("Enter a number: ")
l = len(num)
sum = 0
for x in range(l):
    sum = sum + int(num[x])
print("The sum of the number: " +str(sum))