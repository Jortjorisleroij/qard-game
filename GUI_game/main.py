# -*- coding: utf-8 -*-
"""
Main entry point for GUI application.
"""

from GUI_game import (
    GUI,
    ImageLoader,
    Display_full_deck,
    Display_first_card,
    Build_buttons,
    Display_player_decks,
    Display_player_cards
)


example_cards = ["C_3", "T_5", "R_1", "super", "T_cr", "C_sp", "T_1", "T_2", "T_3", "T_4", "T_5"]


def main():
    # Initialize GUI
    app = GUI()
    root = app.main_window()
    app.draw_black_square()
    app.draw_table_square()
    image_loader = ImageLoader(bg_color=(0, 128, 0))
    Display_full_deck(root, image_loader, width=200, height=200)
    Display_first_card(root, image_loader, deck_x=0.1, deck_y=0.5, offset_x=0.3, width=150, height=200)
    buttons = Build_buttons(root)
    buttons.manage_buttons()



    # the part that interacts with the backend.
    Display_player_decks(root, image_loader, offset_x=0.3, width=300, height=200, P1=8, P2=6)
    Display_player_cards(root, image_loader, example_cards, width=150, height=200)

    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()
