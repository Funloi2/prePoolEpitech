import tkinter as tk
import Game.inventory_bar as ib
import Game.health_bar as hb

def frame():
    root = tk.Tk()
    root.title("GUI Frame")
    root.geometry("500x500")

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()


    hb.health_bar(canvas, 100, 60)
    ib.inventory_bar(root,canvas)

    root.mainloop()
