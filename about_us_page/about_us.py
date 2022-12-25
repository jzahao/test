from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1500x780")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 780,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


# Background
background_img = PhotoImage(file = f"bg_about_us.png")
background = canvas.create_image(
    750.0, 390,
    image=background_img)

# Button
button_back_img = PhotoImage(file = f"abus_button_back.png")
button_back = Button(
    activebackground = "#F49617",
    bg = "#F49617",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 716, y = 678,
    width = 71,
    height = 71)


window.resizable(False, False)
window.mainloop()