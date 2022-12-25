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
background_img = PhotoImage(file = f"bg_topicvocab_word.png")
background = canvas.create_image(
    750.0, 390.0,
    image=background_img)


# Button: Audio
button_audio_img = PhotoImage(file = f"topicvocab_button_audio.png")
button_audio = Button(
    activebackground = "#D92167",
    bg = "#D92167",
    image = button_audio_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_audio.place(
    x = 236, y = 176,
    width = 150,
    height = 150)


# Button: Back
button_back_img = PhotoImage(file = f"topicvocab_button_back_2.png")
button_back = Button(
    activebackground = "#D92167",
    bg = "#D92167",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 162, y = 706,
    width = 60,
    height = 60)


# Button: Next
button_next_img = PhotoImage(file = f"topicvocab_button_next.png")
button_next = Button(
    activebackground = "#D92167",
    bg = "#D92167",
    image = button_next_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_next.place(
    x = 392, y = 706,
    width = 60,
    height = 60)


# Button: List
button_list_img = PhotoImage(file = f"topicvocab_button_list.png")
button_list = Button(
    activebackground = "#D92167",
    bg = "#D92167",
    image = button_list_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_list.place(
    x = 315, y = 706,
    width = 60,
    height = 60)


# Button: Menu
button_menu_img = PhotoImage(file = f"topicvocab_button_menu_2.png")
button_menu = Button(
    activebackground = "#D92167",
    bg = "#D92167",
    image = button_menu_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_menu.place(
    x = 238, y = 706,
    width = 60,
    height = 60)

# Label: Word
label_word = Label(
    text = "abide by", 
    font = ("Quicksand", 50, "bold"),
    fg = "#CF246E",
    bg = "#F2F2F2")

label_word.place(
    x = 100, y = 46,
    width = 1300,
    height = 90)


# Label: Pronunciation
label_pronoun = Label(
    text = "/ə'baid bai/", 
    font = ("firasan", 34, "bold"),
    fg = "#000000",
    bg = "#F2F2F2")

label_pronoun.place(
    x = 607, y = 188,
    width = 795,
    height = 75)


# Label: Word type
label_wordtype = Label(
    text = "verb", 
    font = ("cambria", 34, "bold"),
    fg = "#CF246E",
    bg = "#F2F2F2")

label_wordtype.place(
    x = 607, y = 305,
    width = 795,
    height = 55)


# Label: Vietnamese
label_vi = Label(
    text = "tuân theo, tuân thủ", 
    font = ("Furtura", 24, "bold","italic"),
    anchor = "w",
    justify = "left",
    fg = "#000000",
    bg = "#F2F2F2")

label_vi.place(
    x = 830, y = 407,
    width = 572,
    height = 85)


# Label: Synonyms
label_syn = Label(
    text = ("to comply with; to conform; adhere to; observe"), 
    font = ("cambria", 24, "italic"),
    anchor = "nw",
    justify = "left",
    wraplength = 420,
    fg = "#000000",
    bg = "#F2F2F2")

label_syn.place(
    x = 95, y = 418,
    width = 420,
    height = 240)


# Label: Example
label_exp = Label(
    text = ("After reading the contract, I was still unable to determine if our company was liable for back wages."), 
    font = ("cambria", 20, "italic"),
    anchor = "nw",
    justify = "left",
    wraplength = 750,
    fg = "#000000",
    bg = "#F2F2F2")

label_exp.place(
    x = 617, y = 605,
    width = 784,
    height = 126)


window.resizable(False, False)
window.mainloop()