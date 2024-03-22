from tkinter import *
import pandas as pd
import customtkinter
import os
from utils import info_reader
# pyinstaller --icon=eye.ico  main.py -w
customtkinter.set_appearance_mode("Dark")

def show(): 
    study = selectstudy.get()
    folder = selectfolder.get()
    filepath = 'C:\\x'+ '\\' + study + '\\' + folder
    if folder == 'F1':
        filepath = 'C:\\x'+ '\\' + study + '\\' + folder
    elif folder == 'F2':
        filepath = 'C:\\x'+ '\\' + study + '\\' + folder
    elif folder == 'F3':
        filepath = 'C:\\x'+ '\\' + study + '\\' + folder
    else:
        filepath = 'C:\\x'+ '\\' + study

    os.startfile(f'{filepath}')


studies, folders = info_reader()

# Main window
root = customtkinter.CTk()
root.title('Study Helper')
root.geometry('300x300')
root.iconbitmap('C:\\x\\eye.ico')

# Frame to store all the needed boxes
frame = customtkinter.CTkFrame(master = root, fg_color = '#262626', border_color= '#eba96a', border_width=2)
frame.pack(expand = True)

# Study information
study_label = customtkinter.CTkLabel(frame, text = 'Select study: ')
selectstudy = customtkinter.CTkComboBox(frame,  values = studies)

# Folder information
folder_label = customtkinter.CTkLabel(frame, text = 'Select folder: ')
selectfolder = customtkinter.CTkComboBox(frame,  values = folders)

# Button 

btn = customtkinter.CTkButton(frame, text = 'Open folder', command = show, corner_radius= 5, fg_color='#eba96a', text_color='#262626')

# Pack up all the thingies

study_label.pack(anchor = 's', expand = True, padx = 30, pady = 10)
selectstudy.pack(anchor = 's', expand = True, padx = 30, pady = 10)

folder_label.pack(anchor = 's', expand = True, padx = 30, pady = 10)
selectfolder.pack(anchor = 's', expand = True, padx = 30, pady = 10)
btn.pack(anchor = 's', expand = True, padx = 30, pady = 15)

root.mainloop()