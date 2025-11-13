import psycopg2

conn = None

try:
    #connect to database
    conn = psycopg2.connect(database = "Practice",user = "postgres",password = "Om@270606", host = "127.0.0.1",port = "5433")
    print("Database connected")
    print(conn)
    
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
    
finally:
    if conn is not None:
        conn.close()  # close the connection
        
        
        
        