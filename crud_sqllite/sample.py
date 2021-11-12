import sqlite3
con = sqlite3.connect('users.db')
cursor = con.cursor()
print("successfully connected")

# try:
#     con=sqlite3.connect('users.db')
#     print("open database successfull")
# except Exception as e:
#     print("Error for database",str(e))

def insertData(name,age,city):
    qry="insert into users (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("user Details Added")

def updateData(name,age,city,id):
    qry="update users set NAME=?,AGE=?,CITY=? where id=?;"
    con.execute(qry,(name,age,city,id))
    con.commit()
    print("user Details update")


def deleteData(Id):
    qry="delete from users where id=?";
    con.execute(qry,(id))
    con.commit()
    print("user Details delete")

def selectData():
    qry="select * from users"
    result=con.execute(qry)
    for row in result:
           print(row)

ch=1
while ch==1:
    c=int(input("select your choice:"))
    if(c==1):
        print("Add New User")
        name=input("Enter the name:")
        Age=int(input("Enter the Age:"))
        city=input("Enter the city:")
        insertData(name,Age,city)
    elif (c==2):
        print("Edit A Record")
        Id=input("Enter the Id:")
        name=input("Enter the name:")
        Age=input("Enter the age:")
        city=input("Enter the Email:")
        updateData(name,Age,city,Id)
    elif (c==3):
        print("Delete the Record")
        Id=input("Enter the id:")
        deleteData(Id)
    elif (c==4):
        print("print All Record")
        selectData()
    else:
        print("Invalid selection")
        ch=int(input("Enter 1 to continue"))
        print("Thank you")
    

