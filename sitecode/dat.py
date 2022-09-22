import psycopg2
from datetime import date

class datamanager():
    def __init__(self):
        self.conn = psycopg2.connect(database="plate_database",user='postgres',password=' ',host='localhost',port= '5432')
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
    def addplate(self,plate,ending_date="9999-12-31"):
        self.cursor.execute(f''' select * from "Plates" where "Plates"."Plate" = '{plate}' ''')
        if len(plate)==8  and self.cursor.fetchone() == None:
            query=f'''insert into "Plates"("Plate","starting date","ending date") values('{plate}','{date.today()}','{ending_date}') '''
            self.cursor.execute(query)
            self.conn.commit()
            return True
        else:
            return False
    def removeplate(self,plate):
        self.cursor.execute(f'''Delete from "Plates" where "Plates"."Plate" = '{plate}' ''')
        self.conn.commit()
    def getplate(self,):
        self.cursor.execute(f'''select * from "Plates"''')
        return(self.cursor.fetchall())
    def getonlyplate(self,):
        self.cursor.execute(f'''select "Plates"."Plate" from "Plates"''')
        return([x[0] for x in self.cursor.fetchall()])