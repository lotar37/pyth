import tkinter
def paint(event):
    print(event.x, event.y)

root = tkinter.Tk()

canvas = tkinter.Canvas(root)
canvas.pack()
canvas.bind("<Motion>",paint)


root.mainloop()
print("Тут и сказочке конец")
