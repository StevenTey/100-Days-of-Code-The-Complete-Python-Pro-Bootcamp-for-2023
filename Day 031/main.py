BACKGROUND_COLOR = "#B1DDC6"

# Import Packages
import pandas as pd
from tkinter import *
import random

# Next Card Function
def next_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=cardfront)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{new_word['French']}", fill="black")
    flip_timer = window.after(3000, func=flip_card)
    
# Flip the Card Function
def flip_card():
    canvas.itemconfig(canvas_image, image=cardback)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{new_word['English']}", fill="white")
    
def is_known():
    to_learn.remove(new_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

cardfront = PhotoImage(file="images/card_front.png")
cardback = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=cardfront)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

right_button = Button(image=right, highlightthickness=0)
right_button.config(bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)
right_button.config(command=next_card)

wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.config(bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)
wrong_button.config(command=next_card)

to_learn = {}
try:
    data_text = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_text.to_dict(orient="records")

next_card()

window.mainloop()