import tkinter as tk
from threading import Thread
from time import sleep


from classes.game import Universe

root = tk.Tk()

root.title('Game of Life')

universe = Universe(root)


life = True
life_thread = None
life_flag = True

def begin_life(event):
    if universe.life_inited:
        return

    universe.life_inited = True

    def tick():
        while True:
            universe.tick()
            sleep(0.2)

    Thread(target=tick).start()
    
def stop_life():
    root.destroy()

root.bind('<Return>', begin_life)

root.protocol('WM_DELETE_WINDOW', stop_life)

root.mainloop()
