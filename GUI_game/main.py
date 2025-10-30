from GUI_game.Classes import Player
from GUI_game.Classes.Game import Game
from GUI_game.Classes.Player import get_player_hand
from GUI import (GUI, ImageLoader, Display_full_deck, Display_first_card,
                      Build_buttons, Display_player_decks, Display_player_cards)

# Example card pack
clickables = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]

players = 1  # connect with names later
def Initialize_start_game():
    # Initialize Game
    game = Game()

    # Initialize deck and deal cards
    game.init_and_shuffle_deck()
    game.deal_cards(3, 7)
    face_up_card = game.table()


    # Initialize GUI
    app = GUI()
    app.ask_player_names()
    root = app.main_window()
    app.draw_black_square()
    app.draw_table_square()
    app.display_player_names()
    image_loader = ImageLoader(bg_color=(0, 128, 0))
    Display_full_deck(root, image_loader)
    Display_first_card(root, image_loader, face_up_card)
    buttons = Build_buttons(root)
    buttons.manage_buttons()

    # test print
    print(face_up_card)
    # Return the game instance so callers can access game.players
    return game, app, root, image_loader




# This part of the main should probably be completely handled by another script. so the back-end.
import time

def update_game():
    game, app, root, image_loader = Initialize_start_game()

    # use an index to rotate through the players list
    current_player_idx = 0
    game_over = False
    tick_delay = 0.1  # seconds between turns

    # Display player decks and cards (example values kept)
    Display_player_decks(root, image_loader, P1=8, P2=6)

    # simple turn loop: rotate to next player and check for zero-card win
    while not game_over and getattr(root, "winfo_exists", lambda: True)():
        try:
            root.update_idletasks()
            root.update()
        except Exception:
            # window closed or Tk error -> exit loop
            break

        # current player by index
        current_player = game.players[current_player_idx]
        current_player_deck = getattr(current_player, "hand", [])
        # show 1-based player and display current player hand
        display_player_number = current_player_idx + 1
        print(f"Current player: {display_player_number}, Deck: {current_player_deck}")
        Display_player_cards(root, image_loader, current_player_deck, clickables)



        # check win condition: any player with zero cards
        if game.players[current_player_idx].hand == 0:
            game_over = True
            winner_id = current_player_idx
            break

        if game_over:
            break

        # move to next player
        current_player_idx = (current_player_idx + 1) % len(game.players)

        time.sleep(tick_delay)

    if game_over:
        print(f"Game over. Winner: player {winner_id}")

    try:
        root.destroy()
    except Exception:
        pass



if __name__ == "__main__":
    update_game()