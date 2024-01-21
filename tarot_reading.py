import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk

def load_image(file_path, width, height):
  img = (Image.open(file_path))
  resized_image = img.resize((180, 80), Image.LANCZOS)
  return ImageTk.PhotoImage(resized_image)

class TarotApp:
  def __init__(self, root, tarot_cards, tarot_cards_flipped):
    self.root = root
    self.root.title('Tarot Card Reading')
    self.tarot_cards = tarot_cards
    self.tarot_cards_flipped = tarot_cards_flipped
    self.root['background'] = "black"

    self.past_image = load_image('images\past.png', 40, 20)
    self.present_image = load_image('images\present.png', 40, 20)
    self.future_image = load_image('images/future.png', 40, 20)

    # Labels
    ttk.Label(root, text='Past', image=self.past_image,  foreground="white", background="black").grid(row=1, column=0)
    ttk.Label(root, text='Present', image=self.present_image, foreground="white", background="black").grid(row=1, column=1)     
    ttk.Label(root, text='Future', image=self.future_image, foreground="white", background="black").grid(row=1, column=2)

    # Card Images
    self.past_label = ttk.Label(root)
    self.present_label = ttk.Label(root)
    self.future_label = ttk.Label(root)

    self.click_btn = load_image('images\shuffle.png', 40, 20)
    ttk.Button(root, image=self.click_btn, command=self.draw_cards).grid(row=0, column=1)

    # Configure columns and rows to expand with the window
    for i in range(3): 
      root.columnconfigure(i, weight=1)

    for i in range(3): 
      root.rowconfigure(i, weight=1)

    self.tarot_cards_all = list(zip(tarot_cards, tarot_cards_flipped))

    self.past_label.bind("<Button-1>", lambda event, card=self.past_label: self.flip_card(card))
    self.present_label.bind("<Button-1>", lambda event, card=self.present_label: self.flip_card(card))
    self.future_label.bind("<Button-1>", lambda event, card=self.future_label: self.flip_card(card))

  def draw_cards(self):
    # Choose random cards
    past_card, past_card_flipped = random.choice(self.tarot_cards_all)
    present_card, present_card_flipped = random.choice(self.tarot_cards_all)
    future_card, future_card_flipped = random.choice(self.tarot_cards_all)

    # Update labels with card images
    self.past_label['image'] = past_card
    self.past_label.flipped_image = past_card_flipped  # Store flipped image reference
    self.past_label.grid(row=2, column=0, padx=self.calculate_padding())

    self.present_label['image'] = present_card
    self.present_label.flipped_image = present_card_flipped
    self.present_label.grid(row=2, column=1, padx=self.calculate_padding())

    self.future_label['image'] = future_card
    self.future_label.flipped_image = future_card_flipped
    self.future_label.grid(row=2, column=2, padx=self.calculate_padding())

  def flip_card(self, label):
    # Flip the card by swapping the images
    label['image'], label.flipped_image = label.flipped_image, label['image']

  def calculate_padding(self):
    # Calculate proportional padding based on the window width
    window_width = self.root.winfo_width()
    padding_percentage = 0.05 
    return int(window_width * padding_percentage)   

if __name__ == "__main__":
  root = tk.Tk()

  width = root.winfo_screenwidth() 
  height = root.winfo_screenheight()

  # setting tkinter window size
  root.geometry("%dx%d" % (width, height))
  root['background'] = "black"
  from tarot_cards import tarot_cards
  from tarot_cards_flipped import tarot_cards_flipped

  app = TarotApp(root, tarot_cards, tarot_cards_flipped)
  root.mainloop()
