import tkinter as tk
import Game.inventory_bar as ib
import Game.health_bar as hb
import Game.score as sc

def frame():
    root = tk.Tk()
    root.title("Game")
    root.geometry("500x500")

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    sc.score_display(canvas, 100)
    hb.health_bar(canvas, 100, 60)
    ib.inventory_bar(root,canvas)

    root.mainloop()
