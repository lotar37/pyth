import tkinter
from random import choice, randint
screen_width = 400
screen_height = 300

class Ball:
    inition_number = 20
    ball_min_radius = 10
    ball_max_radius = 20
    ball_available_colors = ["green", "blue", "red", "yellow", "magenta"]

    def __init__(self):
        """
         создает шарик в случайном месте холста
         при этом шарик не выходит за границы canvas
         :return:
         """

        self._R = randint(Ball.ball_min_radius, Ball.ball_max_radius)
        self._x = randint(0 + self._R, screen_width - 1 - 2 * self._R)
        self._y = randint(0 + self._R, screen_height - 1 - 2 * self._R)
        self._Vx = randint(-3,3)
        self._Vy = randint(-3,3)

        self._avatar = canvas.create_oval(self._x, self._y, self._x + 2 * self._R, self._y + 2 * self._R, fill=choice(Ball.ball_available_colors), outline='white')


def init_main_window():
    global root, canvas, scores_text, scores_value
    root = tkinter.Tk()

    #canvas = tkinter.Canvas(root,background="white", width=400, height=400)

def init_game():
    """
    создаем необходимое для игры количество объектов
     шариков и объект Пушка
    :return:
    """
    global balls
    balls = [Ball() for i in range(Ball.inition_number)]

if __name__ == "__main__":
    init_main_window()
    init_game()
    root.mainloop()
print("Тут и сказочке конец")