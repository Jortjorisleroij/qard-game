"""
Main entry point for GUI application.
"""

from GUI_game import (GUI,ImageLoader,Display_full_deck,Display_first_card,
                      Build_buttons,Display_player_decks,Display_player_cards)



# this is an example card pack. the GUI should receive this from a function in the back-end
cards = ["C_3", "T_5", "R_1", "super", "T_cr", "C_sp", "T_1", "T_2", "T_3", "T_4", "T_5"]
clickables = [1,0,0,0,1,1,0,0,0,0,0]



def main():
    #############################################
    # Initialisation of the interface of the game.
    #############################################
    app = GUI()
    root = app.main_window()
    app.draw_black_square()
    app.draw_table_square()
    image_loader = ImageLoader(bg_color=(0, 128, 0))
    app.ask_player_names()
    app.display_player_names()
    Display_full_deck(root, image_loader, width=200, height=200)
    Display_first_card(root, image_loader, random=True)
    buttons = Build_buttons(root)
    buttons.manage_buttons()
    
    
    ################################################
    # commands to display things throughout the game
    ################################################
    Display_player_decks(root, image_loader, offset_x=0.3, width=300, height=200, P1=8, P2=6)
    player_cards = Display_player_cards(root, image_loader, cards, clickables)
    Display_first_card(root, image_loader, card_name="C_1", random=False)
    
    # command to rotate names.
    #root.after(1000, lambda: app.rotate_player_names())
    
    
    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()
