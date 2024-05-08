import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random

bg_color = "#3d6466"


def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()
    idx = random.randint(0, len(all_tables) - 1)

    table_name = all_tables[idx][1]

    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()

    return table_name, table_records


def pre_processes(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])

    ingredients = []

    for i in table_records:
        name, qty, unit = i[1], i[2], i[3]
        ingredients.append(qty + " " + unit + "of " + name)

    return title, ingredients


def load_frame1():
    frame1.tkraise()
    frame1.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img

    logo_widget.pack()

    tk.Label(
        frame1,
        text="Placeholder text here!!!",
        bg=bg_color,
        fg="white",
        font=("TkMenuFont", 14),
    ).pack()

    tk.Button(
        frame1,
        text="More Placeholder",
        font=("TkHeadingFont", 14),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame2(),
    ).pack(pady=20)


def load_frame2():
    frame2.tkraise()
    table_name, table_records = fetch_db()
    title, ingredients = pre_processes(table_name, table_records)

    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo_botton.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Label(
        frame2,
        text=title,
        bg=bg_color,
        fg="white",
        font=("TkMenuHeading", 20),
    ).pack(pady=25)

    for i in ingredients:
        tk.Label(
            frame2,
            text=i,
            bg=bg_color,
            fg="white",
            font=("TkMenuFont", 12),
        ).pack()
    tk.Button(
        frame2,
        text="Back",
        font=("TkHeadingFont", 18),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1(),
    ).pack(pady=20)


# initiallize app
root = tk.Tk()
root.title("Test App")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()

# run app
root.mainloop()
