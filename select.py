import psycopg2

conn = None

try:
    #connect to database
    conn = psycopg2.connect(database = "learn",user = "postgres",password = "Om@270606", host = "127.0.0.1",port = "5433")
    print("Database connected")
    cur = conn.cursor()  #create a cursor
    cur.execute('''
        SELECT * from classroom
         ''')
    
    # result = cur.fetchone()    #this is for fetching frist row
    # result = cur.fetchall()       #this is for fetching everything
    result = cur.fetchmany(size=2)   #list of tapuls
    
    print(result)
    
    for row in result:
        id = row[0]
        name = row[1]
        print(id, name)
    
    
    cur.close()  #close the cursor
    
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
    
finally:
    if conn is not None:
        conn.close()  # close the connection
        