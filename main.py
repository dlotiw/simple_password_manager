from tkinter import *
import pandas
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator(length=22):
    length = size.get()
    password = ""
    for _ in range(length):
        what = random.choice(['d','z','m','l'])
        if what == 'm':
            password += chr(random.randint(97,122))
        elif what == 'd':
            password += chr(random.randint(65,90))
        elif what == 'z':
            password += random.choice(['?','!','_',",",'*'])
        else:
            password += str(random.randint(0,9))
    return password
    #65-90 Duze
    #97-122 male
    
def gen_click():
    password = password_generator()
    pass_e.focus()
    pass_e.delete(0,"end")
    pass_e.insert(0, password)
    # pass_e.insert(END, string=password)
    

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
num_l = Label(text="Password Length")
num_l.grid(row=4,column=0)

#TextEntry
web_e = Entry(width=58)
web_e.grid(row=1,column=1,columnspan=2,sticky="e",pady=10)
user_e = Entry(width=58)
user_e.grid(row=2,column=1,columnspan=2,sticky="e",pady=10)
pass_e = Entry(width=35)
pass_e.grid(row=3,column=1,columnspan=1,sticky="w",padx=8,pady=10)

#Button
gen_buton = Button(text="Generate password",command=gen_click)
gen_buton.grid(row=3,column=2,sticky="e")
add_button = Button(text="Add",width=50)
add_button.grid(row=5,column=1,columnspan=2)

#Scale
size = Scale(from_=10, to=35,orient="horizontal")
size.grid(row=4,column=1,columnspan=2,pady=(0,10))
window.mainloop()