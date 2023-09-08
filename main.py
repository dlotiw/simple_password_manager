from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

#Screen setup
window = Tk()
window.title("Simple Password Manager")
window.config(padx=20,pady=20)

#Image
canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="Day29/simple_password_manager/logo2.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

#Labels
web_l = Label(text="Website")
web_l.grid(row=1,column=0)
user_l = Label(text="Email/Username")
user_l.grid(row=2,column=0)
pass_l = Label(text="Password")
pass_l.grid(row=3,column=0)

#TextEntry
web_e = Entry(width=58)
web_e.grid(row=1,column=1,columnspan=2,sticky="e",pady=10)
user_e = Entry(width=58)
user_e.grid(row=2,column=1,columnspan=2,sticky="e",pady=10)
pass_e = Entry(width=32)
pass_e.grid(row=3,column=1,columnspan=1,sticky="w",padx=8,pady=10)

#Button
gen_buton = Button(text="Generate password")
gen_buton.grid(row=3,column=2,sticky="e")
add_button = Button(text="Add",width=50)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()