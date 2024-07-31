from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [choice(letters) for i in range(randint(8,10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    
    shuffle(password_list)
    
    password = ''.join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password) # Copy to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        is_empty = messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    
    else:
        is_ok = messagebox.askokcancel(title='website', message=f'These are the details entered: \nEmail/Username: {username}\nPassword:{password}\nIs it okay to save?')
        
        if is_ok:
            with open('/Users/macintosh/Desktop/data.txt', 'a') as file:
                file.write(f'{website} | {username} | {password}\n')
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file='/Users/macintosh/Downloads/password-manager-start/logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(row=1, column=2)

#Labels
website_label = Label(text='Website:')
website_label.grid(row=2, column=1)

username_label = Label(text='Email/Username:')
username_label.grid(row=3, column=1)

password_label = Label(text='Password:', width=21)
password_label.grid(row=4, column=1)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=3, column=2, columnspan=2)

password_entry = Entry()
password_entry.grid(row=4, column=2)

# Buttons
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=4, column=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=5, column=2, columnspan=2)


window.mainloop()
