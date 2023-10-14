import os
import API_Handling
import tkinter as tk
from tkinter import filedialog


GlobalInfo = {
    "userID": "",
    "aviID": ""
}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

"""
    Tkinter Functions
"""

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

def validateAviFile():
    print("")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

"""
    VRCHAT OSC SETUP by C.J.L.
"""
# aviFile = f"C:\Users\Momo\AppData\LocalLow\VRChat\VRChat\OSC\{GlobalInfo['userID']}\Avatars\{GlobalInfo['aviID']}.json"

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

BahnBold = ("Bahnschrift Semibold", 22)
BahnSemiBold = ("Bahnschrift SemiCondensed", 15)
BahnSemiBoldCondensed = ("Bahnschrift SemiBold Condensed", 13)

# Create the main application window
root = tk.Tk()
root.title("Euphoric_PyLove written by C.J.L.")
root.config(bg='#2e2e2e')

# Set the window size to 600x800
root.geometry("600x800")

# Create a label widget
label = tk.Label(root, text="Hello, Welcome to Py-Love!", bg='#2e2e2e', fg="white", font=BahnBold)
label.pack()  # Pack the label widget to fit the window

labelRequest1 = tk.Label(root, font=BahnSemiBold, bg='#2e2e2e', fg="white", text="Please copy and select the path for your VRCHAT Avi,\nthen paste it in the below text box.\n\nPath Looks Similar to This:")
labelRequest1.pack()

labelRequest2 = tk.Label(root, font=BahnSemiBoldCondensed, bg='#2e2e2e', fg="white", text="C:\\Users\\<User>\\AppData\\LocalLow\\VRChat\\VRChat\\OSC\\<User_ID>\\Avatars\\<Avatar_ID>.json")
labelRequest2.pack()

labelRequest3 = tk.Label(root, font=BahnSemiBold, bg='#2e2e2e', fg="white", text="Your UserID Can be found in your URL at 'vrchat.com'.\nYour AvatarID can be found in the VRC Avatar Descriptor Component in Unity.")
labelRequest3.pack()

label_file_explorer = tk.Entry(root, 
                            text = "File Explorer using Tkinter",
                            width = 100,
                            fg = "blue")
label_file_explorer.pack()
  
      
button_explore = tk.Button(root, 
                        text = "Browse Files",
                        command = browseFiles) 
button_explore.pack()

# Define a function to be called when the button is clicked
def on_button_click():
    label.config(text="Button Clicked!")

# Start the main event loop
root.mainloop()
