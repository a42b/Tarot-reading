import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Function to load images using PIL
def load_image(file_path):
  img = (Image.open(file_path))
  resized_image = img.resize((200, 200), Image.LANCZOS)
  return ImageTk.PhotoImage(resized_image)

# Card Illustrations
magician_flipped = load_image('cards_flipped/magician.png')
popess_flipped = load_image('cards_flipped/popess.png')
empress_flipped = load_image('cards_flipped/empress.png')
emperor_flipped = load_image('cards_flipped/emperor.png')
pope_flipped = load_image('cards_flipped/pope.png')
lovers_flipped = load_image('cards_flipped/lovers.png')
chariot_flipped = load_image('cards_flipped/chariot.png')
justice_flipped = load_image('cards_flipped/justice.png')
hermit_flipped = load_image('cards_flipped/hermit.png')
wheel_fortune_flipped = load_image('cards_flipped/wheel_fortune.png')
force_flipped = load_image('cards_flipped/force.png')
hanged_man_flipped = load_image('cards_flipped/hanged_man.png')
death_flipped = load_image('cards_flipped/death.png')
temperance_flipped = load_image('cards_flipped/temperance.png')
devil_flipped = load_image('cards_flipped/devil.png')
tower_flipped = load_image('cards_flipped/tower.png')
star_flipped = load_image('cards_flipped/star.png')
moon_flipped = load_image('cards_flipped/moon.png')
sun_flipped = load_image('cards_flipped/sun.png')
judgment_flipped = load_image('cards_flipped/judgment.png')
world_flipped = load_image('cards_flipped/world.png')
fool_flipped = load_image('cards_flipped/fool.png')

king_wands_flipped = load_image('cards_flipped/king_wands.png')
queen_wands_flipped = load_image('cards_flipped/queen_wands.png')
knight_wands_flipped = load_image('cards_flipped/knight_wands.png')
knave_wands_flipped = load_image('cards_flipped/knave_wands.png')

ace_wands_flipped = load_image('cards_flipped/ace_wands.png')
two_wands_flipped = load_image('cards_flipped/two_wands.png')
three_wands_flipped = load_image('cards_flipped/three_wands.png')
four_wands_flipped = load_image('cards_flipped/four_wands.png')
five_wands_flipped = load_image('cards_flipped/five_wands.png')
six_wands_flipped = load_image('cards_flipped/six_wands.png')
seven_wands_flipped = load_image('cards_flipped/seven_wands.png')
eight_wands_flipped = load_image('cards_flipped/eight_wands.png')
nine_wands_flipped = load_image('cards_flipped/nine_wands.png')
ten_wands_flipped = load_image('cards_flipped/ten_wands.png')

king_cups_flipped = load_image('cards_flipped/king_cups.png')
queen_cups_flipped = load_image('cards_flipped/queen_cups.png')
knight_cups_flipped = load_image('cards_flipped/knight_cups.png')
knave_cups_flipped = load_image('cards_flipped/knave_cups.png')

ace_cups_flipped = load_image('cards_flipped/ace_cups.png')
two_cups_flipped = load_image('cards_flipped/two_cups.png')
three_cups_flipped = load_image('cards_flipped/three_cups.png')
four_cups_flipped = load_image('cards_flipped/four_cups.png')
five_cups_flipped = load_image('cards_flipped/five_cups.png')
six_cups_flipped = load_image('cards_flipped/six_cups.png')
seven_cups_flipped = load_image('cards_flipped/seven_cups.png')
eight_cups_flipped = load_image('cards_flipped/eight_cups.png')
nine_cups_flipped = load_image('cards_flipped/nine_cups.png')
ten_cups_flipped = load_image('cards_flipped/ten_cups.png')

king_coins_flipped = load_image('cards_flipped/king_coins.png')
queen_coins_flipped = load_image('cards_flipped/queen_coins.png')
knight_coins_flipped = load_image('cards_flipped/knight_coins.png')
knave_coins_flipped = load_image('cards_flipped/knave_coins.png')

ace_coins_flipped = load_image('cards_flipped/ace_coins.png')
two_coins_flipped = load_image('cards_flipped/two_coins.png')
three_coins_flipped = load_image('cards_flipped/three_coins.png')
four_coins_flipped = load_image('cards_flipped/four_coins.png')
five_coins_flipped = load_image('cards_flipped/five_coins.png')
six_coins_flipped = load_image('cards_flipped/six_coins.png')
seven_coins_flipped = load_image('cards_flipped/seven_coins.png')
eight_coins_flipped = load_image('cards_flipped/eight_coins.png')
nine_coins_flipped = load_image('cards_flipped/nine_coins.png')
ten_coins_flipped = load_image('cards_flipped/ten_coins.png')

king_swords_flipped = load_image('cards_flipped/king_swords.png')
queen_swords_flipped = load_image('cards_flipped/queen_swords.png')
knight_swords_flipped = load_image('cards_flipped/knight_swords.png')
knave_swords_flipped = load_image('cards_flipped/knave_swords.png')

ace_swords_flipped = load_image('cards_flipped/ace_swords.png')
two_swords_flipped = load_image('cards_flipped/two_swords.png')
three_swords_flipped = load_image('cards_flipped/three_swords.png')
four_swords_flipped = load_image('cards_flipped/four_swords.png')
five_swords_flipped = load_image('cards_flipped/five_swords.png')
six_swords_flipped = load_image('cards_flipped/six_swords.png')
seven_swords_flipped = load_image('cards_flipped/seven_swords.png')
eight_swords_flipped = load_image('cards_flipped/eight_swords.png')
nine_swords_flipped = load_image('cards_flipped/nine_swords.png')
ten_swords_flipped = load_image('cards_flipped/ten_swords.png')

tarot_cards_flipped = [
    magician_flipped, popess_flipped, empress_flipped, emperor_flipped, pope_flipped,
    lovers_flipped, chariot_flipped, justice_flipped, hermit_flipped, wheel_fortune_flipped,
    force_flipped, hanged_man_flipped, death_flipped, temperance_flipped, devil_flipped,
    tower_flipped, star_flipped, moon_flipped, sun_flipped, judgment_flipped, world_flipped, fool_flipped,

    king_wands_flipped, queen_wands_flipped, knight_wands_flipped, knave_wands_flipped,
    ace_wands_flipped, two_wands_flipped, three_wands_flipped, four_wands_flipped, five_wands_flipped,
    six_wands_flipped, seven_wands_flipped, eight_wands_flipped, nine_wands_flipped, ten_wands_flipped,

    king_cups_flipped, queen_cups_flipped, knight_cups_flipped, knave_cups_flipped,
    ace_cups_flipped, two_cups_flipped, three_cups_flipped, four_cups_flipped, five_cups_flipped,
    six_cups_flipped, seven_cups_flipped, eight_cups_flipped, nine_cups_flipped, ten_cups_flipped,

    king_coins_flipped, queen_coins_flipped, knight_coins_flipped, knave_coins_flipped,
    ace_coins_flipped, two_coins_flipped, three_coins_flipped, four_coins_flipped, five_coins_flipped,
    six_coins_flipped, seven_coins_flipped, eight_coins_flipped, nine_coins_flipped, ten_coins_flipped,

    king_swords_flipped, queen_swords_flipped, knight_swords_flipped, knave_swords_flipped,
    ace_swords_flipped, two_swords_flipped, three_swords_flipped, four_swords_flipped, five_swords_flipped,
    six_swords_flipped, seven_swords_flipped, eight_swords_flipped, nine_swords_flipped, ten_swords_flipped
]