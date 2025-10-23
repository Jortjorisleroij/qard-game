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