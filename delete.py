import psycopg2

conn = None


def deleterecord(id):
    try:
        #connect to database
        conn = psycopg2.connect(database = "test",user = "postgres",password = "Om@270606", host = "127.0.0.1",port = "5433")
        print("Database connected")
        cur = conn.cursor()  #create a cursor
        cur.execute('''
                    DELETE FROM employees WHERE emp_num = %s 
        ''', (id, ))
        conn.commit()  #commit to change in databaces 
        
        # cur.execute("select * from emloyees")
        
        print("delete successfully")
        cur.close()  #close the cursor
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()  # close the connection
            
deleterecord(2)