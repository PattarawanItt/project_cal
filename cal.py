#Phatharawan Ittichaiwatthana 6310742744
#SF210
#Project Individual Assignment : Calculator

import time
from tkinter import *

#สร้างหน้าต่างGui
root = Tk()
root.geometry("470x600")
root.title("calculator")

icon = PhotoImage(file="calculator.png")
root.iconphoto(False, icon)

#กำหนดตัวแปร เพื่อเก็บข้อมูล
text_Input = StringVar()
calcu = ""
list_num = []
ans = []

color_theme_operator = "#8b83db"
color_theme_number = "#0066ff"
color_theme_advance = "#f0504e"
font_theme = ('arial', 30, 'bold')

localtime=time.asctime(time.localtime(time.time()))

#สร้าง Frame สำหรับตกแต่ง
top_lable = Frame(root)
top_lable.pack(side=TOP)

#สร้าง Lable ไว้แสดงข้อความ Calculator และใช้ grid ในการช่วยจัดวางตำแหน่ง
info_calcu = Label(top_lable, font=font_theme, fg="#f0504e", text="Calculator", anchor="n")
info_calcu.grid(row=0, column=0)

#สร้าง Lable ไว้แสดงรูปภาพ และใช้ grid ในการช่วยจัดวางตำแหน่ง
image_lable = Label(top_lable, image=icon, pady=5)
image_lable.grid(row=1,column=0)

#สร้าง Lable ไว้แสดงเวลา และใช้ grid ในการช่วยจัดวางตำแหน่ง
times = Label (top_lable, font=('arial', 20), text=localtime ,fg="#f0504e", pady=15, anchor='n')
times.grid(row=2,column=0, pady=15)

#สร้าง Frame สำหรับทำช่องแสดงค่า
show = Frame(root, relief=SUNKEN)
show.pack(side=TOP)

#สร้าง Frame ไว้สำหรับทำปุ่ม
btn = Frame(root)
btn.pack(side=BOTTOM)

#ฟังก์ชันการคำนวณ
def btnClick(numbers):
    global calcu
    calcu = calcu + str(numbers)
    list_num.append(calcu)
    text_Input.set(calcu)

#ฟังก์ชันการเคลียเพื่อเริ่มการคำนวณใหม่
def btnClear():
    global calcu
    calcu=""
    list_num.clear()
    text_Input.set("")

#ฟังก์ชันเท่ากับ 
def btnEquals():
    global calcu, list_num
    sumup = str(eval(calcu))
    ans.append(sumup)
    print(sumup)
    text_Input.set(sumup)
    calcu = str(sumup) + ""
    
    #เมื่อกด = จะมีการเก็บค่าคำตอบของแต่ละรอบเอาไว้ในไฟล์ด้วย
    with open("history.txt", "a") as f:
        f.write(calcu + '\n')
        f.close()
        pass
    print("File successfully create")

#ฟังก์ชันลบค่า เมื่อมีการป้อนค่าผิด
def delete():
    global calcu
    calcu = calcu[: -1]
    text_Input.set(calcu)



#สร้าง Entry ไว้แสดงค่า 
display = Entry(show, font=(None,25), bd=5 , textvariable=text_Input, width=18, bg="#8b83db", fg="black")
display.grid(columnspan=5)

#BUTTON
b_clear = Button(btn,text='AC', font=(None, 20, "bold"), padx=30, pady=15, fg=color_theme_advance, command=btnClear).grid(row=0, column=0, sticky='NSEW')
b_pow = Button(btn,text='pow', font=(None, 16), padx=30, pady=15, fg=color_theme_advance, command=lambda: btnClick("**2")).grid(row=0, column=1, sticky='NSEW')
b_del = Button(btn,text='⌫', font=(None, 16), padx=30, pady=15, fg=color_theme_advance, command=delete).grid(row=0, column=2, sticky='NSEW')
b_di = Button(btn,text='÷', font=(None, 16, "bold"), padx=30, pady=15, fg=color_theme_operator, command=lambda: btnClick("/")).grid(row=0, column=3, sticky='NSEW')
b_equ = Button(btn,text='=', font=(None, 16, "bold"), padx=30, pady=15, fg=color_theme_advance, command=btnEquals).grid(row=0, column=4, sticky='NSEW', rowspan=5)


b7 = Button(btn,text='7', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(7)).grid(row=1, column=0, sticky='NSEW')
b8 = Button(btn,text='8', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(8)).grid(row=1, column=1, sticky='NSEW')
b9 = Button(btn,text='9', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(9)).grid(row=1, column=2, sticky='NSEW')
b_multi = Button(btn,text='x', font=(None, 16, "bold"), padx=30, pady=15, fg=color_theme_operator, command=lambda: btnClick("*")).grid(row=1, column=3, sticky='NSEW')

b4 = Button(btn,text='4', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(4)).grid(row=2, column=0, sticky='NSEW')
b5 = Button(btn,text='5', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(5)).grid(row=2, column=1, sticky='NSEW')
b6 = Button(btn,text='6', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(6)).grid(row=2, column=2, sticky='NSEW')
b_sub = Button(btn,text='-', font=(None, 16, "bold"), padx=30, pady=15, fg=color_theme_operator, command=lambda: btnClick("-")).grid(row=2, column=3, sticky='NSEW')

b1 = Button(btn,text='1', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(1)).grid(row=3, column=0, sticky='NSEW')
b2 = Button(btn,text='2', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(2)).grid(row=3, column=1, sticky='NSEW')
b3 = Button(btn,text='3', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(3)).grid(row=3, column=2, sticky='NSEW')
b_add = Button(btn,text='+', font=(None, 16, "bold"), padx=30, pady=15, fg=color_theme_operator, command=lambda: btnClick("+")).grid(row=3, column=3, sticky='NSEW')

b0 = Button(btn,text='0', font=(None, 16), padx=30, pady=15, fg=color_theme_number, command=lambda: btnClick(0)).grid(row=4, column=0, sticky='NSEW', columnspan=3)
b_dot = Button(btn,text='.', font=(None, 16, "bold"), padx=30, pady=15, fg=color_theme_advance, command=lambda: btnClick(".")).grid(row=4, column=3, sticky='NSEW')

#ปุ่ม Exit เมื่กดจะทำการปิดโปรแกรม
b_exit = Button(btn, text="EXIT", font=(None, 16), padx=30, pady=15, fg="Red", command=lambda:root.destroy()).grid(row=5, column=0, columnspan=5, sticky='NSEW')


root.mainloop()