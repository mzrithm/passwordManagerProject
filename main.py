from tkinter import *
from tkinter import messagebox
import random
import pyperclip

default_username = "mzrithm@gmail.com"


def close_window():
    window.destroy()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_field.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for each in range(nr_letters)] + \
                    [random.choice(symbols) for each in range(nr_symbols)] + \
                    [random.choice(numbers) for each in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_field.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password", message="Your password has been copied to the clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    web = website_field.get()
    name = username_field.get()
    pw = password_field.get()

    if len(web) == 0 or len(pw) == 0:
        messagebox.showerror(title="Error", message="One or more fields are empty!")
    else:
        new_entry = f'{web} | {name} | {pw}\n'

        message = f'Website: {web}\n \nUsername: {name}\n \nPassword: {pw}\n \nIs it ok to save?'
        is_ok = messagebox.askokcancel(title=web, message=message)
        if is_ok:
            with open("data.txt", 'a') as file:
                file.write(new_entry)

        website_field.delete(0, "end")
        username_field.delete(0, "end")
        username_field.insert(0, default_username)
        password_field.delete(0, "end")
        website_field.focus()


# save entry into file data.txt -> website | username | password
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#FFFFFF")

# create canvas widget
canvas = Canvas(width=200, height=200, bg="#FFFFFF", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=1, columnspan=2)

# create website field
website_field = Entry(width=35)
website_field.focus()
# website_field.insert(END, website)
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
website_field.grid(column=1, row=2, columnspan=2)

# create email/username field
username_field = Entry(width=35)
username_field.insert(0, default_username)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=3)
username_field.grid(column=1, row=3, columnspan=2)

# create password field
password_field = Entry(width=21)
# password_field.insert(END, password)
password_label = Label(text="Password:")
password_button = Button(text="Generate Password", command=generate_password)
password_label.grid(column=0, row=4)
password_field.grid(column=1, row=4, columnspan=1)
password_button.grid(column=2, row=4, columnspan=1)

# add entry button
add_entry_button = Button(text="Add", command=add_entry)
add_entry_button.config(width=36)
add_entry_button.grid(column=1, row=5, columnspan=2)

# add exit button
exit_button = Button(text="Quit", command=close_window)
exit_button.config(width=10)
exit_button.grid(column=3, row=0)

window.mainloop()
