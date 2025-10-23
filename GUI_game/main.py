from GUI_game.Classes import Player
from GUI_game.Classes.Game import Game
from GUI_game.Classes.Player import get_player_hand
from GUI_game.GUI import (GUI, ImageLoader, Display_full_deck, Display_first_card,
                      Build_buttons, Display_player_decks, Display_player_cards)

# Example card pack
clickables = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]

players = 1  # connect with names later
def Initialize_start_game():
    # Initialize Deck
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
def update_game():
    game, app, root, image_loader = Initialize_start_game()
    current_player_deck = get_player_hand(game.players, 3)
    # Display player decks and cards
    Display_player_decks(root, image_loader, P1=8, P2=6)

    player_cards = Display_player_cards(root, image_loader, current_player_deck, clickables)

    # Example: rotate names after 1 second
    # root.after(1000, lambda: app.rotate_player_names())


    # # main pseudo-game loop
    # while not game_over and getattr(root, "winfo_exists", lambda: True)():
    #     # 1) GUI event processing (keeps the window responsive)
    #     try:
    #         root.update_idletasks()
    #         root.update()
    #     except Exception:
    #         # window closed or Tk error -> exit loop
    #         break
    #
    #     # 2) Read input / user actions
    #     # placeholder: check input queues, button states or clickables
    #     # e.g., clicked_card = app.poll_clicks()  # not implemented here
    #
    #     # 3) Determine current player's available cards
    #     try:
    #         hand = get_player_hand(game.players, current_player)
    #     except Exception:
    #         hand = []  # defensive fallback
    #
    #     # 4) Game logic placeholder
    #     # - validate playable cards
    #     # - if playable: apply move, update game state (remove from hand, add to table)
    #     # - else: draw from deck or pass
    #     # Example (pseudo):
    #     # playable = find_playable_cards(hand, game.table_cards)
    #     # if playable:
    #     #     chosen = playable[0]
    #     #     game.play_card(current_player, chosen)
    #     # else:
    #     #     game.draw_for_player(current_player)
    #
    #     # 5) Update GUI displays for player decks and table
    #
    #     # 6) End-of-turn housekeeping
    #     # rotate to next player (hide and unhide hands as needed)
    #     current_player = current_player + 1
    #
    #     # 7) Check win condition(s)
    #     # Example: if any player has zero cards -> game_over = True
    #     for p in game.players:
    #         if len(p.hand) == 0:
    #             game_over = True
    #             winner_id = p.id
    #             break
    #
    #     # 8) small delay to avoid tight loop; GUI remains responsive due to updates above
    #     time.sleep(tick_delay)
    #
    # # loop exit: final cleanup and optional end-of-game display
    # try:
    #     if game_over:
    #         print(f"Game over. Winner: player {winner_id}")
    #         # display a simple end screen or dialog
    #         # app.show_game_over(winner_id)  # placeholder
    # finally:
    #     # ensure Tk window closes cleanly
    #     try:
    #         root.destroy()
    #     except Exception:
    #         pass


    root.mainloop()


if __name__ == "__main__":
    update_game()