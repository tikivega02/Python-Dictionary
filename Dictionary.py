# Function

def func(en):
    try:
        word_json = open("words.json", "r")
        json_data = json.loads(word_json.read(3816227))
        label['text'] = json_data[str(en).lower()]
        word_json.close()
    except KeyError:
        label['text'] = f"{en} not found in the words.json file"


from tkinter import *
import tkinter.ttk as ttk
import json

# Variable
HEIGHT = 700
WIDTH = 500


# Root
root = Tk()
root.title("Dictionary")
root.maxsize(WIDTH, HEIGHT)
root.iconbitmap(r'img/icon.ico')

# Canvas
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Background image
bg = PhotoImage(file='img/bg.png')
bg_label = Label()
bg_label.place(relwidth=1, relheight=1)


# Frame
upper_frame = Frame(root, bg='#80c1ff', bd=5)
upper_frame.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.75)
lower_frame = Frame(root, bg='#80c1ff')
lower_frame.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.1)


# Entry
entry = ttk.Entry(lower_frame, font=('Courier', 18))
entry.place(relx=0.01, rely=0.1, relwidth=0.7, relheight=0.8)

# Button
button = ttk.Button(lower_frame, text='Search', command=lambda: func(entry.get()))
button.place(relx=0.73, rely=0.1, relwidth=0.25, relheight=0.8)

# Label
label = ttk.Label(upper_frame, font=('Courier', 18), anchor='nw', justify='left', wraplength='100m')
label.place(relwidth=1, relheight=1)

root.mainloop()
