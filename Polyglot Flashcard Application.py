from tkinter import *
from random import *
import random
import re

root = Tk()
global random_word


# noinspection PyGlobalUndefined
def create_collection():
    global collection_name
    print("≿━━━━༺POLYGLOT༻━━━━≾\n⊱.⋅LANGUAGE FLASHCARDS⋅.⊰")
    while True:
        create_collection_choice = input("\n (c) Create Collection"
                                         "\n (x) Exit App ")
        while True:
            if str.lower(create_collection_choice) == "c":
                collection_name = input("Collection Name (Max. 16 characters): ").upper()[:16]
                if collection_name == "":
                    print("Please enter a collection name")
                else:
                    print(f"\n≿━━━━༺{collection_name}༻━━━━≾")
                    return
            elif str.lower(create_collection_choice) == "x":
                exit()
            else:
                print("Please enter a 'c' (create collection) or 'x' (exit application)")
                break


create_collection()

global collection_name
# Create dictionary from user input
words = {}
while True:
    add_card_choice = input("\nWould you like to:"
                            "\n (y) Add a new card"
                            "\n (n) Present your flashcards"
                            "\n (r) Remove the last card"
                            "\n (x) Cancel card creation"
                            "\n  ")
    if str.lower(add_card_choice) == "n":
        if len(words) == 0:
            print(
                "\nThere are currently no Flashcards to present, please choose 'y' if you would like to create a card. \n     \n   ")
        else:
            print(f"Opening... {collection_name}")
            break
    elif str.lower(add_card_choice) == "r":
        if len(words) == 0:
            print(
                "\nThere are currently no Flashcards to remove, please choose 'y' if you would like to create a card. \n     \n   ")
        else:
            print("\nCard:", words.popitem(), "has been removed")
    elif str.lower(add_card_choice) == "y":
        untranslated = input("\nUntranslated Word (Max. 12 characters): \n").capitalize()[:12]
        if any(x.isalpha() for x in untranslated) or any(x.isspace() for x in untranslated):
            pass
        else:
            print("Sorry! your text contained invalid information, "
                  "\nplease re-enter your information without any integers (1, 2 ,3) or symbols (- * $)")
            continue
        translated = input("\nTranslation (Max. 16 characters): \n").capitalize()[:16]
        if any(x.isalpha() for x in translated) or any(x.isspace() for x in translated):
            pass
        else:
            print("Sorry! your text contained invalid information, "
                  "\nplease re-enter your information without any integers (1, 2 ,3) or symbols (- * $)")
            continue
        words[untranslated] = translated
    elif str.lower(add_card_choice) == "x":
        exit()
    else:
        print("Please enter y (add card), r (remove card) or n (finish card creation)")
    print(f'\n Current Flashcard sets: {words}')

word1, word2 = random.choice(list(words.items()))

# Create base canvas
canvas = Canvas(
    root,
    bg="#f2f3fe",
    height=594,
    width=330,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

# Create and place entry box
entry_image = PhotoImage(file=f"entry.png")
entry = canvas.create_image(
    165.0, 343.5,
    image=entry_image)

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
    global hinter, hint_count, key, value
    # Reset screen
    canvas.itemconfig(text="", tagOrId=answer_label)
    my_entry.delete(0, END)
    canvas.itemconfig(text="", tagOrId=hint_label)
    hinter = ""
    hint_count = 0
    # Get random dictionary value and key and put it into a variable
    random_card = [(k, v) for k, v in words.items()]
    random.shuffle(random_card)
    for key, value in random_card:
        pass
    canvas.itemconfig(text=key.upper(), tagOrId=untranslated_text)


def cardselection():
    # Random words generated from the nextcard function.
    global word1, word2
    word1 = key
    word2 = value


def answer():
    cardselection()
    if my_entry.get().capitalize() == word2:
        canvas.itemconfig(text=f"CORRECT! '{word1.upper()}' \n MEANS {word2.upper()}", tagOrId=answer_label)
    else:
        canvas.itemconfig(text=f" INCORRECT! '{word1.upper()}' \n DOES NOT MEAN \n          {my_entry.get().upper()}",
                          tagOrId=answer_label)


# Keep Track Of the Hints
hinter = ""
hint_count = 0


def hint():
    # Take card selection and place it onto the canvas it letter by letter.
    cardselection()
    global hint_count
    global hinter

    if hint_count < len(word2):
        hinter = hinter + word2[hint_count]
        canvas.itemconfig(text=hinter, tagOrId=hint_label)
        hint_count += 1
    else:
        canvas.itemconfig(text="Hint already used!", tagOrId=hint_label)


def retry():
    # Reset all hint and answer data on the canvas
    global hinter, hint_count
    canvas.itemconfig(text="", tagOrId=answer_label)
    my_entry.delete(0, END)
    canvas.itemconfig(text="", tagOrId=hint_label)
    hinter = ""
    hint_count = 0


# Set app location on screen
app_width = 330
app_height = 594

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

# Set app scale and base information
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.iconbitmap('Logo.ico')
root.configure(bg="#f2f3fe")

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    165.0, 297.0,
    image=background_img)

# Create and place buttons on canvas
next_button_image = PhotoImage(file=f"next.png")
next_button = Button(
    image=next_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=nextcard,
    relief="flat")

next_button.place(
    x=41, y=433,
    width=247,
    height=57)

answer_button_image = PhotoImage(file=f"answer.png")
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

hint_button_image = PhotoImage(file=f"hint.png")
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

retry_button_image = PhotoImage(file=f"retry.png")
retry_button = Button(
    image=retry_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=retry,
    relief="flat")

retry_button.place(
    x=108, y=542,
    width=107,
    height=35)

# Create and place labels on Canvas
answer_label = canvas.create_text(
    165, 165.0,
    text="",
    fill="#9D58FF",
    font=("Roboto-Bold", 8, 'bold'))

hint_label = canvas.create_text(
    165, 275.0,
    text="",
    fill="#828282",
    font=("Roboto", 10, 'bold'))

untranslated_text = canvas.create_text(
    164, 240.0,
    text="",
    fill="#000000",
    font=("Roboto-Bold", 28, 'bold'))

collection_name_label = canvas.create_text(
    164.5, 24.0,
    text=f"{collection_name}",
    fill="#ffffff",
    font=("Roboto", 15, 'bold'))

# Run next function when program starts
nextcard()

root.resizable(False, False)
root.mainloop()
