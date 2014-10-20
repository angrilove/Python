# !usr/bin/python
# -* utf8 *-

'''
import MySQLdb as mysqldb

db = mysqldb.connect(host = '192.168.1.45', user = 'escpt', passwd = '111111', db = 'test', charset = 'utf-8')
cur = db.cursor()
sql = unicode("select * from `test` where sex = ''", "utf-8")
print sql
cur.execute(sql)
cur.close()
db.close()
'''

import MySQLdb

## 
db = MySQLdb.connect("localhost", "root", "123456", "tests")

# 
cursor = db.cursor()

# 
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print ("Database version : %s ", data)

# 
cursor.close()
db.close()
