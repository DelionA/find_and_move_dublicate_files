#
import os
import filecmp
import shutil
import tkinter as tk
from tkinter import filedialog as fd
import time

def create_files_dict(): 
    path = dict_folders.get('source_directory')
    lbl_window_state_pole.configure(text='Start Create Files Dict...',bg='green')
    lbl_window_state_pole.update()
    for dirpath, dirnames,filenames in os.walk(path):
        for name in filenames:
            if name not in dict_files:
                dict_files[name] = list()
            dict_files[name].append(os.path.join(dirpath, name))
    lbl_window_state_pole.configure(text='End Create Files Dict...',bg='green')
    lbl_window_state_pole.update()
    files_count = len(dict_files)

def compared_two_files(file_1, file_2):
    return filecmp.cmp(file_1, file_2)

def match_conditions(file_1, file_2):
    if file_1 == file_2:
        return False    
    file_12 = file_1 + file_2
    file_21 = file_2 + file_1
    if file_12 in set_compared or file_21 in set_compared:
        return False
    set_compared.add(file_12)
    return True

def comparsion_file_list(file_list):     
    if len(file_list) == 1:
        return
    for i in file_list:
        file_1 = i
        for j in file_list:
            file_2 = j
            if match_conditions(file_1, file_2) and compared_two_files(file_1, file_2):
                set_subject_to_transfer.add(file_2)

def find_dublicate_files_func():
    for key in dict_files:
        comparsion_file_list(dict_files[key])
    lbl_dublicate_files_pole.configure(text=len(set_subject_to_transfer))
    lbl_dublicate_files_pole.update()
    
def move_files_func(numerate=0):
    path_to_destination = dict_folders['dublicate_folder']
    files_to_transfer = len(set_subject_to_transfer)
    lbl_window_state_pole.configure(text='Start File Move...',bg='green')
    lbl_window_state_pole.update()
    for file_move in set_subject_to_transfer:
        new_file_name =  path_to_destination + str(numerate) + '_' + file_move.split('/')[-1]
        shutil.move(file_move, new_file_name)
        numerate += 1
        lbl_moving_file.configure(text=file_move.split('/')[-1])
        lbl_moving_file.update()
        lbl_files_remaining_pole.configure(text= files_to_transfer - numerate)
        lbl_files_remaining_pole.update()
    lbl_window_state_pole.configure(text='End Files Move...',bg='green')
    lbl_window_state_pole.update()

def set_source_directory():
    folder_name = fd.askdirectory()
    dict_folders['source_directory']=folder_name+str('/')
    lbl_source_directory.configure(text='['+folder_name.split('/')[-1]+']')

def set_dublicate_folder():
    folder_name=fd.askdirectory()
    dict_folders['dublicate_folder']=folder_name+str('/')
    lbl_destination_folder.configure(text='['+folder_name.split('/')[-1]+']')

def func_start():
    lbl_window_state_pole.configure(text='Start Programm',bg='green')
    lbl_window_state_pole.update()
    path = dict_folders.get('source_directory')
    path_to_destination = dict_folders.get('dublicate_folder')
    if not path or not path_to_destination:
        lbl_window_state_pole.configure(text='Error, Path is Empty',bg='red')
        lbl_window_state_pole.update()
        return
    else:
        lbl_window_state_pole.configure(text='Start Programm',bg='green')
        lbl_window_state_pole.update()
        create_files_dict()
        find_dublicate_files_func()
        move_files_func()

dict_files = dict()
set_compared = set()
set_subject_to_transfer = set()
dict_folders=dict()

okno = tk.Tk()
okno.title('Welcome')
okno.geometry('500x350')
btn_1=tk.Button(okno,text='Choice Source Folder ->',command=set_source_directory)
btn_2=tk.Button(okno,text='Choice Dublicate Folder ->',command=set_dublicate_folder)
btn_1.grid(column=0,row=0,ipadx=20,pady=10)
btn_2.grid(column=0,row=2,ipadx=12,pady=10)
lbl_source_directory=tk.Label(okno)
lbl_source_directory.grid(column=1,row=0,padx=10)
lbl_destination_folder=tk.Label(okno)
lbl_destination_folder.grid(column=1,row=2,padx=10)
lbl_window_state = tk.Label(okno, text='Programm State:')# okno sostianija
lbl_window_state.grid(column=0,row=4,pady=10)
lbl_window_state_pole=tk.Label(okno,text='State Programm Now')
lbl_window_state_pole.grid(column=1,row=4,pady=10)
lbl_dublicate_files = tk.Label(okno,text='All Dublicate Files:')
lbl_dublicate_files.grid(column=0,row=6,pady=10)
lbl_dublicate_files_pole = tk.Label(okno)
lbl_dublicate_files_pole.grid(column=1,row=6)
lbl_files_remaining = tk.Label(okno,text='Files Remaining:')
lbl_files_remaining.grid(column=0,row=8,pady=10)
lbl_files_remaining_pole=tk.Label(okno)
lbl_files_remaining_pole.grid(column=1,row=8,pady=10)
lbl_moving_file=tk.Label(okno)
lbl_moving_file.grid(column=0,row=10,columnspan=2,pady=10)
btn_start=tk.Button(okno,text='Start',command=func_start)
btn_start.grid(column=0,row=13,pady=10, ipadx=30,ipady=10)
exit_btn=tk.Button(okno,text='Exit',comman=exit)
exit_btn.grid(column=1,row=13,pady=10, ipadx=30,ipady=10)
okno.mainloop()
#
