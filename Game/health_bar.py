def text_health(health, max_health):
    return str(health) + "/" + str(max_health)

def health_bar(canvas,max_health,health):
    canvas.create_rectangle(65, 425, 65+375*(health/max_health), 440, fill="green")
    canvas.create_rectangle(65+375*(health/max_health), 425, 440, 440, fill="red")
    canvas.create_text(70, 433, text=text_health(health,max_health), font=("Arial", 10), anchor="w")