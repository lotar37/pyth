import tkinter
from random import choice, randint
ball_inition_number = 190
ball_min_radius = 15
ball_max_radius = 40
ball_available_colors = ["green", "blue", "red", "yellow", "magenta"]
def paint(event):
    print(event.x, event.y)

def create_random_ball():
    """
    создает шарик в случайном месте холста
    при этом шарик не выходит за границы canvas
    :return:
    """

    R = randint(ball_min_radius, ball_max_radius)
    x = randint(0+R, int(canvas["width"])-1-2*R)
    y = randint(0+R, int(canvas["height"])-1-2*R)

    canvas.create_oval(x, y, x+2*R, y+2*R, fill=random_color(), outline='white')

def random_color():
    """
    случайный цвет из некоторого набора цветов
    :return:
    """
    return choice(ball_available_colors)
def init_ball_catch_game():
    """
    создает необходимоео для игры колличество шариков

    :return:
    """
    for i in range(ball_inition_number):
        create_random_ball()

def click_ball(event):
    """
    по клику удаляет шарик над которым мышь
    :return:
    """
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)

    if x1<= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        create_random_ball()



def init_main_window():
    global root, canvas
    root = tkinter.Tk()

    canvas = tkinter.Canvas(root,background="white", width=400, height=400)

    canvas.pack()
    canvas.bind("<Motion>",click_ball)
    line = canvas.create_line(100, 175, 100, 50, fill='lightblue',width=1)


if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
print("Тут и сказочке конец")
