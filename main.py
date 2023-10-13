import tkinter as tk
from settings import *
import winsound
import sys



def calculate():
    exp = entry_1.get() # считать что написано в ентри
    if len(exp) == 0:
        return
    try: 
        res = eval(exp) # посчитать через евал
    except:
        res = 'ОШИБКА'
    entry_1.delete(0, len(exp)) # очистить ентри
    label_1.configure(text = res) # записать в лейбл результат 
    
def click():
    global count
    if count > 10:
        label_1.configure(text = 'РАНГ: ДОБРОСЛАВ')
    if count > 20:
        label_1.configure(text = 'РАНГ: БЕЛОГОР')
    if count > 30:
        label_1.configure(text = 'РАНГ: ЛЮБОРАД')
    if count > 40:
        label_1.configure(text = 'РАНГ: ЯРОМИР')
    winsound.PlaySound('sound.wav',winsound.SND_ASYNC)
    count += 1
    button_2.configure(text= f'УБИТО ЯЩЕРОВ: {count}')
    
count = 0
win = tk.Tk()
win.title(
    "Сами пишите а не списывайте у меня а то че у всех одинаковов так же не интересно вообще."
)
win.geometry(f"{W}x{H}")
win.resizable(0, 0)

win.configure(bg = COLOR_1)

button_1 = tk.Button(text="ЖМИ", bg=COLOR_3, fg=COLOR_4, font=FONT_1, command=lambda: calculate())
button_1.grid(row=1, column=3, sticky="we")

label_1 = tk.Label(text="текст", bg=COLOR_1, fg=COLOR_4, font=FONT_2)
label_1.grid(row=0, column=2, sticky="wens")

entry_1 = tk.Entry( font=FONT_1, fg=COLOR_2)
entry_1.grid(row=1, column=1, sticky="we", columnspan=2)


button_2 = tk.Button(text="ЖМИ", bg=COLOR_3, fg=COLOR_4, font=FONT_1, command=lambda: click())
button_2.grid(row=3, column=3, sticky="we")

# задаем размеры грида
for i in range(20):
    win.grid_columnconfigure(i, minsize=SIZE_W)
    win.grid_rowconfigure(i, minsize=SIZE_H)


win.mainloop()
