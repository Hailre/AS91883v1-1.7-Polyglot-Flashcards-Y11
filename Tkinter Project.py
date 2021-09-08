from tkinter import *
from random import randint

root = Tk()
root.title('Flashcards')
root.geometry("375x667")

# Define Image
bg = PhotoImage(file="B:\DOWNLOADS ARCHIVE\FlashCard_GUI.png")
# Create Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

words = []
while True:
    add_card_choice = input("Would you like to add a new card (y/n)? or remove a card (r)")
    if str.lower(add_card_choice) == "n":
        break
    elif str.lower(add_card_choice) == "r":
        print("Removing:", words.pop())
    else:
        untranslated = input("Untranslated Word: ")
        translated = input("Translated Word: ")
        words.append(untranslated)
        words.append(translated)
    # convert list into tuple
    lst = tuple(words)
    # print tuple
    print(lst)

# get a count of our word list
count = len(words)
print(count)


def next():
    global hinter, hint_count
    # Clear screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    # Reset Hint word
    hinter = ""
    hint_count = 0

    # Make a random selection from the list
    global random_word
    random_word = randint(0, count-1)
    # Update label with the untranslated word
    untranslated_text.config(text=words[random_word])


def answer():
    if my_entry.get().lower() == words[random_word]:
        answer_label.config(text=f"Correct! {words[random_word]} means {my_entry.get().lower}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word]} does not mean {my_entry.get().lower()}")


# Keep Track Of the Hints
hinter = ""
hint_count = 0


def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word]):
        hinter = hinter + words[random_word][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1


# Labels
untranslated_text = Label(root, text="", font=("Ostrich Sans", 36, 'bold'))
untranslated_text.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Ostrich Sans", 18))
my_entry.pack(pady=20)

# Create Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1, )

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Run next function when program starts
next()

root.mainloop()
