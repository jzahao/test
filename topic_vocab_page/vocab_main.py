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
background_img = PhotoImage(file = f"bg_topicvocab_main.png")
background = canvas.create_image(
    750.0, 376.0,
    image=background_img)


# Button: Translator
button_translator_img = PhotoImage(file = f"button_translator.png")
button_translator = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_translator_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_translator.place(
    x = 0, y = 224,
    width = 280,
    height = 64)


# Button: Topic Vocab
button_topicvocab_img = PhotoImage(file = f"topicvocab_button_topicvocab.png")
button_topicvocab = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_topicvocab_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_topicvocab.place(
    x = 0, y = 288,
    width = 280,
    height = 64)


# Button: LT
button_lt_img = PhotoImage(file = f"button_listeningtest.png")
button_lt = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_lt_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_lt.place(
    x = 0, y = 352,
    width = 280,
    height = 64)


# Button: RT
button_rt_img = PhotoImage(file = f"button_readingtest.png")
button_rt = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_rt_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_rt.place(
    x = 0, y = 417,
    width = 280,
    height = 64)


# Button: Short Story
button_shortstory_img = PhotoImage(file = f"button_shortstory.png")
button_shortstory = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_shortstory_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_shortstory.place(
    x = 0, y = 481,
    width = 280,
    height = 64)


# Button: Flashcard
button_flashcard_img = PhotoImage(file = f"button_flashcard.png")
button_flashcard = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_flashcard_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_flashcard.place(
    x = 0, y = 545,
    width = 280,
    height = 64)


# Button: Menu
button_menu_img = PhotoImage(file = f"button_menu_1.png")
button_menu = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_menu_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_menu.place(
    x = 1305, y = 50,
    width = 138,
    height = 138)


# Button: Unit 1
button_unit1_img = PhotoImage(file = f"unit1.png")
button_unit1 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_unit1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_unit1.place(
    x = 366, y = 268,
    width = 515,
    height = 115)


# Button: Unit 2
button_unit2_img = PhotoImage(file = f"unit2.png")
button_unit2 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_unit2_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_unit2.place(
    x = 901, y = 268,
    width = 515,
    height = 115)


# Button: Unit 3
button_unit3_img = PhotoImage(file = f"unit3.png")
button_unit3 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_unit3_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_unit3.place(
    x = 366, y = 403,
    width = 515,
    height = 115)


# Button: Unit 4
button_unit4_img = PhotoImage(file = f"unit4.png")
button_unit4 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_unit4_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_unit4.place(
    x = 901, y = 403,
    width = 515,
    height = 115)


# Button: Unit 5
button_unit5_img = PhotoImage(file = f"unit5.png")
button_unit5 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_unit5_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_unit5.place(
    x = 366, y = 538,
    width = 515,
    height = 115)


# Button: Unit 6
button_unit6_img = PhotoImage(file = f"unit6.png")
button_unit6 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_unit6_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_unit6.place(
    x = 901, y = 538,
    width = 515,
    height = 115)


window.resizable(False, False)
window.mainloop()