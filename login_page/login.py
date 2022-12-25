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
background_img = PhotoImage(file = f"bg_login.png")
background = canvas.create_image(
    750.0, 390.0,
    image=background_img)


# TextBox: Password
entry_password_img = PhotoImage(file = f"login_textbox_password.png")
entry_password_bg = canvas.create_image(
    750.0, 455.5,
    image = entry_password_img)

entry_password = Entry(
    font = ("cambria", 14),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_password.place(
    x = 554, y = 435,
    width = 392,
    height = 42)


# TextBox: Username
entry_username_img = PhotoImage(file = f"login_textbox_username.png")
entry_username_bg = canvas.create_image(
    750.0, 368.5,
    image = entry_username_img)

entry_username = Entry(
    font = ("cambria", 14),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_username.place(
    x = 554, y = 348,
    width = 392,
    height = 42)


# Button: Log In
button_login_img = PhotoImage(file = f"login_button_login.png")
button_login = Button(
    activebackground = "#983493",
    bg = "#983493",
    image = button_login_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_login.place(
    x = 657, y = 518,
    width = 190,
    height = 59)


# Button: Back
button_back_img = PhotoImage(file = f"login_button_back.png")
button_back = Button(
    activebackground = "#89399D",
    bg = "#89399D",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 716, y = 633,
    width = 71,
    height = 71)


window.resizable(False, False)
window.mainloop()