from tkinter import *
import pandas as pd
import customtkinter
import os
from utils import info_reader
# pyinstaller --icon=eye.ico  main.py -w --windowed
customtkinter.set_appearance_mode("Dark")

def show(): 
    study = selectstudy.get()
    folder = selectfolder.get()
    filepath = 'C:\\Users\\janav\\Documents\\studies'+ '\\' + study + '\\' + folder
    if folder == 'DTA':
        filepath = 'C:\\Users\\janav\\Documents\\studies'+ '\\' + study + '\\' + folder
    elif folder == 'P21':
        filepath = 'C:\\Users\\janav\\Documents\\studies'+ '\\' + study + '\\' + folder
    elif folder == 'Misc':
        filepath = 'C:\\Users\\janav\\Documents\\studies'+ '\\' + study + '\\' + folder
    else:
        filepath = 'C:\\Users\\janav\\Documents\\studies'+ '\\' + study


    os.startfile(f'{filepath}')


studies, folders = info_reader()

# Main window
root = customtkinter.CTk()
root.title('Study Helper')
root.geometry('600x300')
root.iconbitmap('C:\\Users\janav\\OneDrive\\Documents\\DataTechnology\\eye.ico')

# frame1 to store all the needed boxes
frame1 = customtkinter.CTkFrame(master = root, fg_color = '#262626', border_color= '#D9D9D9', border_width=2, height=300, width = 300)
#frame1.pack(side= LEFT, expand = True)
frame1.place(anchor=CENTER, rely = 0.5, relx = 0.25)

# frame1 to store all the needed boxes
frame2 = customtkinter.CTkFrame(master = root, fg_color = '#262626', border_color= '#D9D9D9', border_width=2, height=300, width = 200)
label2 = customtkinter.CTkLabel(frame2, text = "General Folders").pack(pady = 5, side = TOP)

#frame2.pack(side= LEFT)
frame2.place(anchor=CENTER, rely = 0.5, relx = 0.75, bordermode = INSIDE)

# Study information
study_label = customtkinter.CTkLabel(frame1, text = 'Select study: ')
selectstudy = customtkinter.CTkComboBox(frame1,  values = studies, width = 200)

# Folder information
folder_label = customtkinter.CTkLabel(frame1, text = 'Select folder: ')
selectfolder = customtkinter.CTkComboBox(frame1,  values = folders, width = 200)

# Button 

btn1 = customtkinter.CTkButton(frame1, text = 'Open folder', command = show, corner_radius= 5, fg_color='#eba96a', text_color='#262626', width = 200)
btn2 = customtkinter.CTkButton(frame2, text = 'Open folder', command = show, corner_radius= 5, fg_color='#eba96a', text_color='#262626', width = 200)
btn3 = customtkinter.CTkButton(frame2, text = 'Open folder', command = show, corner_radius= 5, fg_color='#eba96a', text_color='#262626', width = 200)
btn4 = customtkinter.CTkButton(frame2, text = 'Open folder', command = show, corner_radius= 5, fg_color='#eba96a', text_color='#262626', width = 200)
btn5 = customtkinter.CTkButton(frame2, text = 'Open folder', command = show, corner_radius= 5, fg_color='#eba96a', text_color='#262626', width = 200)



# Pack up all the thingies

study_label.pack(anchor = 's', expand = True, padx = 30, pady = 10)
selectstudy.pack(anchor = 's', expand = True, padx = 30, pady = 10)

folder_label.pack(anchor = 's', expand = True, padx = 30, pady = 10)
selectfolder.pack(anchor = 's', expand = True, padx = 30, pady = 10)
btn1.pack(anchor = 's', expand = True, padx = 30, pady = 10)
btn2.pack(anchor = 's', expand = True, padx = 30, pady = 10)#, side = BOTTOM)
btn3.pack(anchor = 's', expand = True, padx = 30, pady = 10)
btn4.pack(anchor = 's', expand = True, padx = 30, pady = 10)
btn5.pack(anchor = 's', expand = True, padx = 30, pady = 10)

root.mainloop()
