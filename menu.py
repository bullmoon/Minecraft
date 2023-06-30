import tkinter as tk
import subprocess

def run_script1():
    subprocess.Popen(["python", "script1.py"])

def run_script2():
    subprocess.Popen(["python", "script2.py"])

root = tk.Tk()

button1 = tk.Button(root, text="Build zombie factory", command='Zombie_factory/zombie_factory.py')
button1.pack()

button2 = tk.Button(root, text="Run Script 2", command=run_script2)
button2.pack()

root.mainloop()
