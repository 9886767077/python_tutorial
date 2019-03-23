limit=int(input("enter the integer limit: "))
num=int(input("By which num you want to divide: "))
output_string= "Number divisible by {} between 0 to {} are: ".format(num,limit)

for i in range(0,limit+1):
    if(i>=100 and i<=200):
        continue

    if(i%num==0):
        output_string = output_string + str(i) +","

print(output_string)
