from tkinter import *
from back_end import Data
from tkinter import messagebox
import sys

data = Data('d:/mydata.db')
root = Tk()
root.geometry('600x400')
root.title('مدیریت فروشگاه')
root.config(bg='#FFA500')
#========def==============
def fetch():
    lstbox.delete(0 , END)
    rows = data.fetch()
    for row in rows:
        lstbox.insert(END , row)


def clear():
    ent_name.delete(0 , END)
    ent_sell.delete(0 , END)
    ent_price.delete(0 , END)
    ent_number.delete(0 , END)

def add():
    name = ent_name.get()
    f_price= ent_sell.get()
    gh_price = ent_price.get()
    number = ent_number.get()
    if name =='' :
        messagebox.showerror(title='error' , message='ورود نام الزامی است')
        return
    else:
        lstbox.insert(END ,f'{name} ,{f_price}قیمت فروش ,{gh_price}قیمت خرید,{number}تعداد')
        data.insert(name , gh_price , f_price , number)
    clear()
    fetch()
    ent_name.focus()
        


    
def search():
    lstbox.delete(0 , END)
    name = ent_name.get()
    f_price= ent_sell.get()
    gh_price = ent_price.get()
    number = ent_number.get()
    rows = data.search(name or f_price or gh_price or number)
    lstbox.delete(0 , END)
    lstbox.insert(END , f'نام - ق خ - ق ف - تعداد')
    for row in rows:    
        lstbox.insert(END , row)
    clear()
    
def delet():
    messeg = messagebox.askyesno(title= 'delete' , message='are you sure')
    if messeg == True:
        indx = lstbox.curselection()
        lst = lstbox.get(indx)
        lstbox.delete(indx)
        data.delet(lst[0])
def update():
    name = ent_name.get()
    f_price= ent_sell.get()
    gh_price = ent_price.get()
    number = ent_number.get()
    if name == '' :
        pass
    else:
        lstbox.insert(END ,f'{name} ,{f_price},{gh_price},{number}')
        data.insert(name , gh_price , f_price , number)
    clear()
def exist():
    messeg = messagebox.askyesno(title='exits' , message='are you sure')
    if messeg == True :
        root.destroy()



def select_item(event):
    name = ent_name.get()
    f_price= ent_sell.get()
    gh_price = ent_price.get()
    number = ent_number.get()
    if name == '' :
        pass
    else:
        lstbox.insert(END ,f'{name} ,{f_price},{gh_price},{number}')
        data.insert(name , gh_price , f_price , number)

    try:
        global selected_item
        index = lstbox.curselection()
        selected_item = lstbox.get(index)
        clear()
        ent_name.insert(END , selected_item[0])
        ent_number.insert(END , selected_item[3])
        ent_price.insert(END , selected_item[1])
        ent_sell.insert(END , selected_item[2])
        
        indx = lstbox.curselection()
        lst = lstbox.get(indx)
        lstbox.delete(indx)
        data.delet(lst[0])
    except IndexError:
        pass




#=========lbl==========
lbl_name= Label(root , text= ':نام کالا' , font='IranNastaliq 20 ' , bg='#FFA500' , fg='#4B0082')
lbl_name.place(x = 540 , y=15)

lbl_sell= Label(root , text= ':قیمت فروش' , font='IranNastaliq 20 ' , bg='#FFA500' , fg='#4B0082')
lbl_sell.place(x = 520 , y=70)

lbl_price = Label(root , text=':قیمت خرید' , font='IranNastaliq 20' , bg='#FFA500' , fg='#4B0082')
lbl_price.place(x=240 , y=15)

lbl_number= Label(root , text= ':تعداد' , font='IranNastaliq 20 ' , bg='#FFA500' , fg='#4B0082')
lbl_number.place(x = 250 , y=70)

lbl_star = Label(root , text='*' , fg='red' , font='Arial 18' , bg='#FFA500' ).place(x=320 , y=30)


#===========entry==========
ent_name = Entry(root , font='Calibri 14' , width=20 , bg='#FFF8DC')
ent_name.place(x= 335 , y=30)

ent_sell = Entry(root , font='Calibri 14' , width=18 , bg='#FFF8DC')
ent_sell.place(x= 335 , y=85)

ent_price = Entry(root , font='Calibri 14' , width=20 , bg='#FFF8DC')
ent_price.place(x= 35 , y=30)

ent_number = Entry(root , font='Calibri 14' , width=20 , bg='#FFF8DC')
ent_number.place(x= 35 , y=85)

#===========btn=============

btn_add = Button(root , text='اضافه کردن' , font='Arial 14' , width=15 , fg= '#FFA500' , bg= '#FFF8DC' , command=add)
btn_add.place(x=410 , y= 140)

btn_search = Button(root , text='جستجو کالا' , font='Arial 14' , width=15 , fg= '#FFA500' , bg= '#FFF8DC' , command=search)
btn_search.place(x=410 , y= 180)

btn_delet = Button(root , text='حذف کالا' , font='Arial 14' , width=15 , fg= '#FFA500' , bg= '#FFF8DC' , command=delet)
btn_delet.place(x=410 , y= 220)

btn_update = Button(root , text='ویرایش' , font='Arial 14' , width=15 , fg= '#FFA500' , bg= '#FFF8DC' , command=update)
btn_update.place(x=410 , y= 260)

btn_exit = Button(root , text='بستن' , font='Arial 14' , width=15 , fg= '#FFA500' , bg= '#FFF8DC', command=exist)
btn_exit.place(x=410 , y= 300)



lstbox= Listbox(root , font='Arial 12' , width=38 , bg='#FFF8DC')
lstbox.place(x=35 , y= 140 )


scrl = Scrollbar(root, command=lstbox.yview)
scrl.place(x=385, y=140, height=195)
lstbox.config(yscrollcommand=scrl.set)

lstbox.bind('<Double-Button-1>',select_item)


root.mainloop()
