import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Blackjack")

def onClick(event):
    global window
    window.delete('all')

# Create a Canvas widget
window = tk.Canvas(master=root, width=1260, height=720)
# window.bind("<Shift-Button-1>", onClick)
window.pack(fill=tk.BOTH, expand=True)

# Rightside Options Frame
frm_options = tk.Frame(master=window, width=125, height=720, relief=tk.GROOVE, borderwidth=5, bg='#a6660d')
frm_options.pack(fill=tk.Y, side=tk.RIGHT, expand=False)

btn_start_game = tk.Button(master=frm_options, text='Start Game', bg='#a6660d')
btn_start_game.pack()

# Table Frame
frm_table = tk.Frame(master=window, width=1000, height=720, relief=tk.SUNKEN, borderwidth=5, bg='#277714')
frm_table.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

# Game Elements
frm_game = tk.Frame(master=frm_table, width=250, height=720, bg='#277714')
frm_game.pack(fill=tk.Y, side=tk.RIGHT, expand=False)

# Deck
facedown = tk.PhotoImage(file="Cards/cardBack_red3.png")
lbl_deck = tk.Label(master=frm_game, image=facedown)
lbl_deck.pack(padx=5, pady=(15, 5))

# Player Elements
frm_play = tk.Frame(master=frm_table, width= 750, height=720, bg='#277714')
frm_play.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

# Dealer Frame
frm_dealer = tk.Frame(master=frm_play, width=750, height=300, bg='blue')
frm_dealer.pack(fill=tk.X)

# Player Frame
frm_player = tk.Frame(master=frm_play, width=750, height=300)
frm_player.pack(fill=tk.X)

# Bottom Frame

# Load the image

Diamonds6 = tk.PhotoImage(file="Cards/cardDiamonds6.png")
ClubsJ    = tk.PhotoImage(file="Cards/cardClubsJ.png")

# Add the image to the canvas
# canvas.create_image(200, 150, image=ClubsJ)
# window.create_image(150, 150, image=Diamonds6)
# window.create_image(200, 150, image=facedown)

# Run the main event loop
root.mainloop()
