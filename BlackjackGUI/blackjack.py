import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Blackjack")
root.minsize(0, 720)

def onClick(event):
    global window
    window.delete('all')

# Create a Canvas widget
window = tk.Canvas(master=root, width=1260, height=720)
# window.bind("<Shift-Button-1>", onClick)
window.pack(fill=tk.BOTH, expand=True)

# Rightside Options Frame
frm_sidebar = tk.Frame(master=window, width=125, height=720, relief=tk.GROOVE, borderwidth=5, bg='#a6660d')
frm_sidebar.pack(fill=tk.Y, side=tk.RIGHT, expand=False)

# Start Game Button
btn_start_game = tk.Button(master=frm_sidebar, text='Start Game', bg='#ba863f')
btn_start_game.pack()

# Table Frame
frm_table = tk.Frame(master=window, width=1000, height=720, relief=tk.SUNKEN, borderwidth=5, bg='#277714')
frm_table.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

# Game Elements
frm_game = tk.Frame(master=frm_table, width=250, height=720, bg='#277714')
frm_game.pack(fill=tk.Y, side=tk.RIGHT, expand=False)

# Deck
facedown = tk.PhotoImage(file="Cards/cardBack_red3.png")
lbl_deck = tk.Label(master=frm_game, image=facedown, bg='#277714')
lbl_deck.pack(padx=5, pady=(15, 5))

# Game Elements
frm_play = tk.Frame(master=frm_table, width= 750, height=720, bg='#277714')
frm_play.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

# Bottom Frame
frm_bottom = tk.Frame(master=frm_play, width=750, height= 50, bg='')
frm_bottom.pack(fill=tk.X, side=tk.BOTTOM)

# Dealer Frame
frm_dealer = tk.Frame(master=frm_play, width=750, height=300, relief=tk.RIDGE, borderwidth=4, bg='#277714')
frm_dealer.pack(fill=tk.X)

lbl_dealer = tk.Label(master=frm_dealer, text='Dealer', font=('Copperplate', 30), bg='#277714')
lbl_dealer.pack()

frm_dealer_cards = tk.Frame(master=frm_dealer, width=750, height=250, bg='#277714')
frm_dealer_cards.pack(fill=tk.X)

# Player Frame
frm_player = tk.Frame(master=frm_play, width=750, height=300, relief=tk.RIDGE, borderwidth=4, bg='#277714')
frm_player.pack(fill=tk.X)

lbl_player = tk.Label(master=frm_player, text='Player', font=('Copperplate', 30), bg='#277714')
lbl_player.pack()

frm_player_cards = tk.Frame(master=frm_player, width=750, height=250, bg='#277714')
frm_player_cards.pack(fill=tk.X)

# Options Frame
frm_options = tk.Frame(master=frm_play, width=750, height= 50, bg='')
frm_options.pack(fill=tk.X)

# Player Options
btn_hit    = tk.Button(master=frm_options, text='Hit',    bg='#a6660d')
btn_stand  = tk.Button(master=frm_options, text='Stand',  bg='#a6660d')
btn_double = tk.Button(master=frm_options, text='Double', bg='#a6660d')
btn_split  = tk.Button(master=frm_options, text='Split',  bg='#a6660d')
btn_hit.pack(side=tk.LEFT)
btn_stand.pack(side=tk.LEFT)
btn_double.pack(side=tk.LEFT)
btn_split.pack(side=tk.LEFT)

# Load the image

Diamonds6 = tk.PhotoImage(file="Cards/cardDiamonds6.png")
ClubsJ    = tk.PhotoImage(file="Cards/cardClubsJ.png")

# Add the image to the canvas
# canvas.create_image(200, 150, image=ClubsJ)
# window.create_image(150, 150, image=Diamonds6)
# window.create_image(200, 150, image=facedown)

# Run the main event loop
root.mainloop()
