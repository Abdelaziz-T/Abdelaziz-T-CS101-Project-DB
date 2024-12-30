from tkinter import*
from tkinter import messagebox
import os , math ,random 
class Super:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1300x700+30+10')
        self.root.title('Super_Market: سوبر ماركت')
        self.root.resizable(False,False)
        self.root.iconbitmap('Shopping bag gold logo vector image on VectorStock.ico')
        title = Label(self.root, text='ادارة المشاريع : سوبر ماركت',fg='white', bg='#0B2F3A',font=('tajawal',15))
        title.pack(fill=X)
        #====================Customer Data===========
        F1= Frame(root,bd=2,width=338,height=170,bg='#0B4C5F')
        F1.place(x=961,y=35)
        tit=Label(F1, text=' : بيانات المشتري  ' , font=('tajawal',13,'bold'), bg='#0B4c5F', fg='tomato')
        tit.place(x=185,y=0)
        his_name= Label(F1 , text=' اسم المشتري',font=('tajawal',10),bg='#0B4C5F',fg='white')
        his_name.place(x=230,y=40)
        his_phone= Label(F1 , text=' رقم المشتري',font=('tajawal',10),bg='#0B4C5F',fg='white')
        his_phone.place(x=235,y=70)
        bill_num= Label(F1 , text=' رقم الفاتورة',font=('tajawal',10),bg='#0B4C5F',fg='white')
        bill_num.place(x=242,y=100)

        Ent_name = Entry(F1, justify='center')
        Ent_name.place(x=90,y=42)
        Ent_phone = Entry(F1, justify='center')
        Ent_phone.place(x=90,y=72)
        Ent_bill = Entry(F1, justify='center')
        Ent_bill.place(x=90,y=102)

        btn_customer = Button(F1 , text='Search' , font=('tajawal',10),width=10,height=4,bg='white')
        btn_customer.place(x=3,y=40)

        #============== Fatora bill ==============

        titdd = Label(F1 , text='[الفواتير]' , font=('tajawal',13,'bold') , bg='#0B4C5F' , fg='gold' )
        titdd.place(x=125,y=135)
        F3 = Frame(root,bd=2 , width=338 ,height=399 , bg='white')
        F3.place(x=961,y=205)
        scrol_y = Scrollbar(F3, orient=VERTICAL)
        self.textarea= Text(F3 ,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH , expand=1)
        #============ Price =============
        F4 = Frame(root, bd=2 , width=657, height=112 , bg='#0B4C5F')
        F4.place(x=641,y=587)
        hesab = Button(F4, text='الحساب', width=13, height=1 , font='tajawal', bg='#DBA901')
        hesab.place(x=520, y=10)
        fatora = Button(F4, text='تصدير الفاتورة' , width=13,height=1,font='tajawal',bg='#DBA901')
        fatora.place(x=520,y=55)
        clear = Button(F4, text='افراغ الحقول' , width= 13,height=1 , font='tajawal', bg='#DBA901')
        clear.place(x=375,y=10)
        exit = Button(F4, text='اغلاق البرنامج', width=13,height=1,font='tajawal',bg='#DBA901' )
        exit.place(x=375, y=55)
        
        
        lb101 = Label(F4, text='حساب الكلي للبقوليات', font=('tajawal',10,'bold'), bg='#0B4C5F',fg='gold')
        lb101.place(x=220,y=10)

        lb102 = Label(F4, text='حساب اللوازم المنزليه', font=('tajawal',10,'bold'), bg='#0B4C5F',fg='gold')
        lb102.place(x=220,y=40)

        lb103 = Label(F4, text='حساب ادوات الكهرباء', font=('tajawal',10,'bold'), bg='#0B4C5F',fg='gold')
        lb103.place(x=220,y=70)


        ento1 = Entry(F4, width=24)
        ento1.place(x=40, y=12)

        ento2 = Entry(F4, width=24)
        ento2.place(x=40, y=42)

        ento3 = Entry(F4, width=24)
        ento3.place(x=40, y=72)

        #============= items[1] ============
        FF1=Frame(root, bd=2 , width=318, height=664,bg='#0B4C5F')
        FF1.place(x=1,y=35)
        t = Label(FF1, text='البقوليات', font=('tajawal',13,'bold'), bg='#0B4C5F' , fg='gold')
        t.place(x=122,y=0)
        bq1 = Label(FF1, text='الرز', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq1.place(x=250,y=50)

        bq2 = Label(FF1, text='برغل', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq2.place(x=240,y=80)

        bq3 = Label(FF1, text='فاصولياء', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq3.place(x=210,y=110)

        bq4 = Label(FF1, text='عدس', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq4.place(x=232,y=140)

        bq5 = Label(FF1, text='مكرونة', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq5.place(x=213,y=170)

        bq6 = Label(FF1, text='حمص', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq6.place(x=233,y=200)

        bq7 = Label(FF1, text='فول', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq7.place(x=228,y=230)

        bq8 = Label(FF1, text='الملح', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq8.place(x=240,y=270)

        bq9 = Label(FF1, text='سكر', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq9.place(x=230,y=300)

        bq10 = Label(FF1, text='فلفل اسود', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq10.place(x=233,y=330)

        bq11 = Label(FF1, text='اللوبيا', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq11.place(x=200,y=370)

        bq12 = Label(FF1, text='فلفل احمر', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq12.place(x=200,y=400)

        bq13 = Label(FF1, text='كمون', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq13.place(x=230,y=430)

        bq14 = Label(FF1, text='قمح', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq14.place(x=210,y=470)

        bq15 = Label(FF1, text='شعير', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq15.place(x=230,y=500)

        bq16 = Label(FF1, text='شوفان', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq16.place(x=220,y=530)

        bq17 = Label(FF1, text='ذرة', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq17.place(x=230,y=570)

        bq18 = Label(FF1, text='اللوبيا', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq18.place(x=230,y=600)







root=Tk()
ob = Super(root)
root.mainloop()