import tkinter as tk
from tkinter import ttk
    

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

text = tk.Text(root, height=8)
text.pack()

text.insert("1.0", "Please enter a comment..")
text["state"] = "disabled"
text["state"] = "normal"

text_content = text.get("1.0", "end")
print(text_content)

root.mainloop()
