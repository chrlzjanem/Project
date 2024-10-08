
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\charl\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\project\3\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x740")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 740,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    389.0,
    740.0,
    fill="#FFDB00",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1060.0,
    y=691.0,
    width=219.89620971679688,
    height=43.96636199951172
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=269.4220275878906,
    width=389.2879638671875,
    height=49.19176483154297
)

canvas.create_rectangle(
    0.0,
    245.0,
    389.0,
    269.0,
    fill="#CABB11",
    outline="")

canvas.create_text(
    396.0,
    30.0,
    anchor="nw",
    text="EMPLOYEE",
    fill="#0F2F9F",
    font=("Times New Roman Bold", 60 * -1)
)

canvas.create_text(
    465.0,
    138.0,
    anchor="nw",
    text="Employee Name",
    fill="#000000",
    font=("Times New Roman Bold", 15 * -1)
)

canvas.create_text(
    700.0,
    138.0,
    anchor="nw",
    text="ID Number",
    fill="#000000",
    font=("Times New Roman Bold", 15 * -1)
)

canvas.create_text(
    900.0,
    138.0,
    anchor="nw",
    text="Position",
    fill="#000000",
    font=("Times New Roman Bold", 15 * -1)
)

canvas.create_text(
    1025.0,
    138.0,
    anchor="nw",
    text="Total Work Hours",
    fill="#000000",
    font=("Times New Roman Bold", 15 * -1)
)

canvas.create_text(
    1158.0,
    138.0,
    anchor="nw",
    text="No. of Absences",
    fill="#000000",
    font=("Times New Roman Bold", 15 * -1)
)

canvas.create_text(
    2.0,
    181.0,
    anchor="nw",
    text="ADMIN",
    fill="#000000",
    font=("Times New Roman", 50 * -1)
)

canvas.create_text(
    5.0,
    248.0,
    anchor="nw",
    text="Main",
    fill="#000000",
    font=("Times New Roman", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1210.0,
    417.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#0F2F9F",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1168.0,
    y=156.0,
    width=84.0,
    height=521.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1085.0,
    417.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#0F2F9F",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1043.0,
    y=156.0,
    width=84.0,
    height=521.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    736.5,
    417.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#0F2F9F",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=662.0,
    y=156.0,
    width=149.0,
    height=521.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    927.5,
    417.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#0F2F9F",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=856.0,
    y=156.0,
    width=143.0,
    height=521.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    516.5,
    417.5,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#0F2F9F",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=415.0,
    y=156.0,
    width=203.0,
    height=521.0
)

#savemore photo
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    179.0,
    81.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
