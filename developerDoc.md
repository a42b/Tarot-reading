Project Structure
main.py
  main.py is the entry point of the application. It creates the main window of the GUI and sets up the main menu for accessing different features of the app.

  Main Classes and Functions:

  MainWindow:
    Initializes the main window with buttons for accessing tarot card readings and getting answers to yes/no questions.
    Utilizes the tarot_reading and yes_no modules to launch specific functionalities.

  launch_tarot_app():
    Creates a new top-level window for the tarot card reading feature.
    Instantiates the TarotApp class from tarot_reading.py and passes necessary parameters.

  launch_answer_app():
    Creates a new top-level window for getting answers to yes/no questions.
    Instantiates the AnswerApp class from yes_no.py and passes necessary parameters.

tarot_reading.py
  tarot_reading.py contains the implementation of the tarot card reading feature. Users can draw three cards representing past, present, and future situations.

  Main Classes and Functions:
    
  TarotApp:
    Initializes the tarot card reading window.
    Provides buttons for shuffling and drawing cards for past, present, and future.
    Displays card images and allows users to flip the cards to reveal their meanings.

  load_image(file_path, width, height):
    Loads and resizes images using the PIL library.

yes_no.py
  yes_no.py implements the feature for answering yes/no questions using tarot cards.

  Main Classes and Functions:

  AnswerApp:
  Initializes the window for answering yes/no questions.
  Users can enter a question, draw a card, and receive an answer based on the drawn card.
  Displays the card image and provides an option to flip the card.

  load_image(file_path, width, height):
    Loads and resizes images using the PIL library.
  
tarot_cards.py and tarot_cards_flipped.py
  These modules contain the images of tarot cards, both in their original and flipped states. Each card is loaded as an ImageTk.PhotoImage object using the PIL library.

How to Run the Application
Ensure you have Python installed on your system.
Install required libraries using: pip install Pillow
Run main.py using Python.

Dependencies
tkinter: Standard GUI library for Python.
Pillow: Used for image processing and handling.