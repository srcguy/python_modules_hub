#PMH by src_guy
#2023

from tkinter import *
import tkinter as tk
import os
import os.path

def run_module(module_name):
    file_py = open("modules_py.txt")
    temp_py = file_py.read().splitlines()
    if module_name in temp_py:
        file_exist = os.path.exists(module_name + '.py')
        if file_exist == True:
            os.system("start " + module_name + ".py")
        else:
            print("File doesn't exist")
    else:
        print("???")
    
def run_command():
    command = command_raw.get()
    result = command.split()
    if result[0] == "new":
        if result[1] == "py":
            with open("modules_py.txt", "a") as modules_file:
                modules_file.write(result[2])
                modules_file.write("\n")
                modules_file.close()
                modules_buttons_number = 0
        if result[1] == "exe":
            with open("modules_exe.txt", "a") as modules_file:
                modules_file.write(result[2])
                modules_file.write("\n")
                modules_file.close()
                modules_buttons_number = 0
                   
def run():
    index = index_raw.get()
    result = index.split() #every word to list
    if result[0] == "py":
        file_exist = os.path.exists(result[1] + '.py')
        if file_exist == True:
            os.system("start " + result[1] + ".py")
        else:
            print("Module doesn't exist")
    if result[0] == "exe":
        file_exist = os.path.exists(result[1] + '.exe')
        if file_exist == True:
            os.system("start " + result[1] + ".exe")
        else:
            print("Module doesn't exist")
            
root = tk.Tk()
root.title('Python Modules Hub')
root.geometry("600x400")

index_raw = tk.StringVar()
command_raw = tk.StringVar()
modules_buttons_number = 0
modules_buttons_names = []

title = tk.Label(root, text="Python Modules Hub\n beta 1.0", font='Arial 17 bold')
title.grid(row = 0, column = 0)

with open('modules_py.txt') as modules_py:
     modules_names = modules_py.read().splitlines()
     for item in modules_names:
         modules_buttons_names.append(item)

with open('modules_exe.txt') as modules_exe:
     modules_names = modules_exe.read().splitlines()
     for item in modules_names:
         modules_buttons_names.append(item)

while len(modules_buttons_names) > modules_buttons_number:
    module_name = modules_buttons_names[modules_buttons_number]
    module_button = tk.Button(root, text = modules_buttons_names[modules_buttons_number], command = lambda module_name=module_name: run_module(module_name))
    module_button.grid(row = 1, column = modules_buttons_number)
    modules_buttons_number = modules_buttons_number + 1
    
index_entry = tk.Entry(root, textvariable = index_raw)
button1 = tk.Button(root, text = "Run module!", command = run)
index_entry.grid(row = 3, column = 0)
button1.grid(row = 3, column = 1)

command_entry = tk.Entry(root, textvariable = command_raw)
button2 = tk.Button(root, text = "Run command", command = run_command)
command_entry.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)

root.mainloop()
