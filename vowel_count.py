sen = input("Enter a sentence: ")

l = len(sen)
count = 0
for x in range(l):
    if sen[x] == 'a' or sen[x] == 'e' or sen[x] == 'i' or sen[x] == 'o' or sen[x] == 'u' or sen[x] == 'A' or sen[x] == 'E' or sen[x] == 'I' or sen[x] == 'O' or sen[x] == 'U':
        count = count + 1
        print(sen[x]+" ")
print(count)