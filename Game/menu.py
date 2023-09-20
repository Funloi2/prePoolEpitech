from PIL import Image, ImageTk
import tkinter as tk


def menu_button(root, canvas):
    button = tk.Button(root, text="Menu", command=lambda: show_menu(canvas))
    button.pack()
    button.place(x=450, y=10, width=40, height=20)


def show_menu(canvas):
    menu_container = canvas.create_rectangle(100, 100, 400, 400, fill="grey")
    menu_menu_text = canvas.create_text(250, 150, text="Menu", font=("Arial", 20))
    menu_resume_text = canvas.create_text(250, 200, text="Resume", font=("Arial", 20))
    menu_save_text = canvas.create_text(250, 250, text="Save", font=("Arial", 20))
    menu_load_text = canvas.create_text(250, 300, text="Load", font=("Arial", 20))
    menu_quit_text = canvas.create_text(250, 350, text="Quit", font=("Arial", 20))
    close_button = tk.Button(canvas, text="X", command=lambda: close_menu(canvas))
    close_button.pack()
    close_button.place(x=350, y=110, width=40, height=20)

    def close_menu(canvas):
        canvas.delete(menu_container)
        canvas.delete(menu_menu_text)
        canvas.delete(menu_resume_text)
        canvas.delete(menu_save_text)
        canvas.delete(menu_load_text)
        canvas.delete(menu_quit_text)
        close_button.destroy()
