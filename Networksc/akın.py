import tkinter as tk
import os
import sys
import subprocess


# --- functions ---

def test():
    print("ifconfig")
    p = subprocess.run("ifconfig", shell=True, stdout=subprocess.PIPE)
    print(p.stdout.decode())


# --- classes ---

class Redirect():

    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert('end', text)
        # self.widget.see('end') # autoscroll

    # def flush(self):
        pass


# --- main ---

root = tk.Tk()
root.title("VenomAge")
root.geometry("300x100")
root.resizable(True,True)

text = tk.Text(root)
text.pack()

button = tk.Button(root, text='TEST', command=test)
button.pack()

old_stdout = sys.stdout
sys.stdout = Redirect(text)

root.mainloop()

sys.stdout = old_stdout