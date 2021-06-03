from tkinter import *
master = Tk()
master.title("Exception Handling")
master.geometry("600x400")
master.config(bg="#ae2012")
lbl1 = Label(master, text="Please Enter amount in your account:")
lbl1.place(x=10, y=50)
entry1 = Entry(master, width=30)
entry1.place(x=300, y=50)



from tkinter import messagebox
def verify():
    funds = entry1.get()
    try:
        funds = int(funds)
        if funds < 3000:
            messagebox.showerror("STATUS", 'Please deposit more funds for this excursion')
        else:
            messagebox.showinfo("PERMiSION", "You qualify fro the Malysia trip. Cogratulations.")
    except ValueError:
            messagebox.showerror("Feedback, Error PLease insert funds.")


btn_verify = Button(master, text="Check Qualification", borderwidth=5, command=verify)
btn_verify.place(x=150, y=200)






master.mainloop()
