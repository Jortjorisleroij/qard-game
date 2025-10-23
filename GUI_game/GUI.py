# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 23:21:41 2025

@author: jortj
"""


import tkinter as tk
import os, random
from PIL import Image, ImageTk
from tkinter import simpledialog


class ImageLoader:
    def __init__(self, bg_color=(0, 128, 0)):
        self.bg_color = bg_color
        self.cache = {}  # 🟢 cache: {(path, size): PhotoImage}

    def load_card_image(self, path, size):
        size = tuple(size)  # ✅ make sure it’s always a tuple
        key = (path, size)
        if key in self.cache:
            return self.cache[key]
    
        img = Image.open(path).resize(size, Image.LANCZOS)
        if img.mode in ("RGBA", "LA"):
            bg = Image.new("RGBA", img.size, self.bg_color)
            img = Image.alpha_composite(bg, img)
    
        tk_img = ImageTk.PhotoImage(img.convert("RGB"))
        self.cache[key] = tk_img
        return tk_img



class GUI:

    def __init__(self):
        self.height      = 1300
        self.width       = 2000
        self.root        = None  
        self.table_x     = 100
        self.table_y     = 50
        self.table_width = 1650
        self.table_height= 1170
        self.player_names = []  # store player names
        self.name_labels = []   # store Label widgets for easy update

    def main_window(self):
        self.root = tk.Tk()
        self.root.title("Customizable Window")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.configure(bg="lightgray", highlightbackground="black", highlightthickness=20)
        return self.root

    def draw_table_square(self):
        canvas = tk.Canvas(self.root, width=self.table_width, height=self.table_height,
                           bg="green", highlightthickness=0)
        canvas.place(x=self.table_x, y=self.table_y)
        return canvas

    def draw_black_square(self):
        canvas = tk.Canvas(self.root, width=self.table_width + 40, height=self.table_height + 40, 
                           bg="black", highlightthickness=0)
        canvas.place(x=self.table_x - 20, y=self.table_y - 20)
        return canvas


    def ask_player_names(self, num_players=3):
        self.player_names = []
        for i in range(1, num_players + 1):
            name = simpledialog.askstring("Player Name", f"Enter name for Player {i}:")
            if not name:
                name = f"Player {i}"
            self.player_names.append(name)
        return self.player_names


    def display_player_names(self):
        positions = [(0.2, 0.05), (0.8, 0.05), (0.9, 0.85)]  # relative positions for player names
        # Clear previous labels
        for lbl in self.name_labels:
            lbl.destroy()
        self.name_labels = []

        for i, name in enumerate(self.player_names):
            x_rel, y_rel = positions[i % len(positions)]
            label = tk.Label(self.root, text=name, font=("Arial", 24), bg="green")
            label.place(relx=x_rel, rely=y_rel, anchor="n")
            self.name_labels.append(label)

    def rotate_player_names(self):
        if self.player_names:
            # Rotate list by 1: first element goes to the end
            self.player_names = self.player_names[1:] + [self.player_names[0]]
            self.display_player_names()



class Build_buttons:
    
    def __init__(self, root):
        
        self.root        = root
        self.color       = "orange"
        self.hover_color = "darkorange"   # color when hovered
        self.contourcolor= "black"
        
        
    def manage_buttons(self):
        
        for attr in dir(self):
            
            if attr.startswith("button_") and callable(getattr(self, attr)):
                getattr(self, attr)()

        
    def create_rounded_button(self, x, y, w, h, text, command=None, bg_color=None, hover_color=None):
        
        radius = 15
        canvas = tk.Canvas(self.root, width=w, height=h, highlightthickness=0, bg=self.root["bg"])
        canvas.place(x=x, y=y)
        fill_color = bg_color if bg_color else self.color
        hover_fill = hover_color if hover_color else self.hover_color

        # Draw rounded rectangle
        def round_rect(x1, y1, x2, y2, r, **kwargs):
            
            points = [x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r,
                      x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2,
                      x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r,
                      x1, y1+r, x1, y1]
            
            return canvas.create_polygon(points, smooth=True, **kwargs)
        
        rect = round_rect(0, 0, w, h, radius, fill=fill_color, outline=self.contourcolor, width=3)
        label = canvas.create_text(w/2, h/2, text=text, font=("Arial", 14), fill="black")
    
        if command is not None:
            
            def on_enter(e):
                
                canvas.itemconfig(rect, fill=hover_fill)
                
            def on_leave(e):
                
                canvas.itemconfig(rect, fill=fill_color)
            
            canvas.tag_bind(rect , "<Enter>"   , on_enter)
            canvas.tag_bind(label, "<Enter>"   , on_enter)
            canvas.tag_bind(rect , "<Leave>"   , on_leave)
            canvas.tag_bind(label, "<Leave>"   , on_leave)
            canvas.tag_bind(rect , "<Button-1>", lambda e: command())
            canvas.tag_bind(label, "<Button-1>", lambda e: command())
        
        
    def button_I(self, x=1800, y=100, w=130, h=60):
        self.create_rounded_button(x, y, w, h, "Quit", self.on_click)    
    
    def button_X(self, x=1800, y=170, w=130, h=60):
        self.create_rounded_button(x, y, w, h, "Reset", self.on_click)    
 

    def on_click(self):
        """Action performed when button is clicked."""
        print("Button was clicked!")



class Display_full_deck:
    
    def __init__(self, root, image_loader, width=100, height=100):
        
        self.root         = root
        self.image_loader = image_loader
        self.image_path   = os.path.join("visuals", "deck_images", "full_deck.png")
        self.width        = width
        self.height       = height
        self.image_label  = None
        self.root.after(100, self.display_image)

    def display_image(self):
        tk_img = self.image_loader.load_card_image(self.image_path, 
                                                   (self.width, self.height))
        self.image_label = tk.Label(self.root, image=tk_img, bg="green", 
                                    borderwidth=0, highlightthickness=0)
        self.image_label.image = tk_img
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")
        self.image_label.bind("<Button-1>", lambda e: self.deck_clicked())
        self.image_label.bind("<Enter>", lambda e: self.image_label.config(cursor="hand2"))

    def deck_clicked(self):
        print("Deck clicked!")                       



class Display_first_card:
    def __init__(self, root, image_loader, card_name="T_4", random=True):
        self.root          = root
        self.card_name     = card_name
        self.image_loader  = image_loader
        self.image_label   = None
        self.tk_img        = None  # 🟢 persistent reference
        self.deck_x        = 0.5
        self.deck_y        = 0.5
        self.offset_x      = -0.1
        self.custom_width  = 150
        self.custom_height = 200
        self.root.after(200, self.display_a_card)


    def display_a_card(self):

        if self.image_label is not None:
            self.image_label.destroy()        

        if random == True:
            card_files = [f for f in os.listdir(os.path.join("visuals", "common_cards")) 
                          if f.lower().endswith(".png")]
            chosen_file = random.choice(card_files)
            image_path = os.path.join(os.path.join("visuals", "common_cards"), chosen_file)
        
        else:
            image_path = os.path.join("visuals", "mixed_cards", f"{self.card_name}.png")

        self.tk_img = self.image_loader.load_card_image(image_path, (self.custom_width, self.custom_height))
        self.image_label = tk.Label(self.root, image=self.tk_img, bg="green", borderwidth=0, highlightthickness=0)
        self.image_label.place(relx=self.deck_x + self.offset_x, rely=self.deck_y, anchor="center")



class Display_player_decks:
    
    def __init__(self, root, image_loader, offset_x=0.1, width=100, height=100, P1=7, P2=7):
        self.root           = root
        self.image_loader   = image_loader
        self.width          = width
        self.height         = height
        self.P1             = P1
        self.P2             = P2
        self.offset_x       = offset_x
        self.positions      = {"P1": (0.3, 0.2), "P2": (0.7, 0.2)}
        self.images         = {}
        self.labels         = {}
        self.root.after(200, self.display_both_players)

    def display_both_players(self):
        
        self.display_deck("P1", self.P1)
        self.display_deck("P2", self.P2)

    def display_deck(self, player, deck_number):
        
        image_path = os.path.join("visuals", "deck_images", f"deck_0{deck_number}.png")
        if not os.path.exists(image_path):
            print(f"⚠️ Missing image: {image_path}")
            return

        tk_img      = self.image_loader.load_card_image(image_path, (self.width, self.height))
        relx, rely  = self.positions[player]
        label       = tk.Label(self.root, image=tk_img, bg="green", borderwidth=0, highlightthickness=0)
        label.image = tk_img
        label.place(relx=relx, rely=rely, anchor="center")

        self.images[player] = tk_img
        self.labels[player] = label
        print(f"🂡 Displayed {player}: {image_path} at ({relx}, {rely})")



class Display_player_cards:
    
    def __init__(self, root, image_loader, card_array, card_index, width=150, height=200):
        
        self.root = root
        self.image_loader = image_loader
        self.card_array = card_array
        self.card_index = card_index
        self.width = width
        self.height = height
        self.card_loc = [(950,1100),(800,1100),(1100,1100),(950,880),(650,1100),
                         (800,880),(1250,1100),(1100,880),(500,1100),(650,880),
                         (1400,1100),(1250,880),(350,1100),(500,880),(1550,1100),
                         (1400,880),(350,880),(1550,880)]
        self.images = []
        self.labels = []
        self.display_cards()

    def display_cards(self):

        for idx, card_name in enumerate(self.card_array):
            image_path = os.path.join("visuals", "mixed_cards", f"{card_name}.png")
            
            if not os.path.exists(image_path):
                print(f"⚠️ Missing card image: {image_path}")
                continue

            x, y = self.card_loc[idx]
            tk_img = self.image_loader.load_card_image(image_path, (self.width, self.height))
            label = tk.Label(self.root, image=tk_img, bg="green", borderwidth=0, highlightthickness=0)
            label.image = tk_img
            label.place(x=x, y=y, anchor="center")
            self.images.append(tk_img)
            self.labels.append(label)
            print(f"🂠 Displayed {card_name} at ({x}, {y})")

            if idx < len(self.card_index) and self.card_index[idx] == 1:
                label.bind("<Button-1>", lambda e, name=card_name: self.card_clicked(name))
                label.bind("<Enter>", lambda e, lbl=label: lbl.config(cursor="hand2"))
                label.bind("<Leave>", lambda e, lbl=label: lbl.config(cursor=""))  # restore normal cursor
            else:
                label.config(cursor="arrow")  # not clickable

    def card_clicked(self, card_name):
        print(f"🖱️ You clicked on card: {card_name}")






