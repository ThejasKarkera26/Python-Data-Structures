'''9. Create a meaningful canva design with the help of polygon, 
rectangle, line arc, oval and text''' 
from tkinter import * 
# Create window 
root = Tk() 
root.title("Canvas Design Example") 
# Create canvas 
canvas = Canvas(root, width=600, height=500, bg="skyblue") 
canvas.pack() 
# Sun (oval) 
canvas.create_oval(450, 50, 520,100, fill="yellow") 
# Sun rays (line) 
canvas.create_line(485, 40, 485, 20, width=2) 
canvas.create_line(485, 130, 485, 150, width=2) 
canvas.create_line(440, 85, 420, 85, width=2) 
canvas.create_line(530, 85, 550, 85, width=2) 
# House base (rectangle) 
canvas.create_rectangle(200, 250, 400, 380, fill="lightyellow") 
# Roof (polygon) 
canvas.create_polygon(190, 250, 300, 180, 410, 250, fill="brown") 
# Door (rectangle) 
canvas.create_rectangle(285, 310, 315, 380, fill="saddlebrown") 
# Windows (oval) 
canvas.create_oval(220, 280, 260, 320, fill="white") 
canvas.create_oval(340, 280, 380, 320, fill="white") 
# Tree trunk (rectangle) 
canvas.create_rectangle(100, 300, 120, 380, fill="brown") 
# Tree leaves (oval) 
canvas.create_oval(70, 250, 150, 320, fill="green") 
# Road (rectangle) 
canvas.create_rectangle(0, 380, 600, 450, fill="gray") 
# Road curve (arc) 
canvas.create_arc(200, 350, 400, 450, start=0, extent=180, style=ARC, 
width=3) 
# Road divider (line) 
canvas.create_line(0, 415, 600, 415, dash=(10,5), fill="white") 
# Text 
canvas.create_text(300, 460, text="My Beautiful Home", font=("Arial", 16, 
"bold")) 
root.mainloop() 
