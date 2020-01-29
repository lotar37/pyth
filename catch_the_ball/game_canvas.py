import tkinter
def paint(event):
    print(event.x, event.y)
    canvas.coords(line, 0,0,event.x, event.y)

root = tkinter.Tk()

canvas = tkinter.Canvas(root)
canvas.pack()
canvas.bind("<Motion>",paint)
canvas.create_oval(150,10,190,50, fill='orange', outline='white')
line = canvas.create_line(100, 175, 100, 50, fill='lightblue',width=1)

root.mainloop()
print("Тут и сказочке конец")
