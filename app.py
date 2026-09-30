'''
	python database
'''
from mysql.connector import connect
from tabulate import tabulate
from os import system

def addstudent(**kwargs)->bool:
    keys:list = list(kwargs.keys())
    values:list = list(kwargs.values())
    fields:str = ",".join(keys)
    data:str = "','".join(values)
    sql:str = f"INSERT INTO `students`({fields}) VALUES('{data}')"
    conn:any = connect(
        host='127.0.0.1', #computer database
        database='pythondb',
        user='root',
        password=''
    )
    cursor:any = conn.cursor()#database record manager
    cursor.execute(sql)#prepare inputted data to be stored to db
    conn.commit() #store data to database
    return True if cursor.rowcount>0 else False
    

def getall()->None:
    #system('cls')
    #create a connection from your program to the database
    conn:any = connect(
        host='127.0.0.1', #computer database
        database='pythondb',
        user='root',
        password=''
    )
    #get the database content
    sql:str = "SELECT * FROM `students`"
    #create a recordset
    cursor:any = conn.cursor(dictionary=True)#database record manager
    cursor.execute(sql)
    #fetch al data from the database
    data:list = cursor.fetchall()
    #close the database connection
    conn.close()
    #print(data)
    for item in data:
        print(f"{item['id']}\t{item['idno']}\t{item['lastname']}\t{item['firstname']}\t{item['course']}\t{item['level']}")
    headers = ["id", "idno", "lastname","firstname","course","level"]
    #print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
def main()->None:
    getall()
    print("-"*60)
    addstudent(idno='1006',lastname='uehara',firstname='ai',course='bsit',level='3')
    getall()

if __name__=="__main__":
    main()