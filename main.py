import tkinter as tk

from classes.game import Universe

root = tk.Tk()

root.title('Game of Life')

universe = Universe(root)

root.mainloop()
