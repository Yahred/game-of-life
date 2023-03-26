import tkinter as tk
from threading import Timer
from time import sleep

from classes.game import Universe

root = tk.Tk()

root.title('Game of Life')

universe = Universe(root)


def begin_life(event):
    universe.life_inited = True

    universe.tick()



root.bind('<Return>', begin_life)

root.mainloop()
