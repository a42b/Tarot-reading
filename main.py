import tkinter as tk
from tkinter import ttk
import tarot_reading
import yes_no

class MainWindow:
  def __init__(self, root):
    """
    initialize the main window of the Tarot application.

    parameters:
    - root (tk.Tk): the main Tkinter window.
    """
    self.root = root
    self.root.title('Tarot Main Menu')

    # maximize the window
    self.root.wm_state('zoomed')

    # set the background color
    self.root['background'] = "#c9a593"

    # increase the font size for buttons
    button_font = ('Helvetica', 16)

    # create a custom style for the buttons
    style = ttk.Style()
    style.configure('TButton', font=button_font)

    # create buttons for tarot reading and getting answers
    ttk.Button(root, text='Tarot reading', command=self.launch_tarot_app, style='TButton').pack(pady=20)
    ttk.Button(root, text='Get answer', command=self.launch_answer_app, style='TButton').pack()

  def launch_tarot_app(self):
    """
    launch the Tarot application.

    opens a new top-level window for tarot reading.

    requires:
    - tarot_cards module
    - tarot_cards_flipped module
    """
    from tarot_cards import tarot_cards
    from tarot_cards_flipped import tarot_cards_flipped
    root = tk.Toplevel()
    window_width, window_height = 900, 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate window position for centering
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    # set window geometry
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

    # launch the TarotApp with the specified parameters
    tarot_reading.TarotApp(root, tarot_cards, tarot_cards_flipped)

  def launch_answer_app(self):
    """
    launch the Yes/No Answer application.

    opens a new top-level window for answering yes/no questions.

    requires:
    - tarot_cards module
    - tarot_cards_flipped module
    - positive_cards module
    """
    from tarot_cards import tarot_cards
    from tarot_cards_flipped import tarot_cards_flipped
    from tarot_cards import positive_cards
    root = tk.Toplevel()
    window_width, window_height = 900, 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate window position for centering
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    # set window geometry
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

    # launch the AnswerApp with the specified parameters
    yes_no.AnswerApp(root, tarot_cards, tarot_cards_flipped, positive_cards)

if __name__ == "__main__":
  # create the main window and start the Tkinter main loop
  root = tk.Tk()
  MainWindow(root)
  root.mainloop()
