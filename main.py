import tkinter as tk
from tkinter import ttk
import tarot_reading
import yes_no

class MainWindow:
  def __init__(self, root):
    self.root = root
    self.root.title('Tarot Main Menu')

    # Maximize the window
    self.root.wm_state('zoomed')

    # Set the background color
    self.root['background'] = "#c9a593"

    # Increase the font size for buttons
    button_font = ('Helvetica', 16)

    # Create a custom style for the buttons
    style = ttk.Style()
    style.configure('TButton', font=button_font)

    ttk.Button(root, text='Tarot reading', command=self.launch_tarot_app, style='TButton').pack(pady=20)
    ttk.Button(root, text='Get answer', command=self.launch_answer_app, style='TButton').pack()

  def launch_tarot_app(self):
    from tarot_cards import tarot_cards
    from tarot_cards_flipped import tarot_cards_flipped
    root = tk.Toplevel()
    window_width, window_height = 900, 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))
    tarot_reading.TarotApp(root, tarot_cards, tarot_cards_flipped)

  def launch_answer_app(self):
    from tarot_cards import tarot_cards
    from tarot_cards_flipped import tarot_cards_flipped
    from tarot_cards import positive_cards
    root = tk.Toplevel()
    window_width, window_height = 900, 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))
    yes_no.AnswerApp(root, tarot_cards, tarot_cards_flipped, positive_cards)

if __name__ == "__main__":
  root = tk.Tk()
  MainWindow(root)
  root.mainloop()
