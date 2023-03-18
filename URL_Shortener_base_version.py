import _tkinter
import tkinter as tk
import pyshorteners

#steps to initialize Tkinter GUI
root = tk.Tk()
root.title("URL Shortener and Compiler")
root.geometry("750x750")

#function that shortens URL
def shorten():
    if final_entry.get():
        final_entry.delete(0, tk.END)

    if my_entry.get():
        #convert to tiny url (bitly service available too, but need API key)
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        #project to screen
        final_entry.insert(tk.END, url)

my_label_top = tk.Label(root, text = "Enter URL to Shorten", font = ("Helvetica", 24))
my_label_top.pack(pady=10)

my_entry = tk.Entry(root, font = ("Helvetica", 24), width=40)
my_entry.pack(pady=50)

my_button = tk.Button(root, text = "Shorten Link", command=shorten, font=("Helvetica", 32))
my_button.pack(pady=70)

final_label = tk.Label(root, text="Shortened URL", font=("Helvetica", 24))
final_label.pack(pady=60)

final_entry = tk.Entry(root, font=("Helvetica", 24), justify=tk.CENTER, width=40, bd=0, bg="systembuttonface")
final_entry.pack(pady=1)

#Running the GUI
root.mainloop()


