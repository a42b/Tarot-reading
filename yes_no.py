import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk

def load_image(file_path, width, height):
    img = Image.open(file_path)
    resized_image = img.resize((180, 80), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

class AnswerApp:
  def __init__(self, root, tarot_cards, tarot_cards_flipped, positive_cards):
    self.root = root
    self.root.title('Answer your question')
    self.tarot_cards = tarot_cards
    self.tarot_cards_flipped = tarot_cards_flipped
    self.positive_cards = positive_cards

    # Frame for input and button
    input_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
    input_frame.grid(row=0, column=0, sticky="nsew")

    # Labels
    ttk.Label(input_frame, text='Enter your question (yes, no)', font=('Helvetica', 14)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Create an entry widget for input
    text_input = tk.Text(input_frame, height=5, width=30, font=('Helvetica', 12))
    text_input.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Card Images
    self.card_label = ttk.Label(root)
    self.card_label.grid(row=1, column=0, pady=10)

    # Button
    self.click_btn = load_image('images/answer.png', 40, 20)
    ttk.Button(input_frame, image=self.click_btn, command=self.get_answer).grid(row=2, column=0, columnspan=2, pady=10)

    # Configure columns and rows to expand with the window
    for i in range(2):  # Assuming 2 columns in input_frame
      input_frame.columnconfigure(i, weight=1)

    for i in range(3):  # Assuming 3 rows in root
      root.rowconfigure(i, weight=1)

    self.tarot_cards_all = list(zip(tarot_cards, tarot_cards_flipped))

    self.card_label.bind("<Button-1>", lambda event, card=self.card_label: self.flip_card(card))

  def get_answer(self):
    # Choose random cards
    card, card_flipped = random.choice(self.tarot_cards_all)

    answer = "No"
    if card in self.positive_cards:
      answer = "Yes"

    # Update labels with card images
    self.card_label['image'] = card
    self.card_label.flipped_image = card_flipped  # Store flipped image reference
    ttk.Label(self.root, text=f'Your answer is {answer}', font=('Helvetica', 14)).grid(row=1, column=2, columnspan=2, pady=(0, 10))

  def flip_card(self, label):
    # Flip the card by swapping the images
    label['image'], label.flipped_image = label.flipped_image, label['image']

if __name__ == "__main__":
  root = tk.Tk()

  width = root.winfo_screenwidth()
  height = root.winfo_screenheight()

  # Setting tkinter window size
  root.geometry("%dx%d" % (width * 0.8, height * 0.8))  # Adjusted proportions

  # Load tarot card images after the Tkinter root window is created
  from tarot_cards import tarot_cards, positive_cards
  from tarot_cards_flipped import tarot_cards_flipped

  app = AnswerApp(root, tarot_cards, tarot_cards_flipped, positive_cards)
  root.mainloop()
