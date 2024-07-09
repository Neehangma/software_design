
from tkinter import *
from PIL import Image, ImageTk

# Initialize the main window
root = Tk()
root.geometry('600x600')
root.title('Student Management System')

# Load the image using Pillow
image = Image.open('login page background.png')
photo = ImageTk.PhotoImage(image)

# # Create a label widget to display the image as a background
a = Label(root, image=photo).place(x='180',y='40')



# Create a frame with a transparent background (no background color set)
#n= Frame(root, highlightbackground="#273b7a", highlightthickness=3).place(x=50, y=50, width=300, height=600)

# Add other widgets on top of the background
a=Label(root,text='Login',fg='black',font=('Bold',14)).place(x='485',y='155')
button1 = Button(text="Login",fg="black",bg = "pink").place(x='485',y='310')
e1 = Entry(root).place(x='450',y='250')

button2=Button(text='forgot password?',fg='black',bg='pink',font=('Bold',6)).place(x='513',y='275')
c=Label(root,text='password',fg='black',font=('Bold',8)).place(x='450',y='230')
e2=Entry(root).place(x='450',y='210')
d=Label(root,text='username',fg='black',font=('Bold',8)).place(x='450',y='190')
e=Label(root,text='New User?',fg='black',font=('Bold',8)).place(x='500',y='400')
button2=Button(text='Sign Up Now',fg="black",bg='pink',font=('Bold',8)).place(x='490',y='420')

# Keep the window open
root.mainloop()
