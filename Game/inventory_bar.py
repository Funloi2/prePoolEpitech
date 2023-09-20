
def inventory_slot(i,canvas):
        canvas.create_rectangle(50+40*i, 450, 90+40*i,490, fill="grey")


def inventory_bar(root,canvas):
    for i in range(10):
        inventory_slot(i,canvas)
        canvas.create_text(55+40*i,455,text=str(i+1),font=("Arial", 6))