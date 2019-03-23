para = input("Enter a string :")

count = 0
for c in para:
    print(c)
    if c=='a' or c=="e" or c =="i" or c=="o" or c=="u":
        count = count +1

print("Number of vovels are {}".format(count))

count = 0
for i in range(0,len(para)):
    print(para[i])
    c = para[i]
    if c in "aeiou":
        count = count +1

print("Number of vovels are {}".format(count))