import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

tkinter.messagebox.showerror("showinfo","This is an info msg")
isYes = tkinter.messagebox.askyesno("askyesno","Continue?")
print(isYes)

name = tkinter.simpledialog.askstring("askstring","Enter your name")
print(name)