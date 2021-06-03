from tkinter import *
root = Tk()
root.title("Authentication")
root.geometry("600x600")
root.config(bg="#ff7b00")

# Creating a widgets
l1 = Label(root, text="Please Enter Log In Details", width=50)
l1.place(x=120, y=10)

# Username
l2 = Label(root, text="Username", width=30)
l2.place(x=200, y=100)
e1 = Entry(root, borderwidth=5)
e1.place(x=220, y=150)

# Password
l3 = Label(root, text="Password", width=30)
l3.place(x=200, y=250)
e2 = Entry(root, borderwidth=5, show="*")
e2.place(x=220, y=300)


# Defining a Function for logging in

def login():
   # importing message box
    from tkinter import messagebox
    Username = ["Zipho", "Masi", "Lihle", "Thandokazi"]
    Password = ["555", "333", "200", "221"]
    found = False
    for x in range(len(Username)):
        if e1.get()==Username[x] and e2.get()==Password[x]:
            found = True
        if found==True:
            messagebox.showinfo("PERMISSION", "ACCESS GRANTED")
            root.destroy()
            import Exception_Page
        else:
            messagebox.showinfo("ERROR INFO", "ACCESS DENIED")

# Defining a function for clearing
def clear():
    e1.delete(0, END)
    e2.delete(0, END)


# Button
b1 = Button(root, text="Login", borderwidth=5, width=10, command=login)
b1.place(x=250, y=400)



root.mainloop()






