
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
#initialie main window
root=Tk()
root.geometry('700x700')
root.title('Student Management System')

image_path = "PImage.jpg"  # Update this to the correct path
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
a = Label(root, image=photo)
a.grid(row='0',column='0')

a=Label(root,text='Sign Up',fg='black',font=('Bold',20))
a.place(x='460',y='150')
b=Label(root,text='First Name',fg='black',font=('Bold',12))
b.place(x='400',y='210')
e1 = Entry(root).place(x='390',y='235')
c=Label(root,text='Last Name',fg='black',font=('Bold',12))
c.place(x='540',y='210')
e2 = Entry(root).place(x='530',y='235')
c=Label(root,text='Enter Your Email',fg='black',font=('Bold',12))
c.place(x='400',y='270')
e3 = Entry(root).place(x='390',y='295')
d=Label(root,text='Enter Your Phone Number',fg='black',font=('Bold',12))
d.place(x='400',y='325')
e4 = Entry(root).place(x='390',y='350')
e=Label(root,text='Current Password',fg='black',font=('Bold',12))
e.place(x='400',y='380')
e5 = Entry(root).place(x='390',y='405')
f=Label(root,text='Confirm Password',fg='black',font=('Bold',12))
f.place(x='400',y='435')
e6 = Entry(root).place(x='390',y='455')

mybutton=Button(root,text='Back To Login',fg='black',bg='pink',font=('bold',10)).place(x='400',y='500')
mybutton=Button(root,text='Next',fg='black',bg='pink',font=('bold',10)).place(x='550',y='500')


def Login_Error():
    messagebox.showinfo("Title", text="SignUp error",font=('bold',20))



mainloop()