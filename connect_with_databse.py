#%%
import mysql.connector as msc
class mysqldatabase:
    def __init__(self,username,password):
        self.conn = msc.connect (host = "localhost",
                                 username=username,
                                 passowrd = password,
                                 port = 3306,
                                 database = 'testing')
        self.cursor = self.conn.cursor()

    def insert_data (self,roll_no,name,gender,age):
        data = (roll_no,name,gender,age)
        query = "insert into student_info values (%s,%s,%s,%s)"
        self.cursor.eecute(query,data)
        self.conn.commit()
        return "Successfully added data"
    
    def __update_query(self,field,*data):
        query = f"update student_info set {field}= %s where roll_no = %s"
        self.cursor.execute (query,data)
        self.conn.commit()

    def update_data (self,roll_no,name = None,gender = None,age = None):
        if name != None and gender == None and age == None:
            self.__update_query("name",name,roll_no)
        elif name == None and gender != None and age == None:
            self.__update_query ("gender",gender,roll_no)
        elif name == None and gender == None and age != None:
            self.__update_query("age",age,roll_no)
        else:
            return "wrong update"
        return "successfully data entered"
    
#%%
database = mysqldatabase("root", "qwert")
result = database.insert_data(101, "Adi", "Male", 20)
print(result)
# %%
