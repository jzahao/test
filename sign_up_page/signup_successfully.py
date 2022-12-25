from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("787x298")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 298,
    width = 787,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


# Background
background_img = PhotoImage(file = f"bg_signup_successfully.png")
background = canvas.create_image(
    393.5, 149.0,
    image=background_img)


# Button
button_tick_img = PhotoImage(file = f"signup_button_tick.png")
button_tick = Button(
    activebackground = "#FFFFFF",
    bg = "#FFFFFF",
    image = button_tick_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_tick.place(
    x = 354, y = 177,
    width = 84,
    height = 84)


window.resizable(False, False)
window.mainloop()