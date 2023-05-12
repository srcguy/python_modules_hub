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
    reset()
    
def run_command():
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
    reset()
                   
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
    reset()

def main():         
    global root   
    root = tk.Tk()
    root.title('Python Modules Hub')
    root.geometry("600x400")

    global index_raw
    global command_raw

    index_raw = tk.StringVar()
    command_raw = tk.StringVar()

    title = tk.Label(root, text="Python Modules Hub\n beta 3.0", font='Arial 17 bold', fg='#1ce4eb', bg="#ff0a0e")
    title.grid(row = 0, column = 0)

    modules_info = tk.Label(root, text="Added modules:")
    modules_info.grid(row = 1, column = 0)

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
        module_button.grid(row = 1, column = 1 + modules_buttons_number)
        modules_buttons_number = modules_buttons_number + 1

    index_entry = tk.Entry(root, textvariable = index_raw)
    button1 = tk.Button(root, text = "Run module!", bg="#03fc7f", command = run)
    index_entry.grid(row = 3, column = 0)
    button1.grid(row = 3, column = 1)

    command_entry = tk.Entry(root, textvariable = command_raw)
    button2 = tk.Button(root, text = "Run command", bg="#03fc7f", command = run_command)
    command_entry.grid(row = 4, column = 0)
    button2.grid(row = 4, column = 1)

    root.mainloop()

main()