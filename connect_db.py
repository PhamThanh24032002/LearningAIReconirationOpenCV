import sqlite3

class sinhvien:
    
    
    def __init__(self, id = None,name = None,lop = None):
        self.id = id
        self.name = name
        self.lop = lop
        self.count_people = []
    # def getAllSinhvien(self):
    #     db = "database/sinhvien.db"
    #     conn = sqlite3.connect(db)
        
    #     # kieemr tra id xem cos ton tai hay khong
        
    #     query = "select Id from sinhvien"
    #     cursor = conn.execute(query)
    #     return cursor.fetchall()
        
    def insertOrUpdate(self):
        #connect to db
        db = "database/sinhvien.db"
        conn = sqlite3.connect(db)
        
        # kieemr tra id xem cos ton tai hay khong
        
        query = "select * from sinhvien WHERE ID="+str(self.id)
        cursor = conn.execute(query)
        print('hi')
        isRecordExist = 0
        for row in cursor:
            isRecordExist =1
        if(isRecordExist ==1):
            query = "update sinhvien SET Name='"+str(self.name)+"' where ID="+str(id)
        else:
            query = "insert into sinhvien(ID,Name,Checked,Lop) values("+str(self.id)+",'"+str(self.name)+"',0,'"+str(self.lop)+"')"
            conn.execute(query)
            conn.commit()
            print(query)
            conn.close()
            
    def getProfile(id):
        conn=sqlite3.connect("database/sinhvien.db")
        cmd="SELECT * FROM sinhvien WHERE ID="+str(id)
        cursor=conn.execute(cmd)
        profile=None
        for row in cursor:
            profile=row
        conn.close()
        return profile
            