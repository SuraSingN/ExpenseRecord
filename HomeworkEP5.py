# HomeworkEP3.py
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv
# ttk is theme of Tk

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by SingZ')
GUI.geometry('400x650+800+20')
#600 คือตำแหน่งจากแกน x ที่ให้ GUI ปรากฎหน้า window
#450 คือตำแหน่งจากแกน y ที่ให้ GUI ปรากฎหน้า window

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก
#ipadx=20 internal pading ขยายข้อความแนวแกน x

#---------MENU-------------

menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to GoogleSheet')
# Help
def About():
	messagebox.showinfo('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูล\nสนใจบริจาคเราไหม ขอ 1 BTC ก็พอครับ')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)
# Donate
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)





#--------MENU_END------------

#---------TAB---------------
Tab = ttk.Notebook(GUI)
f1 = Frame(Tab)
f2 = Frame(Tab)
Tab.pack(fill=BOTH)

#---------IMAGE---------------
img1 = PhotoImage(file='G:/Sing/Customer Logo/Calculator1.png').subsample(6)
img2 = PhotoImage(file='G:/Sing/Customer Logo/Calculator.png').subsample(6)
# subsample คือย่อรูป
# เวปหา icon  คือ IconArchive
#--------End_Image----------

Tab.add(f1,image = img1, text =f'{"ค่าใช้จ่าย":^{30}}', compound ='top')
Tab.add(f2,image = img2, text =f'{"ค่าใช้จ่ายทั้งหมด":^{30}}', compound = 'top')

#----------End_Tab----------

F1 = Frame(f1)
F1.pack()
#F1.place(x=50,y=120)

#---------Add_Background------------
imgbg = PhotoImage(file='G:/Sing/Customer Logo/Shopping.png').subsample(10)
imgbg1 = Label(F1,image = imgbg)
imgbg1.pack()
#---------End_Background------------

days ={'Mon':'จันทร์','Tue':'อังคาร','Wed':'พุธ',
		'Thu':'พฤหัสบดี','Fri':'ศุกร์','Sat':'เสาร์',
		'Sun':'อาทิตย์'}

def Save(event=None):
	expense = v_expense.get()
	price = v_price.get()
	quantity = v_quantity.get()

	if expense == '':
		print('No Data')
		messagebox.showinfo('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
		return
	elif price == '':
		messagebox.showerror('Error','กรุณากรอกราคา')
		return
	elif quantity == '':
		messagebox.showwarning('Error','กรุณากรอกจำนวน')
		return

	try:
		total = int(price) * int(quantity)
		# .get() ดึงมาจาก v_expense = StringVar()
		print('รายการ: {} \nราคา: {} บาท \nจำนวน: {} \nทั้งหมด {} บาท'.format(expense,price,quantity,total))
		text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
		text = text + 'จำนวน: {} รวมทั้งหมด: {}\n'.format(quantity,total)
		v_result.set(text)
		# clear ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		

		# บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
		today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
		print(today)
		dt = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
		dt = days[today] + '-' + dt
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
			# with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			# 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
			# 'w' การบันทึกครั้งเดียว
			# newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) #เป็นการสร้างฟังก์ชั่นสำหรับเขียนข้อมูล
			data = [dt,expense,price,quantity,total]
			dt = datetime.now()
			fw.writerow(data)
			
		# ทำให้ cursor กับไปตำแหน่งช่องกรอก E1
		E1.focus()
		update_table()


	except Exception as e:
		print('ERROR',e)
		#messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		#messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')

# ทำให้สามารถกด Enter ได้
GUI.bind('<Return>',Save) # ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = (None,20)# None เปลี่ยนเป็น 'Angsana New' ได้

#---------text1--------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#---------End----------


#---------text2--------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#---------End----------

#---------text3--------
L = ttk.Label(F1,text='จำนวน',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#---------End----------

saveimg = PhotoImage(file='G:/Sing/Customer Logo/save.png').subsample(6)
B2 = ttk.Button(F1,image = saveimg, text='Save',command=Save, compound = 'left')
B2.pack(ipadx=50,ipady=20,pady=30)

v_result = StringVar()
v_result.set('    ผลลัพธ์     ')
result = ttk.Label(F1, textvariable=v_result, font=FONT1,foreground='Blue')
result.pack(pady=10)

#----------------TAB2----------------

def read_csv():
	with open('savedata.csv',newline='',encoding='utf-8') as f: # function with เอาไว้กันลืม close
		fr = csv.reader(f)
		data = list(fr)
	return data
		# print(data)
		# print('--------')
		# print(data[0][0])
		# for d in data:
		#     print(d)

#-----------TABLE----------

L = ttk.Label(f2,text='ตารางแสดงผลลัพธ์ทั้งหมด',font=FONT1).pack(pady=20)

header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
result_table = ttk.Treeview(f2,columns=header,show='headings',height=20)
result_table.pack()

# result_table.heading(header[0],text=header[0])

for h in header:
	result_table.heading(h,text=h)

headerwidth = [150,170,80,80,80] # หน่วยเป็น pixel
for h,w in zip(header,headerwidth):
	result_table.column(h,width=w)


# result_table.insert('','end',value=['จันทร์','น้ำดื่ม',30,50,1500])
# result_table.insert('','end',value=['อังคาร','น้ำดื่ม',30,50,1500])

def update_table():
	result_table.delete(*result_table.get_children())
	# for c in result_table.get_children():
	#      result_table.delete(c)
	data = read_csv()
	for d in data :
		result_table.insert('',0,value=d)

update_table()
print('GET CHILD',result_table.get_children())


GUI.mainloop()
