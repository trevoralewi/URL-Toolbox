#Required modules
from optparse import Values
from tkinter import *
import tkinter
from tkinter import filedialog as fd
from turtle import bgcolor
import customtkinter 
import pyshorteners
import qrcode
from PIL import ImageTk, Image, ImageDraw, ImageFont
import numpy as np
import textwrap
import re
from urllib.parse import urlparse


#main app class
class URLToolbox:
    #Option menu selection of tools
    def optionmenu_select(self, choice):
        print("optionmenu dropdown clicked:", choice)
        if choice == "URL Shortener":
            self.frame.place_forget()
            self.frame_C.pack_forget()
            self.frame_D.pack_forget()
            self.frame_A.pack(padx=35, pady=25, fill=tkinter.BOTH, expand=True)
            self.shorten_window()

        elif choice == "QR Code Generator":
            self.frame.place_forget()
            self.frame_A.pack_forget()
            self.frame_D.pack_forget()
            self.frame_C.pack(padx=35, pady=25, fill=tkinter.BOTH, expand=True)
            self.QR_code_window()
        elif choice == "Digital Flyer Generator":
            self.frame.place_forget()
            self.frame_A.pack_forget()
            self.frame_C.pack_forget()
            self.frame_D.pack(padx=35, pady=25, fill=tkinter.BOTH, expand=True)
            self.flyer_window()
        else:
            print("Error Found")


