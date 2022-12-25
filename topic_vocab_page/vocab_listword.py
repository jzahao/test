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
background_img = PhotoImage(file = f"bg_topicvocab_listword.png")
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

# Button: Name of Unit
button_nameofunit_img = PhotoImage(file = f"topicvocab_button_nameofunit.png")
button_nameofunit = Button(
    text = "UNIT 1: CONTRACT",
    font = ("cambria", 40, "bold"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_nameofunit_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_nameofunit.place(
    x = 430, y = 79,
    width = 930,
    height = 100)


# Button: Word 1
button_word1_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word1 = Button(
    text = "abide by",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word1.place(
    x = 430, y = 189,
    width = 460,
    height = 85)


# Button: Word 2
button_word2_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word2 = Button(
    text = "agreement",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word2_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word2.place(
    x = 900, y = 189,
    width = 460,
    height = 85)


# Button: Word 3
button_word3_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word3 = Button(
    text = "assurance",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word3_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word3.place(
    x = 430, y = 284,
    width = 460,
    height = 85)

# Button: Word 4
button_word4_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word4 = Button(
    text = "cancellation",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word4_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word4.place(
    x = 900, y = 284,
    width = 460,
    height = 85)


# Button: Word 5
button_word5_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word5 = Button(
    text = "determine",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word5_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word5.place(
    x = 430, y = 379,
    width = 460,
    height = 85)


# Button: Word 6
button_word6_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word6 = Button(
    text = "establish",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word6_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word6.place(
    x = 900, y = 379,
    width = 460,
    height = 85)


# Button: Word 7
button_word7_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word7 = Button(
    text = "obligate",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word7_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word7.place(
    x = 430, y = 474,
    width = 460,
    height = 85)


# Button: Word 8
button_word8_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word8 = Button(
    text = "provision",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word8_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word8.place(
    x = 900, y = 474,
    width = 460,
    height = 85)


# Button: Word 9
button_word9_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word9 = Button(
    text = "resolve",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word9_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word9.place(
    x = 430, y = 569,
    width = 460,
    height = 85)


# Button: Word 10
button_word10_img = PhotoImage(file = f"topicvocab_button_word.png")
button_word10 = Button(
    text = "specific",
    font = ("firasan", 28, "bold", "italic"),
    fg = "#FFFFFF",
    activeforeground = "#FFFFFF",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word10_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word10.place(
    x = 900, y = 569,
    width = 460,
    height = 85)


# Button: Back
button_back_img = PhotoImage(file = f"topicvocab_button_back_1.png")
button_back = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 813, y = 682,
    width = 75,
    height = 75)


# Button: Menu
button_menu_img = PhotoImage(file = f"topicvocab_button_menu_1.png")
button_menu = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_menu_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_menu.place(
    x = 901, y = 682,
    width = 75,
    height = 75)


window.resizable(False, False)
window.mainloop()