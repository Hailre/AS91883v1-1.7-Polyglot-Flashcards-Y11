from tkinter import *
from random import *
import random

root = Tk()

global random_word

words = {}
while True:
    add_card_choice = input("Would you like to add a new card (y/n)? or remove the last card (r)")
    if str.lower(add_card_choice) == "n":
        break
    elif str.lower(add_card_choice) == "r":
        if len(words) == 0:
            print("There are currently no Flashcards to remove, please choose 'y' if you would like to create a card.")
        else:
            print("Card:", words.popitem(), "has been removed")
    elif str.lower(add_card_choice) == "y":
        untranslated = input("Untranslated Word: ").capitalize()
        translated = input("Translation: ").capitalize()
        words[untranslated] = translated
    else:
        print("Please enter y (add card), r (remove card) or n (finish card creation)")
    print(words)

word1, word2 = random.choice(list(words.items()))

canvas = Canvas(
    root,
    bg="#f2f3fe",
    height=594,
    width=330,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

# Labels
entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    165.0, 343.5,
    image=entry0_img)

my_entry = Entry(
    bd=0,
    bg="#e4e5ff",
    highlightthickness=0)

my_entry.place(
    x=40.0, y=329,
    width=250.0,
    height=27)


# noinspection PyGlobalUndefined
def nextcard():
    global hinter, hint_count, key
    # Clear screen
    canvas.itemconfig(text="", tagOrId=answer_label)
    my_entry.delete(0, END)
    canvas.itemconfig(text="", tagOrId=hint_label)
    # Reset Hint word
    hinter = ""
    hint_count = 0
    # Get random dictionary value and key and put it into a variable to use as itemconfig text
    random_card = ([(k, v) for k, v in words.items()])
    random.shuffle(random_card)
    for key, value in random_card:
        pass
    canvas.itemconfig(text=key, tagOrId=untranslated_text)


def answer():
    if my_entry.get().capitalize() == word2:
        canvas.itemconfig(text=f"CORRECT! {word1.upper()} MEANS {word2.upper()}", tagOrId=answer_label)
    else:
        canvas.itemconfig(text=f"INCORRECT! {word1.upper()} DOES NOT MEAN {my_entry.get().upper()}",
                          tagOrId=answer_label)


# Keep Track Of the Hints
hinter = ""
hint_count = 0


def hint():
    global hint_count
    global hinter

    if hint_count < len(word2):
        hinter = hinter + word2[hint_count]
        canvas.itemconfig(text=hinter, tagOrId=hint_label)
        hint_count += 1


root.geometry("330x594")
root.iconbitmap('triangles.ico')
root.configure(bg="#f2f3fe")

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    165.0, 297.0,
    image=background_img)

next_button_image = PhotoImage(file=f"img0.png")
next_button = Button(
    image=next_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=nextcard,
    relief="flat")

next_button.place(
    x=41, y=472,
    width=247,
    height=57)

answer_button_image = PhotoImage(file=f"img1.png")
answer_button = Button(
    image=answer_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=answer,
    relief="flat")

answer_button.place(
    x=32, y=380,
    width=107,
    height=35)

hint_button_image = PhotoImage(file=f"img2.png")
hint_button = Button(
    image=hint_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=hint,
    relief="flat")

hint_button.place(
    x=191, y=380,
    width=107,
    height=35)

answer_label = canvas.create_text(
    164.5, 180.0,
    text="",
    fill="#000000",
    font=("Roboto-Bold", int(8)))

# Create Hint Label
hint_label = canvas.create_text(
    164, 275.0,
    text="",
    fill="#000000",
    font=("Roboto-Black", int(9)))

untranslated_text = canvas.create_text(
    164, 240.0,
    text="",
    fill="#000000",
    font=("Roboto-Black", int(23)))

# Run next function when program starts
nextcard()

root.resizable(False, False)
root.mainloop()
