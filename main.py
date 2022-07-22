from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip

BEIGE ="#FFE3A9"
GREEN="#BAFFB4"
DARK_BLUE = "#0078AA"
SKY_BLUE = "#3AB4F2"
PINK = "#FF5D5D"
SAFFRON="#FFAB76"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    alphabets =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers=[1,2,3,4,5,6,7,8,9,0]
    specials = ["!","@","#","$","%","&","*","(",")","/","~"]

    final_pass=[]

    num_small_chars = random.randint(2,3)
    capital_chars = random.randint(2,3)
    num_chars = random.randint(1,2)
    special_chars = random.randint(1,2)


    final_pass+=[alphabets[random.randint(0,25)] for x in range(0,num_small_chars)]



    final_pass += [alphabets[random.randint(0,25)].upper() for x in range(0,capital_chars)]


    final_pass += [str(random.randint(0,9)) for x in range(0,num_chars)]


    final_pass += [specials[random.randint(0,10)] for x in range(0,special_chars)]
    random.shuffle(final_pass)


    result = ""
    for x in final_pass:
        result += x
    pyperclip.copy(result)
    password_input.insert(0,result)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    no_blank_fields=True
    website_saved = website_input.get().lower()
    user_saved = user_input.get()
    pass_saved = password_input.get()
    dict_saved = {website_saved: {
        "email": user_saved,
        "password": pass_saved
    }
    }
    if len(website_saved)==0 or len(user_saved)==0 or len(pass_saved)==0:
        messagebox.showinfo(title="Fields Empty!", message="No fields should be left empty")
        no_blank_fields = False

    else:
        confirm = messagebox.askyesno(title="Password Saving Confirmation",
                                  message=f"Do you want to save the following? \n Website : "
                                          f"{website_saved}\n Username : {user_saved}\n "
                                          f"Password: {pass_saved}")

    if no_blank_fields and confirm:
        #file = open("data.txt","a")
        #file.write(f"{website_saved} | {user_saved} | {pass_saved}\n")
        #file.close()
        try:
            with open("data.json","r") as file:
                curr_data = json.load(file)
        except FileNotFoundError:
            print("snkjsn")
            with open("data.json","w") as file:
                json.dump(dict_saved,file,indent=3)
        else:
            curr_data.update(dict_saved)

            with open("data.json","w") as file:
                json.dump(curr_data,file,indent=3)
        finally:
            website_input.delete(0,"end")
            user_input.delete(0,"end")
            password_input.delete(0, "end")
            website_input.focus()
            messagebox.showinfo(title="Password Saved", message = "Your password has been successfully saved!")

#----------INFORMATION SEARCHING----------------#
def searcher():
    website_searched = website_input.get().lower()
    try:
        with open("data.json","r") as file:
            data_collected = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Unsucessful Passoword Retrival", message="No Entries Saved Found!")
    else:
        for x in data_collected:
            if x == website_searched:
                collected_creditentials= data_collected[x]
                email_collected = collected_creditentials["email"]
                password_collected = collected_creditentials["password"]
                messagebox.showinfo(title="Password Retrived", message =f"Email/Username :{email_collected} \n"
                                                                        f" Password: {password_collected}")
                return
        raise ValueError("No such Website Saved Found!")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=55,pady=55,bg=GREEN)
window.title("My Password Manger")


canvas = Canvas(width=200,height=200,bg=GREEN,highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=password_image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website",fg=SAFFRON,bg=GREEN,highlightthickness=0)
website_label.grid(row=1,column=0)

website_input = Entry()
website_input.config(fg="#FFAB76",highlightthickness=0,width=23)
website_input.grid(row=1,column=1)
website_input.focus()



user_label = Label(text="Email/Username",fg=SAFFRON,bg=GREEN,highlightthickness=0)
user_label.grid(row=2,column=0)

user_input = Entry()
user_input.config(fg="#FFAB76",highlightthickness=0,width=41)
user_input.grid(row=2,column=1,columnspan=2)


password_label = Label(text="Password",fg=SAFFRON,bg=GREEN,highlightthickness=0)
password_label.grid(row=3,column=0)


password_input = Entry()
password_input.config(fg="#FFAB76",highlightthickness=0,width=23)
password_input.grid(row=3,column=1)


password_generator = Button(text="Generate Password!",fg=SAFFRON,bg=GREEN,highlightthickness=0,command = pass_generator)
password_generator.grid(row=3,column=2,columnspan=1)


add_button = Button(text="Add!",fg=SAFFRON,bg=GREEN,highlightthickness=0,width=42,command=add)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",fg=SAFFRON,bg=GREEN,highlightthickness=0,command = searcher)
search_button.grid(row=1,column=2,columnspan=1)




window.mainloop()