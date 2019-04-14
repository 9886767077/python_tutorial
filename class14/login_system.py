import mysql.connector

def createNewUser(user_tuple):
    #print(user_tuple)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="python12",
        database="mydb1"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address, phone_no, pwd, data) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, user_tuple)

    mydb.commit()
    #print(type(mycursor.rowcount))
    print(mycursor.rowcount, "record inserted.")
    if mycursor.rowcount ==1 :
        return 1
    else :
        return -1

def checkLogin(phone, pwd):
    res = ""
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="python12",
        database="mydb1"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM customers WHERE phone_no ='{}'".format(phone)
    #sql = "SELECT * FROM customers WHERE name ='mukund'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    #print(type(myresult))
    #print(myresult)

    #for x in myresult:
    #    print(type(x))
    #    print(x)
    if myresult:
        stored_pwd = myresult[0][3]
        if stored_pwd == pwd:
            res = myresult[0][4]
        else:
            res = "-2"
    else:
        res = "-1"

    return res

def mainFunction():
    c = input("1. Login 2. Sign Up")
    if c =='1':
        ph_no = input("Enter phone no :")
        pwd = input("Enter password :")
        data = checkLogin(ph_no, pwd)
        if data == '-1':
            print("You are a first time user. Please signup")
        elif data == '-2':
            print("Sorry password incorrect !")
        else:
            print("Congrats login successful. Your personal data is printed below:")
            print(data)
    elif c == '2':
        name = input("Enter your name :")
        addr = input("Enter your address :")
        ph_no = input("Enter your phone no :")
        pwd = input("Enter password :")
        data = input("Enter you personal data :")
        user_tuple = (name, addr, ph_no, pwd, data)
        res = createNewUser(user_tuple)
        if res ==1 :
            print("Record successfully inserted . You can login now")
        else:
            print("Some error occured while inserting to database ")
    else:
        print("Wrong input !!!")

def runMainFunctionInWhileLoop():
    while(True):
        choice = input("Want to login or sign up ? (Enter -1 to exit)")
        if choice == '-1':
            break
        else:
            mainFunction()

runMainFunctionInWhileLoop()