from optparse import Values
import tkinter
import customtkinter  # <- import the CustomTkinter module



root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("800x540")
root_tk.title("URL Toolbox")

frame = customtkinter.CTkFrame(master=root_tk,
                               width=750,
                               height=415,
                               corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def shorten():
    pass

def extend():
    pass

def click_counter():
    pass

def flyer():
    pass


def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=.93, anchor=tkinter.CENTER)

optionmenu_var = customtkinter.StringVar(value="URL Shortener")  # set initial value


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu_dropdown = customtkinter.CTkComboBox(master=root_tk,
                                     values=["URL Shortener", "URL Extender", "URL Click Generator", "Digital Flyer Generator"],
                                     command=optionmenu_callback, #need to pass two arguments here
                                     variable=optionmenu_var)
optionmenu_dropdown.pack(padx=20, pady=10)

if optionmenu_callback("URL Shortener"):
    shorten()


def shorten():
    pass

def extend():
    pass

def click_counter():
    pass

def flyer():
    pass



root_tk.mainloop()