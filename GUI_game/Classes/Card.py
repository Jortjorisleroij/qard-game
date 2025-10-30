import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from GUI import(GUI, ImageLoader, Display_full_deck, Display_first_card,
                Build_buttons, Display_player_decks, Display_player_cards)


# Special names
CRYOSTAT = "cr"
ENTANGLEMENT = "en"
SPIN = "sp"
SUPERFLUID = "su"
TELEPORTATION = "te"
SUPERCONDUCTION = "super"

SPECIALS = [CRYOSTAT, SUPERFLUID, SPIN, ENTANGLEMENT, TELEPORTATION]

# Normal ranks and suits
RANKS = ["1", "2", "3", "4", "5"]

CIRCLE = "C"
SQUARE = "R"
TRIANGLE = "T"
CROSS = "X"
SUITS = [CIRCLE, SQUARE, TRIANGLE, CROSS]

RANK_VALUE = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
}

class Card:
    def __init__(self, kind, rank=None, suit=None, special=None, private_known_for=None):
        self.kind = kind  # 'NORMAL' or 'SPECIAL'
        self.rank = rank  # for normal
        self.suit = suit
        self.special = special  # for special
        self.private_known_for = private_known_for  # player index that can see this card fully

    def __repr__(self):
        if self.kind == 'NORMAL':
            return f"{self.rank}_{self.suit}"
        else:
            return f"{self.special}"



"""
Function that accepts the card currently on the pile and the current players cards.
and generates a binary code for clickables.
"""
class Create_binary_code:
    def __init__(self, pile_card, player_cards):
        self.pile_card = pile_card
        self.player_cards = player_cards
        self.binarycode = []
        self.check_card_fits()
        
    def check_card_fits(self):
        """Check which player cards are compatible and classify them."""
        for card in self.player_cards:
            
            if card.startswith(self.pile_card[0]):
                self.binarycode.append(1)
                print(f"{card} is compatible with {self.pile_card}")

            elif card[2] == self.pile_card[2]:
                self.binarycode.append(1)

            elif card == "super":
                self.binarycode.append(1)

            else:
                self.binarycode.append(0)
                
        print("\nBinary code:", self.binarycode)

"""
example use
"""
#pile = "T_4"
#player_cards = ["T_2", "C_3", "X_4", "super", "R_4", "Z_1"]
#game = Create_binary_code(pile, player_cards)



class Card_compatibility:
    def __init__(self, card_name):
        self.card_name = card_name
        
    
    def Common_or_power(self):
        if len(self.card_name) == 3 and self.card_name[1] == "_":
            self.Play_Common_card()
        else:
            self.Play_power_card()
        
    def Play_Common_card(self):
        Display_first_card(self.root, self.image_loader, card_name=self.card_name)
    
    def Play_power_card(self):
        print("need to figure out what to do depending on card")



# List of tuples: (variable_name, filename)
CARD_LIST = [(f"{suit}_{rank}", f"{suit}_{rank}.png") for suit in SUITS for rank in RANKS]
# Add specials
CARD_LIST += [(f"{suit}_{special}", f"{suit}_{special}.png") for suit in SUITS for special in SPECIALS]
# Add superconduction card
CARD_LIST += [(SUPERCONDUCTION, f"{SUPERCONDUCTION}.png")]

# Dict for quick lookup: variable_name -> filename
CARD_FILE_MAP = dict(CARD_LIST)
if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter(width=120, compact=False)
    print("CARD_LIST:")
    pp.pprint(CARD_LIST)
    print("\nCARD_FILE_MAP:")
    pp.pprint(CARD_FILE_MAP)
    print(f"\nTotal cards: {len(CARD_LIST)}")
