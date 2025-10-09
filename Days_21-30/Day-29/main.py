from tkinter import *
from tkinter import messagebox
from random import choice,shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters_=[choice(letters) for _ in range(0,12)]
    numbers_=[choice(numbers) for _ in range(2,4)]
    symbols_=[choice(symbols) for _ in range(2,4)]
    password_list=letters_+numbers_+symbols_
    shuffle(password_list)
    password="".join(password_list)   # this joins the list into a string
    pyperclip.copy(password)   # copy password to clipboard for easy pasting into other applications
    password_entry.insert(0,password)   # this inserts the password into the password entry field

# ---------------------------- SAVE PASSWORD to DATA.TXT------------------------------- #
def add_data():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={website:{"email":email,"password":password}}

    if website=="" or email=="" or len(password)<6:
        messagebox.showinfo(title="Error",message="Please check your fields!")
    else:
        with open("data.json", "r+") as data_file:
            data = json.load(data_file)
            data.update(new_data)
            data_file.seek(0)  # Move to the start of the file
            json.dump(data, data_file, indent=4)
            data_file.truncate()  # Remove any remaining content if new content is shorter
        # Clear the entries
        website_entry.delete(0, END)
        password_entry.delete(0, END)

#------------------------------Search-----------------------------------#
def search():
    website = website_entry.get().strip().lower()

    # Normalize the website name by removing 'ww
    # w.' and '.com' if present
    normalized_website = website.replace('www.', '').split('.')[0]
    
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

            # Check both the exact match and normalized version
            for site in data:
                normalized_site = site.replace('www.', '').split('.')[0]
                if normalized_website == normalized_site:
                    email = data[site]["email"]
                    password = data [site]["password"]
                    pyperclip.copy(password)   #this will copy the password into clipboard
                    messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {password}")
                    return
            messagebox.showinfo(title="Error", message="No data found for this website")
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1,pady=(0,20))

# Website
website_label = Label(text="Website:",font=("Arial",12,"bold"))
website_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
website_entry = Entry(width=35,font=("Arial",12))

website_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
website_entry.focus()

# Search
search_button=Button(text="Search",font=("Arial",12,"bold"),command=search)
search_button.grid(row=1,column=2,sticky="w", padx=25, pady=5)

# Email/Username
email_label = Label(text="Email/Username:",font=("Arial",12,"bold"))
email_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
email_entry = Entry(width=35,font=("Arial",12))
email_entry.insert(0,"driss_fadal@hotmail.com") #default text
email_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=5)
# Password
password_label=Label(text="Password:",font=("Arial",12,"bold"))
password_label.grid(row=3,column=0,sticky="e", padx=5, pady=5 )
password_entry=Entry(width=21,font=("Arial",12))
password_entry.grid(row=3,column=1,sticky="w", padx=5, pady=5)
# Buttons
generate_button=Button(text="Generate",font=("Arial",12,"bold"),command=generate_password)
generate_button.grid(row=3,column=2,sticky="w", padx=15, pady=5)

add_button=Button(text="Add",width=28,font=("Arial",12,"bold"),command=add_data)
add_button.grid(row=4,column=1,columnspan=2,pady=10)



window.mainloop()




