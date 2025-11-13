import psycopg2

conn = None

# import os
# import sys

# database = sys.argv[1]
# user = os.environ.get('PGUSER')
# password = os.environ.get('PGPASSWORD')
# host = os.environ.get('PGHOST')
# port = os.environ.get('PGPORT')

def isprime(n):
    if n <= 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


try:
    #connect to database
    conn = psycopg2.connect(database = "Graded Assignment",user = "postgres",password = "Om@270606", host = "127.0.0.1",port = "5433")
    print("Database connected")
    cur = conn.cursor()  #create a cursor
    cur.execute('''
        select t.name ,p.name ,p.jersey_no
        from teams t , players p
        where t.team_id = p.team_id
        order BY p.name DESC , t.name DESC
     ''')
    
    # result = cur.fetchone()    #this is for fetching frist row
    result = cur.fetchall()       #this is for fetching everything
    # result = cur.fetchmany(size=2)   #list of tapuls
    
    # print(result)
    
    for row in result:
        t_name = row[0]
        p_name = row[1]
        jersey_no = row[2]
        
        if isprime(jersey_no):
            print(p_name+ ','+t_name)
    
    
    cur.close()  #close the cursor
    
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
    
finally:
    if conn is not None:
        conn.close()  # close the connection
        