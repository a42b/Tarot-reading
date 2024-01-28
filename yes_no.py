import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk

def load_image(file_path, width, height):
    """
    Load an image from a file path and resize it.

    Parameters:
    - file_path (str): The path to the image file.
    - width (int): The desired width of the image.
    - height (int): The desired height of the image.

    Returns:
    - ImageTk.PhotoImage: The resized image wrapped in a PhotoImage object.
    """
    img = Image.open(file_path)
    resized_image = img.resize((180, 80), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

class AnswerApp:
    def __init__(self, root, tarot_cards, tarot_cards_flipped, positive_cards):
        """
        Initialize the Yes/No Answer application.

        Parameters:
        - root (tk.Tk): The main Tkinter window.
        - tarot_cards (list): List of tarot card images.
        - tarot_cards_flipped (list): List of corresponding flipped tarot card images.
        - positive_cards (list): List of tarot cards considered positive for an answer.
        """
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
        """
        Get a random tarot card and determine the answer.

        Display the card image and the answer (Yes/No) in a label.
        """
        # Choose random cards
        card, card_flipped = random.choice(self.tarot_cards_all)

        answer = "No "
        if card in self.positive_cards:
            answer = "Yes"

        # Update labels with card images
        self.card_label['image'] = card
        self.card_label.flipped_image = card_flipped  # Store flipped image reference
        ttk.Label(self.root, text=f'Your answer is {answer}', font=('Helvetica', 14)).grid(row=1, column=2, columnspan=2, pady=(0, 10))

    def flip_card(self, label):
        """
        Flip the displayed tarot card.

        Swap the image with its corresponding flipped image.

        Parameters:
        - label (ttk.Label): The label representing the tarot card.
        """
        # Flip the card by swapping the images
        label['image'], label.flipped_image = label.flipped_image, label['image']
