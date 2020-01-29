from tkinter import *

root = Tk()
c = Canvas(root, width=200, height=200, bg='white')
c.pack()
c.create_oval(150, 10, 190, 50, fill='orange', outline='white')
c.create_line(100, 175, 100, 50, fill='lightblue', width=100, arrow=LAST, arrowshape="50 50 20")
i = -40
while i < 200:
    c.create_arc(i, 400, (i + 40), 170, start=180, extent=-93, styl=ARC, outline='green', width=2)
    i += 10

root.mainloop()