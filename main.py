from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("Go go gadget password!")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    print("Julee, do the thing!")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="#FFFFFF")

# create canvas widget
canvas = Canvas(width=200, height=200, bg="#FFFFFF", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# create website field
# website = ""
website_field = Entry(width=35)
# website_field.insert(END, website)
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_field.grid(column=1, row=1, columnspan=2)

#create email/username field
# username = ""
username_field = Entry(width=35)
# username_field.insert(END, username)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_field.grid(column=1, row=2, columnspan=2)

#create password field
# password = ""
password_field = Entry(width=21)
# password_field.insert(END, password)
password_label = Label(text="Password:")
password_button = Button(text="Generate Password", command=generate_password)
password_label.grid(column=0, row=3)
password_field.grid(column=1, row=3, columnspan=1)
password_button.grid(column=2, row=3, columnspan=1)

#add entry button
add_entry_button = Button(text="Add", command=add_entry)
add_entry_button.config(width=36)
add_entry_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
