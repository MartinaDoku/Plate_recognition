from sqlite3 import connect
import psycopg2
from datetime import date
conn = psycopg2.connect(
   database="plate_database",
    user='postgres',
    password=' ',
    host='localhost',
    port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()
def addplate(plate,ending_date="9999-12-31"):
    cursor.execute(f''' select * from "Plates" where "Plates"."Plate" = '{plate}' ''')
    if len(plate)==8  and cursor.fetchone() == None:
        query=f'''insert into "Plates"("Plate","starting date","ending date") values('{plate}','{date.today()}','{ending_date}') '''
        print(query)
        print(cursor.execute(query))
    conn.commit()
def removeplate(plate):
    cursor.execute(f'''Delete from "Plates" where "Plates"."Plate" = '{plate}' ''')
    conn.commit()

#addplate("FR255SKI")
#cursor.execute(f'''select * from "Plates"''')
#print(cursor.fetchall())
#removeplate("FR255SKI")
#cursor.execute(f'''select * from "Plates"''')
#print(cursor.fetchall())
