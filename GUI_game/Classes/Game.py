from .Card import CARD_LIST
from GUI_game.Classes.Card import SUITS, RANKS
from .Player import Player
import random


class Game:
    def __init__(self):
        self.players = []
        self.deck = []            # full deck before shuffling
        self.shuffled_deck = []   # draw pile (face-down)
        self.table_cards = []     # face-up pile (renamed to avoid method/attribute conflict)

    def init_and_shuffle_deck(self):
        self.deck = [card_name for card_name, _ in CARD_LIST]
        self.shuffled_deck = self.deck.copy()
        random.shuffle(self.shuffled_deck)

    def table(self):
        """
        Return the latest top card as a string (not a list).
        Uses self.table_cards where the last item is the top card.
        """
        if not self.table_cards:
            return "Table is empty"
        return str(self.table_cards[-1])

    def __str__(self):
        return self.table()

    def ensure_numeric_table_start(self):
        while self.shuffled_deck:
            card = self.shuffled_deck.pop(0)
            if any(card.startswith(f"{suit}_{rank}") for suit in SUITS for rank in RANKS):
                self.table_cards.append(card)
                return
            else:
                self.shuffled_deck.append(card)
        raise ValueError("No numeric card found in the deck to start the table.")

    def deal_cards(self, num_players=3, cards_per_player=7, start_table_card=True):
        players = [Player(i + 1) for i in range(num_players)]
        for _ in range(cards_per_player):
            for player in players:
                if self.shuffled_deck:
                    player.hand.append(self.shuffled_deck.pop(0))

        if start_table_card and self.shuffled_deck:
            self.ensure_numeric_table_start()
        self.players = players
        return players

    def show_table(self):
        print("Table (face-up):")
        top_card = self.table()
        print(top_card)


    def show_deck(self, only_on_table=False):
        if only_on_table:
            self.show_table()
            return
        print("Draw pile (face-down):")
        for card in self.shuffled_deck:
            print(card)

    def play_card(self, card_name, player):
        """Remove card_name from player's hand and add to table.
        Return True if successful, False if card not found."""
        hand = self.hands.get(player)
        if hand is None:
            return False

        if card_name in hand:
            hand.remove(card_name)
            self.table_cards.append(card_name)
            print(f"Played {card_name} from {player} onto table.")
            return True

        print(f"Card {card_name} not in {player} hand.")
        return False


if __name__ == "__main__":
    game = Game()
    game.init_and_shuffle_deck()
    hands = game.deal_cards()
    for i, player in enumerate(hands, 1):
        print(f"Player {i} hand ({len(player.hand)} cards): {player.hand}")

    game.show_deck()
    game.show_table()