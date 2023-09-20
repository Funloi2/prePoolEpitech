import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk

def task1_1():
    print("task 1\n")
    print(np.linspace(1, 10, 10))


def task1_2():
    print("task 2\n")
    x = [0, 1, 2, 3]
    # corresponding y axis values
    y = [12, 32, 42, 52]

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()


def task1_3(arrayX, arrayY):


    # plotting the points
    plt.plot(arrayX, arrayY)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()


def f(x):
    return x**2 + x*3 + 2


def plot_fct(func, x_min, x_max):
    x = np.linspace(x_min, x_max, 100)
    y = np.vectorize(func)(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.show()


def task2_1():
    # Create the main application window
    root = tk.Tk()
    root.title("Tkinter")
    root.geometry("400x300")

    # Create a LabelFrame and place it inside the root window
    label_frame = tk.LabelFrame(root, text="Label Frame")
    label_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Create a Frame and place it inside the LabelFrame
    inner_frame = tk.Frame(label_frame)
    inner_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Add widgets (e.g., labels, buttons, etc.) to the inner_frame
    label1 = tk.Label(inner_frame, text="This is inside the Label Frame")
    label1.pack()

    input1 = tk.Entry(inner_frame)
    input1.pack()
    button1 = tk.Button(inner_frame, text="Click Me", command = lambda: printInput(input1) )
    button1.pack()


    # Run the Tkinter main loop
    root.mainloop()

def printInput(input):
    x = input.get()
    print(x.upper())


def task2_2():
    root = tk.Tk()
    root.title("Tkinter Window with Canvas and Background Image")
    root.geometry("400x300")

    # Create a LabelFrame and place it inside the root window
    label_frame = tk.LabelFrame(root, text="Label Frame")
    label_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Create a Frame and place it inside the LabelFrame
    inner_frame = tk.Frame(label_frame)
    inner_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Create a Canvas and place it inside the inner_frame
    canvas = tk.Canvas(inner_frame, width=300, height=200)
    canvas.pack(fill="both", expand=True)

    # Load the background image and display it on the Canvas
    image = Image.open("@propImageMat4_r2.jpg")  # Replace with your image file
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.photo = photo  # Keep a reference to prevent image from being garbage collected

    # Add widgets (e.g., labels, buttons, etc.) to the inner_frame
    label1 = tk.Label(inner_frame, text="This is inside the Label Frame")
    label1.pack()

    button1 = tk.Button(inner_frame, text="Click Me")
    button1.pack()

    # Run the Tkinter main loop
    root.mainloop()


def task2_3():
    root = tk.Tk()
    root.title("Stickman Figure")
    root.geometry("400x400")

    # Create a Canvas widget to draw on
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    label1 = tk.Label(root, text="Hello")
    label1.pack()
    label1.place(x=100, y=10)
    # Draw the stickman figure using lines and a circle
    canvas.create_oval(175, 50, 225, 100, outline="black", fill="green")

    canvas.create_line(200, 100, 200, 250, fill="red")

    canvas.create_line(200, 150, 150, 175, fill="blue")
    canvas.create_line(200, 150, 250, 175, fill="yellow")

    canvas.create_line(200, 250, 150, 325, fill="purple")
    canvas.create_line(200, 250, 250, 325, fill="green")

    # Run the Tkinter main loop
    root.mainloop()






def task2_4():
    root = tk.Tk()
    root.title("Stickman Figure")
    root.geometry("400x400")

    # Create a Canvas widget to draw on
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    label1 = tk.Label(root, text="Hello")
    label1.pack()
    label1.place(x=100, y=10)
    # Draw the stickman figure using lines and a circle
    head = canvas.create_oval(175, 50, 225, 100, outline="black", fill="green")

    body = canvas.create_line(200, 100, 200, 250, fill="red")

    leftArm = canvas.create_line(200, 150, 150, 175, fill="blue")
    rightArm = canvas.create_line(200, 150, 250, 175, fill="yellow")

    leftLeg = canvas.create_line(200, 250, 150, 325, fill="purple")
    rightLeg = canvas.create_line(200, 250, 250, 325, fill="green")

    def moveLeftArm():
        canvas.move(leftArm, 0, -10)
        canvas.move(rightArm, 0, -10)
        canvas.move(head, 0, -10)
        canvas.move(body, 0, -10)
        canvas.move(leftLeg, 0, -10)
        canvas.move(rightLeg, 0, -10)

    button1 = tk.Button(root, text="Animate", command = moveLeftArm)
    button1.pack()


    # Run the Tkinter main loop
    root.mainloop()


def sphere():
    # Create the main application window
    root = tk.Tk()
    root.title("Realistic Sphere in Tkinter")
    root.geometry("400x400")

    # Create a Canvas widget
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # Define the sphere's center and radius
    center_x, center_y = 200, 200
    radius = 100

    # Create concentric circles to simulate the sphere
    num_circles = 30
    for i in range(num_circles):
        shading_color = "#%02x%02x%02x" % (255 - i * 5, 255 - i * 5, 255 - i * 5)
        canvas.create_oval(
            center_x - radius + i,
            center_y - radius + i,
            center_x + radius - i,
            center_y + radius - i,
            outline=shading_color,
            width=2,
        )

    # Run the Tkinter main loop
    root.mainloop()


