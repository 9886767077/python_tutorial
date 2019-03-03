name = input("Enter your name")
address = input("Enter you address")
Salary = input("What is your monthly salary")
Spent = input("How much you spent this month")

balance = float(Salary) - float(Spent)

message = "Hi {0}, from {1}, has salary {2}, and spent {3}, remaining balance is {4}".format(name,address,Salary,Spent,balance)

print (message)