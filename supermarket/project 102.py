from tkinter import*  # عشان اجيب المكتبة tkinter
from tkinter import messagebox  # استيراد الرساله   tkinter
import webbrowser  # استيراد مكتبة فتح الروابط في الموقع
import os  # استيراد مكتبة عمليات النظام
import sys  # استيراد مكتبة النظام

# إنشاء الواجهه للتطبيق
market = Tk()
market.geometry('800x440+280+50')  #  أبعاد النافذة وموقعها
market.title('SUPERMARKET')  #  عنوان النافذة
market.iconbitmap('Shopping bag gold logo vector image on VectorStock.ico')  #  أيقونة للنافذة

# إضافة العنوان الرئيسي
title = Label(market, text='Super Market System', fg='gold', bg='black', font=('tajawal', 18, 'bold'))
title.pack(fill=X) #ملء العنوان 


def about1 ():
    messagebox.showinfo('develpor', 'omar ehab id:241000953')
def about2 ():
    messagebox.showinfo('about project', 'project supermarket')



def log():
     user= En1.get ()
     passw= En2.get ()
     if user == 'omar' and passw == '123456' :
        messagebox.showinfo('welcome its TRUE', 'HELLO')
     else:
       messagebox.showerror('sorry its wrong', 'false')


# إنشاء الجانب 
F1 = Frame(market, width=230, height=420, bg='#0B2F3A')
F1.place(x=570, y=40)  # وضع الإطار في اليمين

# إضافة العناوين داخل الإطار
title1 = Label(F1, text='PROJECT SUPER MARKET', bg='#0B2F3A', fg='white', font=('tajawal', 11, 'bold'))
title1.place(x=40, y=8)  # وضع الكلام داخل الإطار

title2 = Label(F1, text='OMAR EHAB', bg='#0B2F3A', fg='white', font=('tajawal', 11, 'bold'))
title2.place(x=52, y=50)  # وضع اسم اصحاب المشروع

title3 = Label(F1, text='CONTACT US', bg='#0B2F3A', fg='white', font=('tajawal', 11, 'bold'))
title3.place(x=52, y=90)  #  التواصل

# إضافة الأزرار داخل الإطار
B1 = Button(F1, text='FACEBOOK ACOUNT', width=26, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'))
B1.place(x=6, y=130)  # زر لفتح حساب الفيسبوك

B2 = Button(F1, text='INSTAGRAM ACOUNT', width=26, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'))
B2.place(x=6, y=177)  # زر لفتح حساب الإنستغرام

B3 = Button(F1, text='WATSAPP ACOUNT', width=26, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'))
B3.place(x=6, y=225)  # زر لفتح حساب الواتساب

B4 = Button(F1, text='ABOUT DEVELOPER', width=26, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=about1)
B4.place(x=6, y=272)  # زر لعرض لمحه عن المطورين

B5 = Button(F1, text='ABOUT OF PROJECT', width=26, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=about2)
B5.place(x=6, y=318)  # زر لعرض معلومات عن المشروع

B6 = Button(F1, text='CLOSE PROJECT', width=26, fg='black', bg='#DBA901', font=('tajawal', 11, 'bold'), command=quit) 
B6.place(x=6, y=365)  # زر لإغلاق المشروع


photo= PhotoImage(file="shop.png")
imo=Label(market, image=photo)
imo.place(x=120, y=43, width=308, height=272)

F2= Frame(market , width=570, height=120, bg='#0B2F3A')
F2.place(x=0 , y=339)
photo1 = PhotoImage(file="login.png")
imo1 = Label(market , image=photo1)
imo1.place(x=450, y=335, width=110, height=110)
L1 = Label (F2, text= 'USER NAME', fg='gold', bg='#0B2F3A', font=('tajawal, 12'))
L1.place(x=330, y=25)
L2 = Label (F2, text= 'PASSWORD', fg='gold', bg='#0B2F3A', font=('tajawal, 12'))
L2.place(x=330, y=70)
En1 = Entry(F2 , font=('tajawal',12), justify='center')
En1.place(x=130, y=26)
En2 = Entry(F2 , font=('tajawal',12), justify='center')
En2.place(x=130, y=71)
B= Button(F2 , text='LOGIN' , bg='#DBA901', font=('tajawal',12), width=12 , height=3,command=log )
B.place(x=10 , y=20)


















# تشغيل التطبيق
market.mainloop()