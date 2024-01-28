import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Function to load images using PIL
def load_image(file_path):
  """
  Load an image from a file path and resize it.

  Parameters:
  - file_path (str): The path to the image file.

  Returns:
  - ImageTk.PhotoImage: The resized image wrapped in a PhotoImage object.
  """
  img = Image.open(file_path)
  resized_image = img.resize((200, 400), Image.LANCZOS)
  return ImageTk.PhotoImage(resized_image)

# Card Illustrations
magician = load_image('cards/magician.png')
popess = load_image('cards/popess.png')
empress = load_image('cards/empress.png')
emperor = load_image('cards/emperor.png')
pope = load_image('cards/pope.png')
lovers = load_image('cards/lovers.png')
chariot = load_image('cards/chariot.png')
justice = load_image('cards/justice.png')
hermit = load_image('cards/hermit.png')
wheel_fortune = load_image('cards/wheel_fortune.png')
force = load_image('cards/force.png')
hanged_man = load_image('cards/hanged_man.png')
death = load_image('cards/death.png')
temperance = load_image('cards/temperance.png')
devil = load_image('cards/devil.png')
tower = load_image('cards/tower.png')
star = load_image('cards/star.png')
moon = load_image('cards/moon.png')
sun = load_image('cards/sun.png')
judgment = load_image('cards/judgment.png')
world = load_image('cards/world.png')
fool = load_image('cards/fool.png')

king_wands = load_image('cards/king_wands.png')
queen_wands = load_image('cards/queen_wands.png')
knight_wands = load_image('cards/knight_wands.png')
knave_wands = load_image('cards/knave_wands.png')

ace_wands = load_image('cards/ace_wands.png')
two_wands = load_image('cards/two_wands.png')
three_wands = load_image('cards/three_wands.png')
four_wands = load_image('cards/four_wands.png')
five_wands = load_image('cards/five_wands.png')
six_wands = load_image('cards/six_wands.png')
seven_wands = load_image('cards/seven_wands.png')
eight_wands = load_image('cards/eight_wands.png')
nine_wands = load_image('cards/nine_wands.png')
ten_wands = load_image('cards/ten_wands.png')

king_cups = load_image('cards/king_cups.png')
queen_cups = load_image('cards/queen_cups.png')
knight_cups = load_image('cards/knight_cups.png')
knave_cups = load_image('cards/knave_cups.png')

ace_cups = load_image('cards/ace_cups.png')
two_cups = load_image('cards/two_cups.png')
three_cups = load_image('cards/three_cups.png')
four_cups = load_image('cards/four_cups.png')
five_cups = load_image('cards/five_cups.png')
six_cups = load_image('cards/six_cups.png')
seven_cups = load_image('cards/seven_cups.png')
eight_cups = load_image('cards/eight_cups.png')
nine_cups = load_image('cards/nine_cups.png')
ten_cups = load_image('cards/ten_cups.png')

king_coins = load_image('cards/king_coins.png')
queen_coins = load_image('cards/queen_coins.png')
knight_coins = load_image('cards/knight_coins.png')
knave_coins = load_image('cards/knave_coins.png')

ace_coins = load_image('cards/ace_coins.png')
two_coins = load_image('cards/two_coins.png')
three_coins = load_image('cards/three_coins.png')
four_coins = load_image('cards/four_coins.png')
five_coins = load_image('cards/five_coins.png')
six_coins = load_image('cards/six_coins.png')
seven_coins = load_image('cards/seven_coins.png')
eight_coins = load_image('cards/eight_coins.png')
nine_coins = load_image('cards/nine_coins.png')
ten_coins = load_image('cards/ten_coins.png')

king_swords = load_image('cards/king_swords.png')
queen_swords = load_image('cards/queen_swords.png')
knight_swords = load_image('cards/knight_swords.png')
knave_swords = load_image('cards/knave_swords.png')

ace_swords = load_image('cards/ace_swords.png')
two_swords = load_image('cards/two_swords.png')
three_swords = load_image('cards/three_swords.png')
four_swords = load_image('cards/four_swords.png')
five_swords = load_image('cards/five_swords.png')
six_swords = load_image('cards/six_swords.png')
seven_swords = load_image('cards/seven_swords.png')
eight_swords = load_image('cards/eight_swords.png')
nine_swords = load_image('cards/nine_swords.png')
ten_swords = load_image('cards/ten_swords.png')

tarot_cards = [
  magician, popess, empress, emperor, pope,
  lovers, chariot, justice, hermit, wheel_fortune,
  force, hanged_man, death, temperance, devil,
  tower, star, moon, sun, judgment, world, fool,

  king_wands, queen_wands, knight_wands, knave_wands,
  ace_wands, two_wands, three_wands, four_wands, five_wands,
  six_wands, seven_wands, eight_wands, nine_wands, ten_wands,

  king_cups, queen_cups, knight_cups, knave_cups,
  ace_cups, two_cups, three_cups, four_cups, five_cups,
  six_cups, seven_cups, eight_cups, nine_cups, ten_cups,

  king_coins, queen_coins, knight_coins, knave_coins,
  ace_coins, two_coins, three_coins, four_coins, five_coins,
  six_coins, seven_coins, eight_coins, nine_coins, ten_coins,
  king_swords, queen_swords, knight_swords, knave_swords,
  ace_swords, two_swords, three_swords, four_swords, five_swords,
  six_swords, seven_swords, eight_swords, nine_swords, ten_swords
]

positive_cards = [
  magician, empress, lovers, 
  force, temperance, star, sun, judgment, world,
  king_wands, queen_wands, knave_wands,
  ace_wands, two_wands, three_wands, four_wands, five_wands,
  six_wands, seven_wands, eight_wands, nine_wands, ten_wands,
  king_cups, queen_cups, knight_cups, knave_cups,
  ace_cups, two_cups, three_cups, four_cups, five_cups,
  six_cups, seven_cups, eight_cups, nine_cups, ten_cups,
  king_coins, queen_coins, knight_coins, knave_coins,
  ace_coins, two_coins, three_coins, four_coins, five_coins,
  six_coins, seven_coins, eight_coins, nine_coins, ten_coins,
  king_swords, queen_swords, knight_swords, knave_swords,
  ace_swords, two_swords, three_swords, four_swords, five_swords,
  six_swords, seven_swords, eight_swords, nine_swords, ten_swords
]
