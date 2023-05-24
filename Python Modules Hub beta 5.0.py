#PMH by src_guy
#2023

from tkinter import *
import tkinter as tk
import os
import os.path

def reset():
    root.destroy()
    main()

def run_module(module_name):
    error_blind = tk.Label(root, text="© 2023 src_guy", fg="black")
    error_blind.grid(row=4, column=0)
    file_exe = open("modules_exe.txt")
    file_py = open("modules_py.txt")
    temp_exe = file_exe.read().splitlines()
    temp_py = file_py.read().splitlines()
    if module_name in temp_py:
        file_exist = os.path.exists(module_name + '.py')
        if file_exist == True:
            os.system("start " + module_name + ".py")
        else:
            error = tk.Label(root, text="File doesn't exist", fg="red")
            error.grid(row=4, column=0)

    if module_name in temp_exe:
        file_exist = os.path.exists(module_name + '.exe')
        if file_exist == True:
            os.system("start " + module_name + ".exe")
        else:
            error = tk.Label(root, text="File doesn't exist", fg="red")
            error.grid(row=4, column=0)
    
def run_command():
    error_blind = tk.Label(root, text="© 2023 src_guy", fg="black")
    error_blind.grid(row=4, column=0)
    command = command_raw.get()
    result = command.split()
    if result[0] == "new":
        if result[1] == "py":
            with open("modules_py.txt", "a") as modules_file:
                modules_file.write(result[2])
                modules_file.write("\n")
                modules_file.close()
        if result[1] == "exe":
            with open("modules_exe.txt", "a") as modules_file:
                modules_file.write(result[2])
                modules_file.write("\n")
                modules_file.close()
    if result[0] == "del":
        if result[1] == "py":
            with open("modules_py.txt") as modules_file:
                modules_names = modules_file.readlines()
                modules_names.remove(result[2] + '\n')
                modules_names = ' '.join(map(str,modules_names))
                with open("modules_py.txt", "w") as modules_file:
                    modules_file.write(modules_names)
    if result[0] == "del":
        if result[1] == "exe":
            with open("modules_exe.txt") as modules_file:
                modules_names = modules_file.readlines()
                modules_names.remove(result[2] + '\n')
                modules_names = ' '.join(map(str,modules_names))
                with open("modules_exe.txt", "w") as modules_file:
                    modules_file.write(modules_names)
    if result[0] == "license":
        license_window = Toplevel(root)
        license_window.title("License")
        license_text = tk.Label(license_window, text=" Tea Team license for open-source software v. 1\n\nCopyright © 2023 Bruno Szewczyk\n\nThis license gives the user permission to:\nUse the software for his/her own\nAnalyze the source code\nModify the source code for his/her own\n\nUser can't do anything else with this software")
        license_text.pack()
    if result[0] == "exit":
        root.destroy()
    reset()

def run():
    error_blind = tk.Label(root, text="© 2023 src_guy", fg="black")
    error_blind.grid(row=4, column=0)
    index = index_raw.get()
    result = index.split() #every word to list
    if result[0] == "py":
        file_exist = os.path.exists(result[1] + '.py')
        if file_exist == True:
            os.system("start " + result[1] + ".py")
        else:
            error = tk.Label(root, text="File doesn't exist", fg="red")
            error.grid(row=3, column=1)
    if result[0] == "exe":
        file_exist = os.path.exists(result[1] + '.exe')
        if file_exist == True:
            os.system("start " + result[1] + ".exe")
        else:
            error = tk.Label(root, text="File doesn't exist", fg="red")
            error.grid(row=4, column=0)

def main():        
    global root   
    root = tk.Tk()
    root.title('Python Modules Hub')
    root.geometry("600x400")

    error_blind = tk.Label(root, text="© 2023 src_guy", fg="black")
    error_blind.place(relx = 0.43, rely = 0.7)

    global index_raw
    global command_raw

    index_raw = tk.StringVar()
    command_raw = tk.StringVar()

    title = tk.Label(root, text="Python Modules Hub\n beta 4.0", font='Arial 17 bold', fg='#1ce4eb', bg="#ff0a0e")
    title.place(relx = 0.5, anchor = N)
    
    blank = tk.Label(root, text=" \n \n", font="Arial 17 bold")
    blank.grid(row = 0, column = 0)

    modules_buttons_number = 0
    modules_buttons_names = []
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
        module_button = tk.Button(root, text = modules_buttons_names[modules_buttons_number], bg="yellow", command = lambda module_name=module_name: run_module(module_name))
        module_button.grid(row = 1 + modules_buttons_number, column = 0, pady=5, padx=5)
        modules_buttons_number = modules_buttons_number + 1

    index_entry = tk.Entry(root, textvariable = index_raw)
    button1 = tk.Button(root, text = "Run module!", bg="#03fc7f", command = run)
    index_entry.place(relx = 0.3, rely = 0.3)
    button1.place(relx = 0.55, rely = 0.29)

    command_entry = tk.Entry(root, textvariable = command_raw)
    button2 = tk.Button(root, text = "Run command", bg="#03fc7f", command = run_command)
    command_entry.place(relx = 0.3, rely = 0.4)
    button2.place(relx = 0.55, rely = 0.39)

    root.mainloop()

main()