n = int(input("Enter a starting number :"))
m = int(input("Enter a ending number: "))

res = ""

for i in range(n,m+1):
    #logic for prime numbers
    flag = 1
    for j in range(2,i):
        if i%j ==0:
            flag = 0
            break
        else:
            continue

    if(flag ==1):
        #print(i)
        res = res + str(i)+ ", "
    else:
        pass

print(res)