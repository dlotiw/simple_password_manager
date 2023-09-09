from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
from cryptography.fernet import Fernet

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator(length=22):
    length = size.get()
    password = ""
    for _ in range(length):
        #m - small letter, d-large letters, l - numbers, z - special_chars
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
#TODO copy to clipboard using pyperclip
def gen_click():
    password = password_generator()
    pass_e.focus()
    pass_e.delete(0,"end")
    pass_e.insert(0, password)

    

# ---------------------------- SAVE PASSWORD ------------------------------- #
#TODO Add popup, empty field validation
def add_click():
    try:
        d = pd.read_csv("passwords.csv")
    except FileNotFoundError:
        d = {
            'website': [],
            'username/email':[],
            'passwords': []
        }
    
    if type(d) == dict:
        d['website'].append(web_e.get())
        d['username/email'].append(user_e.get())
        d['passwords'].append(pass_e.get())
        df = pd.DataFrame.from_dict(data=d)
        df.to_csv("passwords.csv",index=False)
        
    else:
        d.loc[0 if pd.isnull(d.index.max()) else d.index.max() + 1] = [web_e.get(),user_e.get(),pass_e.get()]
        d.to_csv("passwords.csv",index=False)
        print(d)
        
        

#------------------------------Ecryption-------------------------------------------#
#TODO repair decryption
def encrypt(file):
    with open('crypt+key.key','r') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(file,'r') as filet:
        org = filet.read()
    enc=fernet.encrypt(org)
    with open(file,'w') as enc_file:
        enc_file.write(enc)

def decrypt(file):
    with open('crypt+key.key','r') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(file,'r') as filet:
        dec = filet.read()
    org=fernet.decrypt(dec)
    with open(file,'w') as org_file:
        org_file.write(org)
    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
            encrypt('passwords.csv')
            window.destroy()
      

# ---------------------------- UI SETUP ------------------------------- #

#TODO a way to view all stored passwords
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
add_button = Button(text="Add",width=50,command=add_click)
add_button.grid(row=5,column=1,columnspan=2)

#Scale
size = Scale(from_=10, to=35,orient="horizontal")
size.grid(row=4,column=1,columnspan=2,pady=(0,10))
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()