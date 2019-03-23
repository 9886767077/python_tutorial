para = input("Enter a string :")
mychar = input("Enter a char :")
index =0
for c in para:
    if c== mychar:
        print(index)
        break

    index = index + 1

for i in range(0, len(para)):
    if para[i] == mychar:
        print(i)
        break

