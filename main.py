import tkinter as tk
from settings import *

win = tk.Tk()
win.title(
    "Сами пишите а не списывайте у меня а то че у всех одинаковов так же не интересно вообще."
)
win.geometry(f"{W}x{H}")
win.resizable(0, 0)



button_1 = tk.Button(text="ЖМИ", bg=COLOR_3, fg=COLOR_4)
button_1.grid(row=1, column=3, sticky="we")

label_1 = tk.Label(text="текст", bg=COLOR_1, fg=COLOR_4)
label_1.grid(row=0, column=2, sticky="wens")

entry_1 = tk.Entry()
entry_1.grid(row=1, column=1, sticky="we", columnspan=2)

entry_1 = tk.Entry()
entry_1.grid(row=1, column=1, sticky="we", columnspan=2)


# задаем размеры грида
for i in range(20):
    win.grid_columnconfigure(i, minsize=SIZE_W)
    win.grid_rowconfigure(i, minsize=SIZE_H)


win.mainloop()
