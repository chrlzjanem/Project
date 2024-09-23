
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\charl\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\project\5\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x740")
window.configure(bg = "#FFDB00")


canvas = Canvas(
    window,
    bg = "#FFDB00",
    height = 740,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
#Number of absent
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1065.5,
    430.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#0F2F9F",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=896.0,
    y=299.0,
    width=339.0,
    height=261.0
)
#number of present
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    610.0,
    430.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#0B2F9F",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=441.0,
    y=299.0,
    width=338.0,
    height=261.0
)
#total worked hours
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    191.5,
    430.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#0B2F9F",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=22.0,
    y=299.0,
    width=339.0,
    height=261.0
)
#Detail entry
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    348.5,
    122.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#0B2F9F",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=22.0,
    y=40.0,
    width=653.0,
    height=163.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    964.0,
    133.0,
    image=image_image_1
)
#Logout
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
    x=1022.3297119140625,
    y=679.1943359375,
    width=238.67025756835938,
    height=50.80557632446289
)
#Check Out
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
    x=22.0,
    y=643.863037109375,
    width=219.89620971679688,
    height=43.96636199951172
)
#Check in
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=22.0,
    y=584.26416015625,
    width=219.89620971679688,
    height=43.96636199951172
)

canvas.create_text(
    23.0,
    255.0,
    anchor="nw",
    text="Total Worked Hours",
    fill="#000000",
    font=("Times New Roman Bold", 35 * -1)
)

canvas.create_text(
    465.0,
    255.0,
    anchor="nw",
    text="Number of Present",
    fill="#000000",
    font=("Times New Roman Bold", 35 * -1)
)

canvas.create_text(
    925.0,
    255.0,
    anchor="nw",
    text="Number of Absent",
    fill="#000000",
    font=("Times New Roman Bold", 35 * -1)
)
window.resizable(False, False)
window.mainloop()
