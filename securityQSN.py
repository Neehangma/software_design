from tkinter import *
from PIL import Image,ImageTk

#initialie main window
root=Tk()
root.geometry('700x700')
root.resizable(0, 0)
root.title('Student Management System')
a=Label(root,text='Sign Up',fg='black',font=('Bold',20)).place(x='425',y='155')
b=Label(root,text='Security Questions',fg='black',font=('Bold',15)).place(x='400',y='210')
c=Label(root,text='1.What is your favourite colour?',fg='black',font=('Bold',12)).place(x='400',y='275')
e1 = Entry(root).place(x='405',y='305')
d=Label(root,text='2.What is your dream destination?',fg='black',font=('Bold',12)).place(x='400',y='335')
e2 = Entry(root).place(x='405',y='365')
e=Label(root,text='3.What kind of music do you like?',fg='black',font=('Bold',12)).place(x='400',y='395')
e5 = Entry(root).place(x='405',y='425')

f=Label(root,text='THE GODOLPHIN AND LATYMER SCHOOL',fg='black',font=('Bold',25)).place(x='15',y='20')

mainloop()