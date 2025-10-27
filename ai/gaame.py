import tkinter as tk
import random
def move(t):
	e, i = tiles.index(" "), tiles.index(t)
	if abs(e - i) in [1, 3]: tiles[e], tiles[i] = tiles[i], tiles[e]; draw()
def draw():
	[buttons[t].grid(row=i//3, column=i%3) for i, t in enumerate(tiles)]
root = tk.Tk(); tiles = [*map(str, range(1, 9)), " "]; random.shuffle(tiles)
buttons = {t: tk.Button(root, text=t, font=("Arial", 20), width=4, height=2, command=lambda x=t: move(x)) for t in tiles}
draw(); root.mainloop()