from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import re


window = Tk()
window.geometry("800x1000")
window.configure(background="pink")
c=tkinter

def summit_details():
   window1 = Tk()

   Label1=Label(window1, text="your response has been recorded",font="ar 20 normal")
   Label1.grid(row=4,column=2,padx=20,pady=30)
   
   window1.title("canvas")
   window1.geometry("500x300")
   window1.mainloop()

### label ###
Title=Label(window,text="STUDENT  REGISTRATION  FORM",font="ar 15 bold")
Title.grid(row=1,column=1,padx=30,pady=10)

name = Label(window, text="Name",font="ar 13 bold")
name.grid(row=4,column=0,padx=30,pady=10)

father = Label(window, text="Father Name",font="ar 13 bold")
father.grid(row=6,column=0,padx=30,pady=10)

address = Label(window, text="Address",font="ar 13 bold")
address.grid(row=8,column=0,padx=30, pady=10)


sex = Label(window, text="Sex",font="ar 13 bold")
sex.grid(row=12,column=0,padx=30, pady=30)

state = Label(window, text="State",font="ar 13 bold")
state.grid(row=18,column=0,padx=10, pady=10)

distric = Label(window, text="Distric",font="ar 13 bold")
distric.grid(row=20,column=0,padx=30, pady=10)

city = Label(window, text="City",font="ar 13 bold")
city.grid(row=22,column=0,padx=30, pady=10)

pincode = Label(window, text="Pincode",font="ar 13 bold")
pincode.grid(row=24,column=0,padx=30, pady=10)

course = Label(window, text="Course",font="ar 13 bold")
course.grid(row=26,column=0,padx=30, pady=10)

email = Label(window, text="Email Id",font="ar 13 bold")
email.grid(row=28,column=0,padx=30, pady=10)

dob = Label(window, text="DOB",font="ar 13 bold")
dob.grid(row=30,column=0,padx=30, pady=10)

mobile = Label(window, text="Mobile Number",font="ar 13 bold")
mobile.grid(row=32,column=0,padx=30, pady=10)


#####    checkbutton    #######
malevalue = IntVar()
femalevalue = IntVar()

male = Checkbutton(window, text="Male",variable = malevalue,font="ar 10 bold")
male.grid(row=12,column=2, padx=30, pady=10)

female = Checkbutton(window, text="Female",variable = femalevalue,font="ar 10 bold")
female.grid(row=12,column=1, padx=30, pady=10)

####    Entrybox    ########
namevalue    = StringVar
fathervalue  = StringVar
#addressvalue = StringVar
pincodevalue = StringVar
emailvalue = StringVar
dobvalue = IntVar
mobilenumber = IntVar

nameentry = Entry(window, textvariable=namevalue,width=30, font=('calibre',10,'normal'))
nameentry.grid(row=4,column=1,padx=10,pady=10)

fatherentry = Entry(window, textvariable=fathervalue,width=30,font=('calibre',10,'normal'))
fatherentry.grid(row=6,column=1,padx=10,pady=10)

"""addressentry = Entry(window, textvariable=addressvalue,font=('calibre',13,'normal'))
addressentry.grid(row=8,column=1,padx=30, pady=10)"""
txtaddress=Text(window,width=30,height=3,font=("calibre",10,"normal"))
txtaddress.grid(row=8,column=1,columnspan=4,padx=90,pady=10,sticky="W")                                              

pincodeentry = Entry(window, textvariable=pincodevalue,width=20,font=('calibre',13,'normal'))
pincodeentry.grid(row=24,column=1,padx=30, pady=10)

emailentry = Entry(window, textvariable=emailvalue,width=20,font=('calibre',13,'normal'))
emailentry.grid(row=28,column=1,padx=30, pady=10)

dobentry = Entry(window, textvariable=dobvalue,width=20,font=('calibre',13,'normal'))
dobentry.grid(row=30,column=1,padx=30, pady=10)

mobileentry = Entry(window, textvariable=mobilenumber,width=20,font=('calibre',13,'normal'))
mobileentry.grid(row=32,column=1,padx=30, pady=10)


####    combobox   #######
statevalue = StringVar
districvalue = StringVar
cityvalue = StringVar
coursevalue = StringVar

statecombo = ttk.Combobox(window,textvariable = statevalue, width=24, font=('calibre',10,'normal'))
statecombo.grid(row=18,column=1,padx=30, pady=10)
statecombo['values'] = ('Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharhand',
                        'Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab',
                        'Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal')

districcombo = ttk.Combobox(window,textvariable = districvalue, width=24, font=('calibre',10,'normal'))
districcombo.grid(row=20,column=1,padx=30, pady=10)
districcombo['values'] = ('Ariyalur','Chengalpattu','Chennai','Coimbatore','Cuddalore','Dharmapuri','Dindigul','Erode','Kallakurichi','Kanchipuram',
                          'kanyakumari','Karur','Krishnagiri','Madurai','Nagapattinam','Namakkal','Nilgiris','Perambalur','Pudukkottai','Ranipet','Slem')

citycombo = ttk.Combobox(window,textvariable = cityvalue, width=24, font=('calibre',10,'normal'))
citycombo.grid(row=22,column=1,padx=30, pady=10)
citycombo['values'] = ('Ariyalur','Chennai','Coimbatore','Cuddalore','Dharmapuri','Dindigul','Erode','Kanchipuram','Kanniyakumari','Krishnagiri','Madurai',
                       'Nagapattinam','Namakkal','Perambalur','Pudukkottai','Ramanathapuram','Salem','Sivaganga','Thanjavur','Theni','The Nilgiris','Thiruvallur',
                       'Thiruvarur','Thoothukkudi','Tiruchirappalli','Trunelveli','Tiruppur','Tiruvannamalai','Vellore','Viluppuram','Virudhunagar')

courseentry = ttk.Combobox(window, textvariable=coursevalue, width = 24, font=('calibre',10,'normal'))
courseentry['value'] = ('Aeronautical Engineering','Aerospace Engineering','Automobile Engineering','Biotechnology Engine','Chemical Engineering',
                       'Civil Engineering','Computer Science Engineering','Electronics & Communication Engineering','Electrical and Electronics Engineering',
             'Marine Engineering','Mechanical Engineering','Nuclear Engineering')

courseentry.grid(row=26,column=1,padx=30, pady=10)
courseentry.current()

button = Button(window,command = summit_details,text="Summit",background="lightgray",foreground="black",font="ar 13 bold")
button.grid(row=36,column=1,padx=30, pady=10)


window.mainloop()
