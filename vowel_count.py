sen = input("Enter a sentence: ")

l = len(sen)
count = 0
for x in range(l):
    if sen[x] == 'a' or sen[x] == 'e' or sen[x] == 'i' or sen[x] == 'o' or sen[x] == 'u':
        count = count + 1
        print(sen[x]+" ")
print(count)