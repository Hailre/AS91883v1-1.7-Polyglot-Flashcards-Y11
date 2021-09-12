from tkinter import *
from random import *

root = Tk()
root.title('Flashcards')
root.geometry("375x667")

global random_word

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

# Labels
answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Ostrich Sans", 18))
my_entry.pack(pady=20)


def nextcard():
    global hinter, hint_count
    # Clear screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    # Reset Hint word
    hinter = ""
    hint_count = 0


# Make a random selection from the list
random_word = choice(words)

untranslated_text = Label(root, text="", font=("Ostrich Sans", 36, 'bold'))
untranslated_text.pack(pady=50)

word1 = random_word
word2 = random_word[1]
# Update label with the untranslated word

untranslated_text.configure(text=word1)


def answer():
    if my_entry.get().lower() == word1:
        answer_label.config(text=f"Correct! {word1} means {word2}")
    else:
        answer_label.config(text=f"Incorrect! {word1} does not mean {my_entry.get().lower()}")


# Keep Track Of the Hints
hinter = ""
hint_count = 0


def hint():
    global hint_count
    global hinter

    if hint_count < len(random_word[0]):
        hinter = hinter + random_word[1][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1


# Create Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=nextcard)
next_button.grid(row=0, column=1, )

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Run next function when program starts
nextcard()

root.mainloop()
