import os
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

root = Tk()
root.attributes("-topmost", True)
root.withdraw()  # we don't want a full GUI, so keep the root window from appearing

user_input = input('Type something: ')

filepath = askopenfilename(parent=root)  # show an "Open" dialog box and return the path to the selected file
print(filepath)

filename = os.path.basename(filepath)
print(filename)
