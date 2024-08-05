from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open('/Users/macintosh/Desktop/data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=f'Error', message=f'No data file found.')
    else:
        if website in data:
            username = data[website]['username']
            password = data[website]['password']
            show_info = messagebox.showinfo(title=f'{website}', message=f'Username: {username}\nPassword: {password}')
        else:
            messagebox.showinfo(title=f'Error', message=f'No details for {website} exists.')
    

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
    new_data = {
        website: {
            'username': username,
            'password': password
            }
        }
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        is_empty = messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    
    else:
        try:
            with open('/Users/macintosh/Desktop/data.json', 'r') as file:
                # Reading old data
                data = json.load(file)
                
        except FileNotFoundError:
            with open('/Users/macintosh/Desktop/data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        
        else:
            # Updating old data with new data
            data.update(new_data)
            
            with open('/Users/macintosh/Desktop/data.json', 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
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
website_entry = Entry(width=21)
website_entry.grid(row=2, column=2)
website_entry.focus()

username_entry = Entry(width=39)
username_entry.grid(row=3, column=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=4, column=2)

# Buttons
search_button = Button(text='Search', width=13, command=search)
search_button.grid(row=2, column=3)

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=4, column=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=5, column=2, columnspan=2)


window.mainloop()
   
