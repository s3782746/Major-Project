# Import module 
from tkinter import *

import tkinter.messagebox
  
# Create object 
root = Tk()

# adding title for root window
root.title("Major Project")
  
# Adjust size 
root.geometry("853x625")
  
# Add image file
bg = PhotoImage(file = "Melbourne CBD.png")
  
# Create Canvas
canvas1 = Canvas( root, width = 853,
                 height = 625)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

canvas1.create_text( 350, 50, text = "The Best Coffee in Melbourne CBD", font=('Helvetica','24','bold'))

# creating the messagebox which will display the information
def place1():
    tkinter.messagebox.showinfo("Name: Liminal", "Address: 161 collins street Rating: 4.2/5")

def place2():
    tkinter.messagebox.showinfo("Name: Altius Coffee Bewers", "Address: 517 Flinders Lane Rating: 4.8/5")

def place3():
    tkinter.messagebox.showinfo("Name: Vacation", "Address: 1 Exhibition Street Rating: 4.6/5")

def place4():
    tkinter.messagebox.showinfo("Name: King St Espresso Bar", "Address: 1 270 King Street Rating: 4.4/5")

def place5():
    tkinter.messagebox.showinfo("Name: Bonnie Coffee Co.", "Address: Shop 5 495 Collins Street Rating: 4.6/5")

def place6():
    tkinter.messagebox.showinfo("Name: Manchester Press", "Address: 8 Rankins Lane Rating: 4.2/5")

def place7():
    tkinter.messagebox.showinfo("Name: Little Rogue", "Address: 12 Drewery Lane Rating: 4.7/5")

def place8():
    tkinter.messagebox.showinfo("Name: Traveller", "Address: 2/14 Crossley Street Rating: 4.7/5")

def place9():
    tkinter.messagebox.showinfo("Name: 65 Degrees", "Address: 309 Exhibition Street Rating: 4.3/5")

def place10():
    tkinter.messagebox.showinfo("Name: Everyday Midtown", "Address: 213 Little Collins Street Rating: 4.5/5")
  
# Create Buttons
button1 = Button( root, text = "1", command=place1)
button2 = Button( root, text = "2", command=place2)
button3 = Button( root, text = "3", command=place3)
button4 = Button( root, text = "4", command=place4)
button5 = Button( root, text = "5", command=place5)
button6 = Button( root, text = "6", command=place6)
button7 = Button( root, text = "7", command=place7)
button8 = Button( root, text = "8", command=place8)
button9 = Button( root, text = "9", command=place9)
button10 = Button( root, text = "10", command=place10)

  
# Display Buttons
button1_canvas = canvas1.create_window( 120, 300, anchor = "nw",
                                       window = button1)
  
button2_canvas = canvas1.create_window( 400, 490, anchor = "nw",
                                       window = button2)
  
button3_canvas = canvas1.create_window( 180, 570, anchor = "nw",
                                       window = button3)
                        
button4_canvas = canvas1.create_window( 660, 100, anchor = "nw",
                                       window = button4)

button5_canvas = canvas1.create_window( 750, 250, anchor = "nw",
                                       window = button5)

button6_canvas = canvas1.create_window( 600, 220, anchor = "nw",
                                       window = button6)

button7_canvas = canvas1.create_window( 200, 380, anchor = "nw",
                                       window = button7)

button8_canvas = canvas1.create_window( 380, 350, anchor = "nw",
                                       window = button8)

button9_canvas = canvas1.create_window( 450, 200, anchor = "nw",
                                       window = button9)

button10_canvas = canvas1.create_window( 600, 400, anchor = "nw",
                                       window = button10)
  
# Execute tkinter
root.mainloop()

