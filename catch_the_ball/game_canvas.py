import tkinter
def paint(event):
    print(event.x, event.y)
    canvas.coords(line, 0,0,event.x, event.y)

def create_random_ball():
    canvas.create_oval(x, y, x+2*R, y+2*R, fill=random_color, outline='white')

def init_ball_catch_game():
    """
    создает необходимоео для игры колличество шариков

    :return:
    """

def click_ball():
    """
    по клику удаляет шарик над которым мышь
    :return:
    """

def create_random_ball()
    """
    создает шарик в случайном месте холста
    при этом шарик не выходит за границы canvas
    :return: 
    """

def init_main_window():
    global root, canvas
    root = tkinter.Tk()

    canvas = tkinter.Canvas(root,background="white", width=400, height=400)
    canvas.pack()
    canvas.bind("<Motion>",paint)
    line = canvas.create_line(100, 175, 100, 50, fill='lightblue',width=1)

init_main_window()
root.mainloop()
print("Тут и сказочке конец")
