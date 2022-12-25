from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("787x351")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 351,
    width = 787,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


# Background
background_img = PhotoImage(file = f"bg_signup_failed_1.png")
background = canvas.create_image(
    393.5, 175.5,
    image=background_img)


# Button
button_exit_img = PhotoImage(file = f"signup_button_exit.png")
button_exit = Button(
    activebackground = "#FFFFFF",
    bg = "#FFFFFF",
    image = button_exit_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_exit.place(
    x = 344, y = 221,
    width = 104,
    height = 104)


window.resizable(False, False)
window.mainloop()