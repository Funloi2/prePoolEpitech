def score_display(canvas,score):
    canvas.create_text(10, 10, text="Score: " + str(score), font=("Arial", 10), anchor="w")