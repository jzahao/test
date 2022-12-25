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
background_img = PhotoImage(file = f"bg_signup.png")
background = canvas.create_image(
    750.0, 379.0,
    image=background_img)


# Textbox: Your full name
entry_your_full_name_img = PhotoImage(file = f"signup_textbox_info.png")
entry_your_full_name_bg = canvas.create_image(
    508.0, 317.5,
    image = entry_your_full_name_img)

entry_your_full_name = Entry(
    font = ("cambria", 14),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_your_full_name.place(
    x = 313, y = 297,
    width = 390,
    height = 42)


# Textbox: Date of birth
entry_date_of_birth_img = PhotoImage(file = f"signup_textbox_info.png")
entry_date_of_birth_bg = canvas.create_image(
    508.0, 404.5,
    image = entry_date_of_birth_img)

entry_date_of_birth = Entry(
    font = ("cambria", 14),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_date_of_birth.place(
    x = 313, y = 384,
    width = 390,
    height = 42)


# Textbox: Your email
entry_your_email_img = PhotoImage(file = f"signup_textbox_info.png")
entry_your_email_bg = canvas.create_image(
    508.0, 490.5,
    image = entry_your_email_img)

entry_your_email = Entry(
    font = ("cambria", 14),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_your_email.place(
    x = 313, y = 470,
    width = 390,
    height = 42)


# Textbox: Username
entry_user_name_img = PhotoImage(file = f"signup_textbox_info.png")
entry_username_bg = canvas.create_image(
    992.0, 317.5,
    image = entry_user_name_img)

entry_username = Entry(
    font = ("cambria", 14),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_username.place(
    x = 797, y = 297,
    width = 390,
    height = 42)


# Textbox: Password
entry_password_img = PhotoImage(file = f"signup_textbox_info.png")
entry_password_bg = canvas.create_image(
    992.0, 404.5,
    image = entry_password_img)

entry_password = Entry(
    font = ("cambria", 14),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_password.place(
    x = 797, y = 384,
    width = 390,
    height = 42)


# Textbox: Re_enter password
entry_re_password_img = PhotoImage(file = f"signup_textbox_info.png")
entry_re_password_bg = canvas.create_image(
    992.0, 490.5,
    image = entry_re_password_img)

entry_re_password = Entry(
    font = ("cambria", 14),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_re_password.place(
    x = 797, y = 470,
    width = 390,
    height = 42)


# Button: Sign Up
button_signup_img = PhotoImage(file = f"signup_button_signup.png")
button_signup = Button(
    activebackground = "#2FDC81",
    bg = "#2FDC81",
    image = button_signup_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_signup.place(
    x = 657, y = 562,
    width = 190,
    height = 71)


# Button: Back
button_back_img = PhotoImage(file = f"signup_button_back.png")
button_back = Button(
    activebackground = "#34E77E",
    bg = "#34E77E",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 716, y = 673,
    width = 71,
    height = 71)


window.resizable(False, False)
window.mainloop()