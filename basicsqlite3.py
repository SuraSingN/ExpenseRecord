# basicsqlite3.py

import sqlite3 

# สร้าง database
conn = sqlite3.connect('expense.db') # หรือ .sqlite3
# สร้างตัวดำเนินการหรือ execution (อยากได้อะไรใช้ตัวนี้ได้เลย)
c = conn.cursor() 

# สร้าง table ด้วยภาษา sql
'''['รหัสรายการ (transactionid)' TEXT,
'วัน-เวลา(datetime)' TEXT,
'รายการ(title)' TEXT,
'ค่าใช้จ่าย(expense)' REAL (float),
'จำนวน(quantity)' INTEGER,
'รวม(total)' REAL]
'''

# ถ้าหลายบรรทัดเมื่อไรต้องใช้ """__""" ไม่สามารถใช้ "_" ได้
# transaction is sqlite keyword 

c.execute("""CREATE TABLE IF NOT EXISTS expenselist(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				transactionid TEXT,
				datetime TEXT,
				title TEXT,
				expense REAL,
				quantity INTEGER,
				total REAL
			)""")

def insert_expense(transactionid,datetime,title,expense,quantity,total):
	ID = None # ID คือตัวที่ 7 ของ ?
	with conn:
		c.execute("""INSERT INTO expenselist VALUES (?,?,?,?,?,?,?)""",
			(ID,transactionid,datetime,title,expense,quantity,total))
		conn.commit() # การบันทึกข้อมูลลงในฐานข้อมูล ถ้าไม่รันตัวนี้จะไม่บันทึก
		print('Insert Success!')

def show_expense():
	with conn:
		c.execute("SELECT * FROM expenselist")
		expense = c.fetchall() # คำสั่งให้ดึงข้อมูลเข้ามาใส่ในตัวแปรที่ชื่อ expense
		print(expense)

	return expense

def update_expense(transactionid,title,expense,quantity,total):   # expense,quantity,total):
	with conn:
		c.execute("""UPDATE expenselist SET 
			title=?, 
			expense=?, 
			quantity=?, 
			total=? WHERE transactionid=?""",
			([title,expense,quantity,total,transactionid]))
	conn.commit()
	print('Data updated')

def delete_expense(transactionid):
	with conn:
		c.execute("DELETE FROM expenselist WHERE transactionid=(?)",([transactionid]))
	conn.commit()
	print('Data deleted')

# insert_expense('20213234456','วันเสาร์ 2021-06-19','ข้าวสาร',45,2,90) # - C - CREATE
# show_expense() # - R - READ
# update_expense('20213234456','omelette',50,2,100) # - U - UPDATE
# delete_expense('20213234457') # - D - DELETE 

show_expense()

print('success')