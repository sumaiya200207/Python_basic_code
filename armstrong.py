import math

num = input()
n = int(num)
count = sum = 0
for x in num:
    count = count + 1
print("We have " +str(count))

for y in num:
    sum = sum + math.pow(int(y), int(count))
print(sum)


