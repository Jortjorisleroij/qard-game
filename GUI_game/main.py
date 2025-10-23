from GUI_game import (GUI, ImageLoader, Display_full_deck, Display_first_card,
                      Build_buttons, Display_player_decks, Display_player_cards)

# Example card pack
cards = ["C_3", "T_5", "R_1", "super", "T_cr", "C_sp", "T_1", "T_2", "T_3", "T_4", "T_5"]
clickables = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]


def Initialize_start_game():
    # Initialize GUI
    app = GUI()
    app.ask_player_names()
    root = app.main_window()
    app.draw_black_square()
    app.draw_table_square()
    app.display_player_names()
    image_loader = ImageLoader(bg_color=(0, 128, 0))
    Display_full_deck(root, image_loader)
    Display_first_card(root, image_loader, random=True)
    buttons = Build_buttons(root)
    buttons.manage_buttons()
    
    return app, root, image_loader



# This part of the main should probably be completely handled by another script. so the back-end. 
def update_game():
    app, root, image_loader = Initialize_start_game()
    
    # Display player decks and cards
    Display_player_decks(root, image_loader, P1=8, P2=6)
    player_cards = Display_player_cards(root, image_loader, cards, clickables)
    
    # Example: rotate names after 1 second
    # root.after(1000, lambda: app.rotate_player_names())
    
    root.mainloop()


if __name__ == "__main__":
    update_game()
