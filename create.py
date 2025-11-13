import psycopg2

conn = None

try:
    #connect to database
    conn = psycopg2.connect(database = "test",user = "postgres",password = "Om@270606", host = "127.0.0.1",port = "5433")
    print("Database connected")
    cur = conn.cursor()  #create a cursor
    cur.execute('''
                CREATE TABLE employees(
                    emp_num int PRIMARY KEY,
                    emp_name varchar(25) NOT NULL
                )
         ''')
    conn.commit()  #commit to change in databaces 
    
    # cur.execute("select * from emloyees")
    
    print("Table created successfully")
    cur.close()  #close the cursor
    
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
    
finally:
    if conn is not None:
        conn.close()  # close the connection
        
        