para = input("Enter a string :")
mychar = input("Enter a char :")

index = -1
for i in range(0,len(para)):
    if(para[i]==mychar):
        index = i

if(index == -1):
    print("Sorry couldn't find the character")
else:
    print("Last occurance at index {}".format(index))