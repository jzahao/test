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
background_img = PhotoImage(file = f"bg_menu.png")
background = canvas.create_image(
    750.0, 390,
    image=background_img)


# Button: Translator
button_translator_img = PhotoImage(file = f"menu_button_translator.png")
button_translator = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_translator_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_translator.place(
    x = 212, y = 315,
    width = 520,
    height = 100)


# Button: Topic Vocab
button_topicvocab_img = PhotoImage(file = f"menu_button_topicvocab.png")
button_topicvocab = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_topicvocab_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_topicvocab.place(
    x = 788, y = 315,
    width = 520,
    height = 100)


# Button: TOEIC LT
button_lt_img = PhotoImage(file = f"menu_button_lt.png")
button_lt = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_lt_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_lt.place(
    x = 212, y = 415,
    width = 520,
    height = 100)


# Button: TOEIC RT
button_rt_img = PhotoImage(file = f"menu_button_rt.png")
button_rt = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_rt_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_rt.place(
    x = 788, y = 415,
    width = 520,
    height = 100)


# Button: Short Story
button_shortstory_img = PhotoImage(file = f"menu_button_shortstory.png")
button_shortstory = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_shortstory_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_shortstory.place(
    x = 212, y = 515,
    width = 520,
    height = 100)


# Button: Flashcard
button_flashcard_img = PhotoImage(file = f"menu_button_flashcard.png")
button_flashcard = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_flashcard_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_flashcard.place(
    x = 788, y = 515,
    width = 520,
    height = 100)


# Button: About Us
button_abus_img = PhotoImage(file = f"menu_button_abus.png")
button_abus = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_abus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_abus.place(
    x = 212, y = 615,
    width = 520,
    height = 100)


# Button: LOG OUT
button_logout_img = PhotoImage(file = f"menu_button_logout.png")
button_logout = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_logout_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_logout.place(
    x = 788, y = 615,
    width = 520,
    height = 100)


window.resizable(False, False)
window.mainloop()