#Initilization of root and base widgets
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x750")
        self.master.title("URL Toolbox")
        
        self.frame_A = customtkinter.CTkFrame(master=self.master, width=750,
                                   height=675,
                                   corner_radius=10)
        self.frame_A.pack(padx=0.5, pady=0.5, anchor=tkinter.CENTER)
        self.frame_A.pack_forget()
        self.frame_C = customtkinter.CTkFrame(master=master,
                                       width=750,
                                       height=675,
                                       corner_radius=10)
        self.frame_C.pack(padx=0.5, pady=0.5, anchor=tkinter.CENTER)
        self.frame_C.pack_forget()


        self.frame_D = customtkinter.CTkFrame(master=master,
                                       width=1000,
                                       height=700,
                                       corner_radius=10)
        self.frame_D.pack(padx=0.5, pady=0.5, anchor=tkinter.CENTER)
        self.frame_D.pack_forget()

        self.frame_D2 = customtkinter.CTkFrame(master=self.frame_D, width=405,
                                height=225,
                                corner_radius=10, fg_color="silver")
        self.frame_D2.place(relx=.017, rely=.65,) 

        self.var_default="Select Function"
        self.optionmenu_var = customtkinter.StringVar(value=self.var_default)  # set initial value

        self.optionmenu_dropdown = customtkinter.CTkComboBox(master=self.master, width=165,
                                                values=["URL Shortener", "QR Code Generator", "Digital Flyer Generator"],
                                                command=self.optionmenu_select,
                                                variable=self.optionmenu_var)
        self.optionmenu_dropdown.pack(padx=.5, pady=.18)

        self.frame = customtkinter.CTkFrame(master=self.master, width=740, height=675, corner_radius=10)
        self.frame.place(relx=0.5, rely=0.51, anchor=tkinter.CENTER, width=740, height=675)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # Landing page canvas
        self.canvas_main = Canvas(master=self.frame, width=740, height=675)
        self.canvas_main.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")

        self.maincanvas_pic=Image.open("URL Toolkit Folder\Mainpage.png")
        self.maincanvas_pic = self.maincanvas_pic.resize((740,675))
        self.maincanvas_pic.save("URL Toolkit Folder\Mainpage-re.png")
        self.maincanvas_pic = ImageTk.PhotoImage(Image.open("URL Toolkit Folder\Mainpage-re.png"))
        self.image_on_canvas = self.canvas_main.create_image(370, 337.5, image=self.maincanvas_pic, anchor=tkinter.CENTER)

        self.canvas_D = Canvas(master=self.frame_D2, width=125, height=175)
        self.canvas_image = self.canvas_D.create_image(62.5, 87.5, anchor=tkinter.CENTER)


        #Example elements for flyer method
        self.dark_example_f = Image.open("URL Toolkit Folder\Dark Flyer Example.PNG")
        self.dark_example_f = self.dark_example_f.resize((125, 175))
        self.dark_example_f = ImageTk.PhotoImage(self.dark_example_f)

        self.blue_example_f = Image.open("URL Toolkit Folder\Blue Image Example.PNG")
        self.blue_example_f = self.blue_example_f.resize((125, 175))
        self.blue_example_f = ImageTk.PhotoImage(self.blue_example_f)

        self.orange_example_f = Image.open("URL Toolkit Folder\Orange Flyer Example.PNG")
        self.orange_example_f = self.orange_example_f.resize((125, 175))
        self.orange_example_f = ImageTk.PhotoImage(self.orange_example_f)


    #Start of URL Shortener methods
    def shorten(self):
        # Check if the user has entered a valid URL in the entry field
        url = self.entry.get()
        if not urlparse(url).scheme:
            # If the URL does not include a scheme (e.g. "http" or "https"),
            # add "http" as the default scheme
            url = "http://" + url
        # Check if the resulting URL is valid
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            # Display a pop-up window if the URL is invalid
            self.window_ishort = customtkinter.CTkToplevel()
            self.window_ishort.geometry("600x300")
            self.label_ishort = customtkinter.CTkLabel(self.window_ishort, text="Please provide a valid URL \n in the entry field to shorten.", text_font=("Helvetica", 16, "bold"))
            self.label_ishort.pack(side="top", fill="both", expand=True, padx=40, pady=40)
            return
        # If the URL is valid, proceed with the URL shortening process
        if self.entry2.get():
            self.entry2.delete(0, customtkinter.END)
        if self.entry.get():
            # Convert to tiny url (bitly service available too, but need API key)
            url = pyshorteners.Shortener().tinyurl.short(url)
            # Project to screen
            self.entry2.insert(customtkinter.END, url)

    # Additional window with helpful tips for URL shortener tool
    def shorten_help(self):
        self.window_shelp = customtkinter.CTkToplevel()
        self.window_shelp.geometry("900x500")
        self.canvas_shortenhelp = Canvas(self.window_shelp, width=900, height=500)
        self.canvas_shortenhelp.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")
        self.shortenhelp_pic = ImageTk.PhotoImage(Image.open("URL Toolkit Folder\\URL Shortener Helpful Tips.png"))
        self.shortenhelp_on_canvas = self.canvas_shortenhelp.create_image(450, 250, image=self.shortenhelp_pic, anchor=tkinter.CENTER)
        
    # Tkinter widgets 
    def shorten_window(self):       
        self.master.geometry("800x750")

        self.text_var = tkinter.StringVar(value="Enter Link to Shorten")

        self.label_SH = customtkinter.CTkLabel(master=self.frame_A,
                                    text="URL Shortener",
                                    width=340,
                                    height=55,
                                    text_font=("Helvetica", 32, "bold"),
                                    fg_color=("#d1d5d8", "gray75"),
                                    corner_radius=8, bg_color="#d1d5d8")
        self.label_SH.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER) 

        self.label = customtkinter.CTkLabel(self.frame_A,
                                    textvariable=self.text_var,
                                    width=340,
                                    height=75,
                                    text_font=("Lato", 24),
                                    fg_color=("#d1d5d8", "gray75"),
                                    corner_radius=8, bg_color="#d1d5d8")
        self.label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    

        self.entry = customtkinter.CTkEntry(self.frame_A,
                                placeholder_text="Paste URL you wish to shorten here",
                                width=500,
                                height=40,
                                border_width=2,
                                corner_radius=10, bg_color="#d1d5d8")
        self.entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        

        self.label2 = customtkinter.CTkLabel(master=self.frame_A,
                                    text = "Shortened Link",
                                    width=340,
                                    height=75,
                                    text_font=("Helvetica", 24),
                                    fg_color=("#d1d5d8", "gray75"),
                                    corner_radius=8, bg_color="#d1d5d8")
        self.label2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.entry2 = customtkinter.CTkEntry(master=self.frame_A,
                                width=500,
                                height=40,
                                border_width=2,
                                corner_radius=10, bg_color="#d1d5d8")
        self.entry2.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        self.Q_pic=Image.open("URL Toolkit Folder\Question Mark.png")
        self.Q_pic = self.Q_pic.resize((30,30))
        self.Q_pic.save("URL Toolkit Folder\Question-Mark-resized.png")
        self.Q_pic=ImageTk.PhotoImage(Image.open("URL Toolkit Folder\Question-Mark-resized.png"))

        self.help_button_S = customtkinter.CTkButton(master=self.frame_A,
                                    width=30,
                                    height=30,
                                    border_width=0,
                                    border_color="#d1d5d8",
                                    fg_color="#d1d5d8",
                                    corner_radius=8,
                                    text="",
                                    image=self.Q_pic, command=self.shorten_help)
        self.help_button_S.place(relx=0.92, rely=0.05, anchor=tkinter.CENTER)

        self.help_label_S = customtkinter.CTkLabel(master=self.frame_A,
                text = "Need Help?",
                width=140,
                height=35,
                text_font=("Helvetica", 12),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.help_label_S.place(relx=0.92, rely=0.1, anchor=tkinter.CENTER)


        self.button2 = customtkinter.CTkButton(master=self.frame_A,
                                        width=180,
                                        height=35,
                                        text_font=("Helvetica", 18),
                                        border_width=0,
                                        corner_radius=8,
                                        text="Shorten URL",
                                        command=self.shorten, bg_color="#d1d5d8")
        self.button2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

       
    # Start of QR code generator methods
    def qr_code(self):
        if self.entry.get():
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=7,
            border=4,
            )
            qr.add_data(self.entry.get())
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img_resize = img.resize((250,250))
            img_resize.save("qrcode.jpg")
             
                
            
            #Create a canvas
            self.canvasQR= Canvas(master=self.frame_C, width= 248, height= 248)
            
            #Load an image in the script
            self.pic=ImageTk.PhotoImage(Image.open("qrcode.jpg"))
        
            #Add image to the Canvas Items
            self.canvasQR.create_image(125,125,anchor=CENTER,image=self.pic)
            self.canvasQR.pack()
            self.canvasQR.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

            pic_file = fd.asksaveasfilename(
            filetypes=[("png file", ".png"), ("jpg file", ".jpg")],
            defaultextension=".png")
            if pic_file:  # user selected file
                img_resize.save(pic_file)
            else: # user cancel the file browser window
                print("No file chosen")  

    # New window with helpful tips for QR code generator tool
    def QR_help(self):
        self.window_QRhelp = customtkinter.CTkToplevel()
        self.window_QRhelp.geometry("900x500")
        self.canvas_QRhelp = Canvas(self.window_QRhelp, width=900, height=500)
        self.canvas_QRhelp.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")
        self.QRhelp_pic = ImageTk.PhotoImage(Image.open("URL Toolkit Folder\QR Generator Helpful Tips.png"))
        self.QRhelp_on_canvas = self.canvas_QRhelp.create_image(450, 250, image=self.QRhelp_pic, anchor=tkinter.CENTER)

    #QR code generator widgets
    def QR_code_window(self):
        self.text_var = tkinter.StringVar(value="To Create QR Code Paste Link Below")

        self.master.geometry("800x750")

        self.label_QRH = customtkinter.CTkLabel(master=self.frame_C,
                                    text="QR Code Generator",
                                    width=340,
                                    height=55,
                                    text_font=("Helvetica", 32, "bold"),
                                    fg_color=("#d1d5d8", "gray75"),
                                    corner_radius=8, bg_color="#d1d5d8")
        self.label_QRH.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER) 

        self.label = customtkinter.CTkLabel(master=self.frame_C,
                                    textvariable=self.text_var,
                                    width=340,
                                    height=75,
                                    text_font=("Helvetica", 24),
                                    fg_color=("#d1d5d8", "gray75"),
                                    corner_radius=8, bg_color="#d1d5d8")
        self.label.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

        self.entry = customtkinter.CTkEntry(master=self.frame_C,
                                placeholder_text="",
                                width=500,
                                height=40,
                                border_width=2,
                                corner_radius=10, bg_color="#d1d5d8")
        self.entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)


        self.label2 = customtkinter.CTkLabel(master=self.frame_C,
                                    text = "QR Code",
                                    width=340,
                                    height=75,
                                    text_font=("Helvetica", 24),
                                    fg_color=("#d1d5d8", "gray75"),
                                    corner_radius=8, bg_color="#d1d5d8")
        self.label2.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER)



        self.button2 = customtkinter.CTkButton(master=self.frame_C,
                                    width=180,
                                    height=35,
                                    text_font=("Helvetica", 18),
                                    border_width=0,
                                    corner_radius=8,
                                    text="Create QR Code",
                                    command=self.qr_code, bg_color="#d1d5d8")
        self.button2.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

        self.Q_pic=Image.open("URL Toolkit Folder\Question Mark.png")
        self.Q_pic = self.Q_pic.resize((30,30))
        self.Q_pic.save("URL Toolkit Folder\Question-Mark-resized.png")
        self.Q_pic=ImageTk.PhotoImage(Image.open("URL Toolkit Folder\Question-Mark-resized.png"))

        self.help_button_QR = customtkinter.CTkButton(master=self.frame_C,
                                    width=30,
                                    height=30,
                                    border_width=0,
                                    border_color="#d1d5d8",
                                    fg_color="#d1d5d8",
                                    corner_radius=8,
                                    text="",
                                    image=self.Q_pic, command=self.QR_help)
        self.help_button_QR.place(relx=0.92, rely=0.05, anchor=tkinter.CENTER)

        self.help_label_QR = customtkinter.CTkLabel(master=self.frame_C,
                text = "Need Help?",
                width=140,
                height=35,
                text_font=("Helvetica", 12),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.help_label_QR.place(relx=0.92, rely=0.1, anchor=tkinter.CENTER)



    #START OF FLYER METHODS
    def image_pull(self):
        # Open the file selection dialog and get the file path
        file_path = fd.askopenfilename(title="Select a File", filetype=(("png files", "*.png"),("jpg files", "*.jpg"),("JPEG files", "*.JPEG"))) 
            
        # Check if a file was selected
        if not file_path:
            raise Exception("No file was selected")
            # Try to open the image file
        try:
            self.file_image = Image.open(file_path)
        except Exception as e:
            raise Exception("Error opening file: {}".format(e))

        # Convert the image mode to "RGB"
        self.file_image = self.file_image.convert("RGB")            
        self.file_image_resized = self.file_image.resize((100,100))
        self.file_image_resized.save("Loaded Profile Pic.jpg")
        self.profile_image = ImageTk.PhotoImage(self.file_image_resized)
        self.canvas_C.create_image(100/2,100/2, anchor=tkinter.CENTER,image=self.profile_image,)
        self.canvas_C.pack()
        self.canvas_C.place(relx=0.5, rely=0.138, anchor=tkinter.CENTER)
        self.profile_var.set(1)
            
        
    #Checking if length of entry boxes is compatible for formatting 
    def check_len(self):
        if len(self.entry_A.get()) > 40:
            self.entry_A.delete(40, END)
        if len(self.entry_B.get()) > 400:
            self.entry_B.delete(400, END)
        if len(self.entry_C.get()) > 40:
            self.entry_C.delete(40, END)
        if len(self.entry_D.get()) > 40:
            self.entry_D.delete(40, END)
        if len(self.entry_E.get()) > 15:
            self.entry_E.delete(15, END)
        if len(self.entry_F.get()) > 40:
            self.entry_F.delete(40, END)
        if len(self.entry_G.get()) > 150:
            self.entry_G.delete(150, END)

        
    # Three different display methods for user to view color templates
    def orange_display(self):
        self.canvas_D.place(relx=0.7, rely=0.57, anchor=tkinter.CENTER)
        self.canvas_D.create_image(62.5, 87.5, image=self.orange_example_f, anchor=tkinter.CENTER)
        self.canvas_D.itemconfigure(self.canvas_image, image=self.orange_example_f)
        self.label_EX1.configure(text= "Orange Flyer Example")
        self.expand_button.place(relx=0.878, rely=0.15, anchor=tkinter.CENTER)

    def blue_display(self):
        self.canvas_D.place(relx=0.7, rely=0.57, anchor=tkinter.CENTER)
        self.canvas_D.create_image(62.5, 87.5, image=self.blue_example_f, anchor=tkinter.CENTER)
        self.canvas_D.itemconfigure(self.canvas_image, image=self.blue_example_f)
        self.label_EX1.configure(text= "Blue Flyer Example")
        self.expand_button.place(relx=0.878, rely=0.15, anchor=tkinter.CENTER)

    def dark_display(self):
        self.canvas_D.place(relx=0.7, rely=0.57, anchor=tkinter.CENTER)
        self.canvas_D.create_image(62.5, 87.5, image=self.dark_example_f, anchor=tkinter.CENTER)
        self.canvas_D.itemconfigure(self.canvas_image, image=self.dark_example_f)
        self.label_EX1.configure(text= "Dark Flyer Example")
        self.expand_button.place(relx=0.878, rely=0.15, anchor=tkinter.CENTER)


    #Method to expand color template examples
    def expand_event(self):
        if self.radio_var.get()==1:
            self.orange_example_f2=Image.open("URL Toolkit Folder\Orange Flyer Example.PNG")
            self.orange_example_f2.show()
        elif self.radio_var.get()==2:
            self.blue_example_f2=Image.open("URL Toolkit Folder\Blue Image Example.PNG")
            self.blue_example_f2.show()
        elif self.radio_var.get()==3:
            self.dark_example_f2=Image.open("URL Toolkit Folder\Dark Flyer Example.PNG")
            self.dark_example_f2.show()
    
    #New window for helpful tips for flyer generator
    def flyer_help(self):
        self.window_fhelp = customtkinter.CTkToplevel()
        self.window_fhelp.geometry("900x500")
        self.canvas_fhelp = Canvas(self.window_fhelp, width=900, height=500)
        self.canvas_fhelp.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")
        self.fhelp_pic = ImageTk.PhotoImage(Image.open("URL Toolkit Folder\Flyer Helpful Tips.png"))
        self.fhelp_on_canvas = self.canvas_fhelp.create_image(450, 250, image=self.fhelp_pic, anchor=tkinter.CENTER)

    #QR code maker for flyer method
    def QR_Maker(self):
        if self.entry_QR.get():
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=7,
            border=4,
            )
            qr.add_data(self.entry_QR.get())
            qr.make(fit=True)
            self.QR_img = qr.make_image(fill_color="black", back_color="white")
            self.QR_img = self.QR_img.resize((250,250))
            self.QR_img.save("qrcode_f.jpg")


    #Start of the three different colored template methods
    def orange_template(self):
        self.ot_img = Image.open("URL Toolkit Folder\Orange & White Elegant Business Flyer Potrait (2).png")
        self.orange_blank = Image.open("URL Toolkit Folder\Orange Blank.png")
        self.orange_blank = self.orange_blank.resize((500,500))
        self.header_img = self.file_image.resize((500,500))
        self.header_img.save("URL Toolkit Folder\Header Img.jpg")
        self.mask = Image.new("L", self.header_img.size, 0)
        self.draw = ImageDraw.Draw(self.mask)
        self.draw.ellipse((10, 10, 500, 500), fill=255,)
        self.header_img2 = Image.composite(self.header_img, self.orange_blank, self.mask)
        self.header_img2.save("URL Toolkit Folder\composite_circle.png", quality=95)
        self.header_img2 = Image.open("URL Toolkit Folder\composite_circle.png")       
        self.ot_img.paste(self.header_img2, (1000, 100))
        self.ot_img2 = ImageDraw.Draw(self.ot_img)
        self.my_header_font = ImageFont.truetype("C:\WINDOWS\FONTS\IMPACT.TTF", 102)
        self.my_tag_font = ImageFont.truetype("C:\WINDOWS\FONTS\STENCIL.TTF", 50)
        self.my_des_font = ImageFont.truetype("C:\WINDOWS\FONTS\IMPACT.TTF", 48)
        self.my_contact_font = ImageFont.truetype("C:\WINDOWS\FONTS\IMPACT.TTF", 32)
        self.my_QR_font = ImageFont.truetype("C:\WINDOWS\FONTS\IMPACT.TTF", 40)
        self.wrapper_d = textwrap.TextWrapper(width=70)
        self.wrapper_t = textwrap.TextWrapper(width=20)
        self.wrapper_tag = textwrap.TextWrapper(width=28)
        self.f_title = self.entry_A.get()
        self.f_title_w = self.wrapper_t.fill(text=self.f_title)
        self.f_des = self.entry_B.get()
        self.f_des_w = self.wrapper_d.fill(text=self.f_des)

        if self.check_var.get()=="on":
            url = pyshorteners.Shortener().tinyurl.short(self.entry_C.get())
            self.f_des2 = url
        if self.check_var.get()=="off":
            self.f_des2 = self.entry_C.get()
        self.f_des3 = self.entry_D.get()
        self.f_des4 = self.entry_E.get()
        self.f_des5 = self.entry_F.get()
        self.f_tag = self.entry_G.get()
        self.f_tag_w = self.wrapper_tag.fill(text=self.f_tag)
        self.contact_list = []
        self.contact_list.clear()
        self.contact_list.append(self.f_des2)
        if len(self.f_des2) == 0:
            self.contact_list.remove(self.f_des2)
        self.contact_list.append(self.f_des3)
        if len(self.f_des3) == 0:
            self.contact_list.remove(self.f_des3)
        self.contact_list.append(self.f_des4)
        if len(self.f_des4) == 0:
            self.contact_list.remove(self.f_des4)
        self.contact_list.append(self.f_des5)
        if len(self.f_des5) == 0:
            self.contact_list.remove(self.f_des5)
        self.contact_list =str(self.contact_list)
        self.contact_final=str(self.contact_list)
        self.contact_final=self.contact_final.replace(",","     |     ")
        self.contact_final=self.contact_final.replace("'","")
        self.contact_final=self.contact_final.replace("[","")
        self.contact_final=self.contact_final.replace("]","")

        

        self.ot_img2.text((70, 100), self.f_title_w, font=self.my_header_font, fill = "white", align = "center")
        self.ot_img2.text((110, 1000), self.f_des_w, font=self.my_des_font, fill = "black", align = "left")
        self.ot_img2.text((30, 1950), self.contact_final, font=self.my_contact_font, fill = "black", align = "left", spacing=60)
        self.ot_img2.text((110, 500), self.f_tag_w, font=self.my_tag_font, fill = "white", align = "left")

        

        if self.entry_QR.get():
            self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=7,
            border=4,
            )
            self.qr.add_data(self.entry_QR.get())
            self.qr.make(fit=True)
            self.QR_img_f = self.qr.make_image(fill_color="black", back_color="white")
            self.QR_img_f = self.QR_img_f.resize((500,500))
            self.QR_img_f.save("qrcode_f.jpg")
            self.ot_img.paste(self.QR_img_f, (525, 1450))
            self.ot_img2.text((640, 1420), "Scan Me!", font=self.my_QR_font, fill = "black", align = "center")       
        
        

        
        self.ot_img.show()
        self.OT_file = fd.asksaveasfilename(
        filetypes=[("png file", ".png"), ("jpg file", ".jpg")],
        defaultextension=".png")
        if self.OT_file:  # user selected file
            self.ot_img.save(self.OT_file)
        else: # user cancel the file browser window
            print("No file chosen")  





    def blue_template(self):
        self.bt_img = Image.open("URL Toolkit Folder\Light Blue Purple Simple Gradient Travel Poster (2).png")
        self.header_img = self.file_image.resize((1550,1000))
        self.header_img.save("URL Toolkit Folder\Header Img.jpg")
        self.header_img.copy()
        self.bt_img.paste(self.header_img, (85, 100))
        self.bt_img2 = ImageDraw.Draw(self.bt_img)
        self.my_header_font = ImageFont.truetype("C:\WINDOWS\FONTS\BOD_BLAR.TTF", 80)
        self.my_des_font = ImageFont.truetype("C:\WINDOWS\FONTS\BOD_BLAR.TTF", 50)
        self.my_contact_font = ImageFont.truetype("C:\WINDOWS\FONTS\BOD_BLAR.TTF", 24)
        self.my_QR_font = ImageFont.truetype("C:\WINDOWS\FONTS\BOD_CBI.TTF", 62)
        self.my_tag_font = ImageFont.truetype("C:\WINDOWS\FONTS\BOD_CBI.TTF", 62)
        self.wrapper_d = textwrap.TextWrapper(width=42)
        self.wrapper_t = textwrap.TextWrapper(width=32)
        self.wrapper_tag = textwrap.TextWrapper(width=48)
        self.f_title = self.entry_A.get()
        self.f_title_w = self.wrapper_t.fill(text=self.f_title)
        self.f_des = self.entry_B.get()
        self.f_des_w = self.wrapper_d.fill(text=self.f_des)
        if self.check_var.get()=="on":
            url = pyshorteners.Shortener().tinyurl.short(self.entry_C.get())
            self.f_des2 = url
        if self.check_var.get()=="off":
            self.f_des2 = self.entry_C.get()
        self.f_des3 = self.entry_D.get()
        self.f_des4 = self.entry_E.get()
        self.f_des5 = self.entry_F.get()
        self.f_tag = self.entry_G.get()
        self.f_tag_w = self.wrapper_tag.fill(text=self.f_tag)

        self.contact_list = []
        self.contact_list.clear()
        self.contact_list.append(self.f_des2)
        if len(self.f_des2) == 0:
            self.contact_list.remove(self.f_des2)
        self.contact_list.append(self.f_des3)
        if len(self.f_des3) == 0:
            self.contact_list.remove(self.f_des3)
        self.contact_list.append(self.f_des4)
        if len(self.f_des4) == 0:
            self.contact_list.remove(self.f_des4)
        self.contact_list.append(self.f_des5)
        if len(self.f_des5) == 0:
            self.contact_list.remove(self.f_des5)
        self.contact_list =str(self.contact_list)
        self.contact_final=str(self.contact_list)
        self.contact_final=self.contact_final.replace(",","|")
        self.contact_final=self.contact_final.replace("'","")
        self.contact_final=self.contact_final.replace("[","")
        self.contact_final=self.contact_final.replace("]","")

        self.bt_img2.text((80, 1110), self.f_title_w, font=self.my_header_font, fill = "mediumblue", align = "left")
        self.bt_img2.text((80, 1640), self.f_des_w, font=self.my_des_font, fill = "mediumblue", align = "left")
        self.bt_img2.text((25, 2250), self.contact_final, font=self.my_contact_font, fill = "mediumblue", align = "left")
        self.bt_img2.text((80, 1330), self.f_tag_w, font=self.my_tag_font, fill = "darkblue", align = "left")

        

        if self.entry_QR.get():
            self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=7,
            border=4,
            )
            self.qr.add_data(self.entry_QR.get())
            self.qr.make(fit=True)
            self.QR_img_f = self.qr.make_image(fill_color="blue", back_color="white")
            self.QR_img_f = self.QR_img_f.resize((215,215))
            self.QR_img_f.save("qrcode_f.jpg")
            self.bt_img.paste(self.QR_img_f, (1490, 2060))
            self.bt_img2.text((1512, 1970), "Scan Me!", font=self.my_QR_font, fill = "mediumblue", align = "center")
            

    
        self.bt_img.show()
        self.BT_file = fd.asksaveasfilename(
        filetypes=[("png file", ".png"), ("jpg file", ".jpg")],
        defaultextension=".png")
        if self.BT_file:  # user selected file
            self.bt_img.save(self.BT_file)
        else: # user cancel the file browser window
            print("No file chosen")  




    def dark_template(self):
        self.dt_img = Image.open("URL Toolkit Folder\Black And Brown Geometric Business Flyer (1).png")
        self.black_blank = Image.open("URL Toolkit Folder\Black Blank.png")
        self.black_blank = self.black_blank.resize((675,675))
        self.header_img = self.file_image.resize((675,675))
        self.header_img.save("URL Toolkit Folder\Header Img.jpg")
        mask = Image.new("L", self.header_img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((10, 10, 660, 660), fill=255,)
        self.header_img2 = Image.composite(self.header_img, self.black_blank, mask)
        self.header_img2.save("URL Toolkit Folder\composite_circle_B.png", quality=95)
        self.header_img2 = Image.open("URL Toolkit Folder\composite_circle_B.png")       
        self.dt_img.paste(self.header_img2, (915, 70))
        self.dt_img2 = ImageDraw.Draw(self.dt_img)
        self.my_header_font = ImageFont.truetype("C:\WINDOWS\FONTS\ELEPHNT.TTF", 85)
        self.my_tag_font = ImageFont.truetype("C:\WINDOWS\FONTS\ENGR.TTF", 52)
        self.my_des_font = ImageFont.truetype("C:\WINDOWS\FONTS\ENGR.TTF", 30)
        self.my_contact_font = ImageFont.truetype("C:\WINDOWS\FONTS\ENGR.TTF", 16)
        self.my_QR_font = ImageFont.truetype("C:\WINDOWS\FONTS\ENGR.TTF", 40)
        self.wrapper_d = textwrap.TextWrapper(width=40)
        self.wrapper_t = textwrap.TextWrapper(width=20)
        self.wrapper_tag = textwrap.TextWrapper(width=15)
        self.f_title = self.entry_A.get()
        self.f_title_w = self.wrapper_t.fill(text=self.f_title)
        self.f_des = self.entry_B.get()
        self.f_des_w = self.wrapper_d.fill(text=self.f_des)
        if self.check_var.get()=="on":
            url = pyshorteners.Shortener().tinyurl.short(self.entry_C.get())
            self.f_des2 = url
        if self.check_var.get()=="off":
            self.f_des2 = self.entry_C.get()
        self.f_des3 = self.entry_D.get()
        self.f_des4 = self.entry_E.get()
        self.f_des5 = self.entry_F.get()
        self.f_tag = self.entry_G.get()
        self.f_tag_w = self.wrapper_tag.fill(text=self.f_tag)

        self.contact_list = []
        self.contact_list.clear()
        self.contact_list.append(self.f_des2)
        if len(self.f_des2) == 0:
            self.contact_list.remove(self.f_des2)
        self.contact_list.append(self.f_des3)
        if len(self.f_des3) == 0:
            self.contact_list.remove(self.f_des3)
        self.contact_list.append(self.f_des4)
        if len(self.f_des4) == 0:
            self.contact_list.remove(self.f_des4)
        self.contact_list.append(self.f_des5)
        if len(self.f_des5) == 0:
            self.contact_list.remove(self.f_des5)
        self.contact_list =str(self.contact_list)
        self.contact_final=str(self.contact_list)
        self.contact_final=self.contact_final.replace(",","\n \n \n")
        self.contact_final=self.contact_final.replace("'","")
        self.contact_final=self.contact_final.replace("[","")
        self.contact_final=self.contact_final.replace("]","")



        self.dt_img2.text((50, 260), self.f_title_w, font=self.my_header_font, fill = "white", align = "left")
        self.dt_img2.text((50, 1320), self.f_des_w, font=self.my_des_font, fill = "white", align = "left")
        self.dt_img2.text((50, 600), self.f_tag_w, font=self.my_tag_font, fill = "goldenrod", align = "left")
        self.dt_img2.text((1070, 1380), self.contact_final, font=self.my_contact_font, fill = "white", align = "left")
        self.dt_img2.text((1070, 1300), "Contact Us", font=self.my_QR_font, fill = "goldenrod", align = "center")

        

        if self.entry_QR.get():
            self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=7,
            border=4,
            )
            self.qr.add_data(self.entry_QR.get())
            self.qr.make(fit=True)
            self.QR_img_f = self.qr.make_image(fill_color="black", back_color="white")
            self.QR_img_f = self.QR_img_f.resize((300,300))
            self.QR_img_f.save("qrcode_f.jpg")
            self.dt_img.paste(self.QR_img_f, (1080, 670))
            self.dt_img2.text((1100, 1000), "Scan Me!", font=self.my_QR_font, fill = "goldenrod", align = "center")       
        
        
        self.dt_img.show()
        self.DT_file = fd.asksaveasfilename(
        filetypes=[("png file", ".png"), ("jpg file", ".jpg")],
        defaultextension=".png")
        if self.DT_file:  # user selected file
            self.dt_img.save(self.DT_file)
        else: # user cancel the file browser window
            print("No file chosen")  
        


    #Error handling for issues with user inputs
    def generate_check(self):
        if self.profile_var.get() == 0:
            print("profile image is false")
            self.window_P = customtkinter.CTkToplevel()
            self.window_P.geometry("600x300")
            # create label on CTkToplevel window
            self.label_PI = customtkinter.CTkLabel(self.window_P, text="Photo required. \n Please upload a photo \n before generating flyer.", text_font=("Helvetica", 16, "bold"))
            self.label_PI.pack(side="top", fill="both", expand=True, padx=40, pady=40)
            return
        if self.radio_var.get()==0:
            print("no template selected")
            self.window_T = customtkinter.CTkToplevel()
            self.window_T.geometry("600x300")
            # create label on CTkToplevel window
            self.label_TS = customtkinter.CTkLabel(self.window_T, text="Template selection required. \n Please select a template \n before generating flyer.", text_font=("Helvetica", 16, "bold"))
            self.label_TS.pack(side="top", fill="both", expand=True, padx=40, pady=40)
            return False
        email = self.entry_D.get()
        if email and not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            print("invalid email")
            self.window_E = customtkinter.CTkToplevel()
            self.window_E.geometry("600x300")
            # create label on CTkToplevel window
            label_E = customtkinter.CTkLabel(self.window_E, text="Please provide a valid email.", text_font=("Helvetica", 16, "bold"))
            label_E.pack(side="top", fill="both", expand=True, padx=40, pady=40)
            return False
        url_pattern = re.compile(r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$')
        url = self.entry_C.get()
        if url and not url_pattern.fullmatch(url):
            self.window_U = customtkinter.CTkToplevel()
            self.window_U.geometry("600x300")
            label_U = customtkinter.CTkLabel(self.window_U, text="Please provide a valid website URL \n in the website field.", text_font=("Helvetica", 16, "bold"))
            label_U.pack(side="top", fill="both", expand=True, padx=40, pady=40)
            return False
        
        return True


    #Flyer creation
    def generate_flyer(self):
        self.check_len()
        if not self.generate_check():  # if generate_check returns False, stop executing generate_flyer
            return
        if self.radio_var.get()==2:
            self.blue_template()
        elif self.radio_var.get()==1:
            self.orange_template()
        elif self.radio_var.get()==3:
            self.dark_template()

    def checkbox_event(self):
        print("checkbox toggled, current value:", self.check_var.get())


    #Widgets for flyer window
    def flyer_window(self):
        self.text_var = tkinter.StringVar(value="Digital Flyer Generator")
        self.master.geometry("1100x750")



        self.label_FL = customtkinter.CTkLabel(master=self.frame_D,
                                    textvariable=self.text_var,
                                    width=340,
                                    height=55,
                                    text_font=("Helvetica", 26, "bold"),
                                    fg_color=("#d1d5d8", "gray75"),
                                    corner_radius=8, bg_color="#d1d5d8")
        self.label_FL.place(relx=0.5, rely=0.03, anchor=tkinter.CENTER)   

            
        #Create a canvas
        self.canvas_C=Canvas(master=self.frame_D, width= 100, height= 100)
        #Load an image in the script
        
        self.anonymous_pic=Image.open("URL Toolkit Folder\gray_anonymous.png")
        self.anonymous_pic = self.anonymous_pic.resize((100,100))
        self.anonymous_pic.save("URL Toolkit Folder\gray_anonymous.png")
        self.anonymous_pic=ImageTk.PhotoImage(Image.open("URL Toolkit Folder\gray_anonymous.png"))
        #Add image to the Canvas Items
        self.canvas_C.create_image(100/2,100/2, anchor=tkinter.CENTER,image=self.anonymous_pic)
        self.canvas_C.pack()
        self.canvas_C.place(relx=0.5, rely=0.138, anchor=tkinter.CENTER)


        self.profile_var = tkinter.IntVar(master=self.frame_D, value=0)
        self.profile_var.set(0)
        
        self.button_A = customtkinter.CTkButton(master=self.frame_D,
                    width=180,
                    height=35,
                    text_font=("Helvetica", 16),
                    border_width=0,
                    corner_radius=8,
                    text="Upload Photo",
                    command=self.image_pull, bg_color="#d1d5d8")
        self.button_A.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

        self.label_T = customtkinter.CTkLabel(master=self.frame_D,
                text = "Add Title",
                width=340,
                height=35,
                text_font=("Helvetica", 18),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.label_T.place(relx=0.5, rely=0.31, anchor=tkinter.CENTER)
        
        self.entry_A = customtkinter.CTkEntry(master=self.frame_D,
                placeholder_text="Name or title of individual, business, service, product, or event -- Limit 40 characters",
                width=500,
                height=35,
                border_width=2,
                corner_radius=10,
                bg_color="#d1d5d8")
        self.entry_A.place(relx=0.5, rely=0.37, anchor=tkinter.CENTER)

        
        self.label_B = customtkinter.CTkLabel(master=self.frame_D,
                text = "Add Description",
                width=340,
                height=35,
                text_font=("Helvetica", 18),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.label_B.place(relx=0.25, rely=0.55, anchor=tkinter.CENTER)
        
        self.entry_B = customtkinter.CTkEntry(master=self.frame_D,
                placeholder_text="Enter description of history, services offered, or mission -- Limit 400 characters",
                width=535,
                height=35,
                border_width=2,
                corner_radius=10,
                bg_color="#d1d5d8")
        self.entry_B.place(relx=0.275, rely=0.61, anchor=tkinter.CENTER)
        
        
        self.label_C = customtkinter.CTkLabel(master=self.frame_D,
                text = "Add Contact Info Below",
                width=340,
                height=35,
                text_font=("Helvetica", 18),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.label_C.place(relx=0.84, rely=0.43, anchor=tkinter.CENTER)    

        self.label_C2 = customtkinter.CTkLabel(master=self.frame_D,
                text = "Website URL",
                width=100,
                height=35,
                text_font=("Helvetica", 14),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.label_C2.place(relx=.63, rely=0.50, anchor=tkinter.CENTER,)    

        
        self.entry_C = customtkinter.CTkEntry(master=self.frame_D,
                placeholder_text="https://yourwebsite.org/",
                width=300,
                height=35,
                border_width=2,
                corner_radius=10,
                bg_color="#d1d5d8")
        self.entry_C.place(relx=0.84, rely=0.50, anchor=tkinter.CENTER)

        self.check_var = tkinter.StringVar(master=self.frame_D, value="off")

        self.checkbox = customtkinter.CTkCheckBox(master=self.frame_D, text="Shorten Website URL on Flyer?", command=self.checkbox_event,
                                            variable=self.check_var, onvalue="on", offvalue="off")
        self.checkbox.place(relx=.72, rely=.53)

        self.label_D2 = customtkinter.CTkLabel(master=self.frame_D,
                text = "Email",
                width=100,
                height=35,
                text_font=("Helvetica", 14),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.label_D2.place(relx=0.63, rely=0.61, anchor=tkinter.CENTER)


        self.entry_D = customtkinter.CTkEntry(master=self.frame_D,
                placeholder_text="hello@greatemail.com",
                width=300,
                height=35,
                border_width=2,
                corner_radius=10,
                bg_color="#d1d5d8")
        self.entry_D.place(relx=0.84, rely=0.61, anchor=tkinter.CENTER)

        self.entry_E = customtkinter.CTkEntry(master=self.frame_D,
                placeholder_text="XXX-XXX-XXXX",
                width=300,
                height=35,
                border_width=2,
                corner_radius=10,
                bg_color="#d1d5d8")
        self.entry_E.place(relx=0.84, rely=0.68, anchor=tkinter.CENTER)

        self.label_E2 = customtkinter.CTkLabel(master=self.frame_D,
                text = "Phone number",
                width=100,
                height=35,
                text_font=("Helvetica", 14),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.label_E2.place(relx=0.625, rely=0.68, anchor=tkinter.CENTER)

        self.label_F2 = customtkinter.CTkLabel(master=self.frame_D,
                text = "Social Media",
                width=100,
                height=35,
                text_font=("Helvetica", 14),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.label_F2.place(relx=0.63, rely=0.75, anchor=tkinter.CENTER)


        self.entry_F = customtkinter.CTkEntry(master=self.frame_D,
                placeholder_text="Format as desired social media site/@Username -- EX: Twitter/@Username",
                width=300,
                height=35,
                border_width=2,
                corner_radius=10,
                bg_color="#d1d5d8")
        self.entry_F.place(relx=0.84, rely=0.75, anchor=tkinter.CENTER)

        self.label_B = customtkinter.CTkLabel(master=self.frame_D,
                text = "Add Tagline",
                width=340,
                height=35,
                text_font=("Helvetica", 18),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.label_B.place(relx=0.25, rely=0.43, anchor=tkinter.CENTER)
        
        self.entry_G = customtkinter.CTkEntry(master=self.frame_D,
                placeholder_text="Add in Brief Tagline -- Limit 150 characters",
                width=535,
                height=35,
                border_width=2,
                corner_radius=10,
                bg_color="#d1d5d8")
        self.entry_G.place(relx=0.275, rely=0.49, anchor=tkinter.CENTER)      

    

        self.label_EX1 = customtkinter.CTkLabel(master=self.frame_D2,
        text = "",
        width=60,
        height=15,
        text_font=("Helvetica", 12, "bold"),
        fg_color="silver",
        corner_radius=8, bg_color="silver")
        self.label_EX1.place(relx=0.7, rely=0.06, anchor=tkinter.CENTER)

        self.radio_var = tkinter.IntVar(master=self.frame_D, value=0)
        self.radio_var.set(0)

        self.radiobutton_1 = customtkinter.CTkRadioButton(master=self.frame_D, text="Orange template",
                                                    variable= self.radio_var, value=1, bg_color="silver", command=self.orange_display)
        self.radiobutton_2 = customtkinter.CTkRadioButton(master=self.frame_D, text="Blue template",
                                                    variable= self.radio_var, value=2, bg_color="silver", command=self.blue_display)
        self.radiobutton_3 = customtkinter.CTkRadioButton(master=self.frame_D, text="Dark template",
                                                    variable= self.radio_var, value=3, bg_color="silver", command=self.dark_display)

        self.radiobutton_1.place(relx=.025, rely=.75)
        self.radiobutton_2.place(relx=.025, rely=.83)
        self.radiobutton_3.place(relx=.025, rely=.91)

        self.label_CTS = customtkinter.CTkLabel(master=self.frame_D2,
                text = "Select Template",
                width=40,
                height=35,
                text_font=("Helvetica", 14, "bold"),
                fg_color=("silver"),
                corner_radius=8, bg_color="silver")
        self.label_CTS.place(relx=0.22, rely=0.12, anchor=tkinter.CENTER)


        self.expand_pic=Image.open("URL Toolkit Folder\expand arrow.png")
        self.expand_pic = self.expand_pic.resize((10,10))
        self.expand_pic.save("URL Toolkit Folder\expand arrow.png")
        self.expand_pic=ImageTk.PhotoImage(Image.open("URL Toolkit Folder\expand arrow.png"))


        self.expand_button = customtkinter.CTkButton(master=self.frame_D2,
                                    width=10,
                                    height=10,
                                    border_width=0,
                                    border_color="white",
                                    fg_color="white",
                                    corner_radius=8,
                                    text="",
                                    image=self.expand_pic, command=self.expand_event)

        self.Q_pic=Image.open("URL Toolkit Folder\Question Mark.png")
        self.Q_pic = self.Q_pic.resize((30,30))
        self.Q_pic.save("URL Toolkit Folder\Question-Mark-resized.png")
        self.Q_pic=ImageTk.PhotoImage(Image.open("URL Toolkit Folder\Question-Mark-resized.png"))

        self.help_button_F = customtkinter.CTkButton(master=self.frame_D,
                                    width=30,
                                    height=30,
                                    border_width=0,
                                    border_color="#d1d5d8",
                                    fg_color="#d1d5d8",
                                    corner_radius=8,
                                    text="",
                                    image=self.Q_pic, command=self.flyer_help)
        self.help_button_F.place(relx=0.94, rely=0.05, anchor=tkinter.CENTER)

        self.help_label_F = customtkinter.CTkLabel(master=self.frame_D,
                text = "Need Help?",
                width=140,
                height=35,
                text_font=("Helvetica", 14),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.help_label_F.place(relx=0.94, rely=0.1, anchor=tkinter.CENTER)

        self.label_G = customtkinter.CTkLabel(master=self.frame_D,
                text = "Select Link to be Converted to QR Code",
                width=340,
                height=45,
                text_font=("Helvetica", 16),
                fg_color=("#d1d5d8", "gray75"),
                corner_radius=8, bg_color="#d1d5d8")
        self.label_G.place(relx=0.8, rely=0.81, anchor=tkinter.CENTER)

        self.entry_QR = customtkinter.CTkEntry(master=self.frame_D,
                placeholder_text="This should be the main destination you want people to view",
                width=400,
                height=35,
                border_width=2,
                corner_radius=10,
                bg_color="#d1d5d8")
        self.entry_QR.place(relx=0.8, rely=0.86, anchor=tkinter.CENTER)


        self.generate_button = customtkinter.CTkButton(master=self.frame_D,
                    width=200,
                    height=25,
                    text_font=("Helvetica", 20),
                    border_width=0,
                    corner_radius=8,
                    text="Generate",
                    command=self.generate_flyer, bg_color="#d1d5d8")
        self.generate_button.place(relx=0.52, rely=0.95, anchor=tkinter.CENTER)


#GUI and class initilization
root = tkinter.Tk()
root.resizable(False, False)
app = URLToolbox(root)
root.mainloop()