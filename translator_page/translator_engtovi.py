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
background_img = PhotoImage(file = f"bg_translator_engtovi.png")
background = canvas.create_image(
    750, 390,
    image=background_img)


# Button: Translator
button_translator_img = PhotoImage(file = f"translator_button_translator.png")
button_translator = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
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
button_topic_vocab_img = PhotoImage(file = f"button_topicvocab.png")
button_topic_vocab = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_topic_vocab_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_topic_vocab.place(
    x = 0, y = 288,
    width = 280,
    height = 64)


# Button: LT
button_lt_img = PhotoImage(file = f"button_listeningtest.png")
button_lt = Button(
    activebackground = "#B31217",
    bg = "#B31217",    image = button_lt_img,
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
    x = 0, y = 416,
    width = 280,
    height = 64)


# Button: Short Story
button_short_story_img = PhotoImage(file = f"button_shortstory.png")
button_short_story = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_short_story_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_short_story.place(
    x = 0, y = 479,
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
    x = 0, y = 542,
    width = 280,
    height = 64)


# Button: Swap
button_swap_img = PhotoImage(file = f"translator_button_swap_1.png")
button_swap = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_swap_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_swap.place(
    x = 855, y = 540,
    width = 64,
    height = 64)


# Button: Trans
button_trans_img = PhotoImage(file = f"translator_button_trans_1.png")
button_trans = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_trans_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_trans.place(
    x = 847, y = 610,
    width = 86,
    height = 59)


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


# Textbox: Input
textbox_input = Text(
    font = ("cambria", 32),
    bd = 0,
    bg = "#F2F2F2",
    fg = "#535353",
    highlightthickness = 0)

textbox_input.place(
    x = 356, y = 380,
    width = 454,
    height = 300)


window.resizable(False, False)
window.mainloop()