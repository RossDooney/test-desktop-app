import tkinter as tk
from PIL import ImageTk

bg_color = "#3d6466"


def load_frame2():
    print("asd")


# initiallize app
root = tk.Tk()
root.title("Test App")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame1.grid(row=0, column=0)
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

# run app
root.mainloop()
