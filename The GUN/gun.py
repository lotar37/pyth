import tkinter
from random import choice, randint
screen_width = 400
screen_height = 300
timer_delay = 100

class Gun():
    def __init__(self):
        self._x = 0
        self._y = screen_height -1
        self._lx = 30
        self._ly = -30
        self._avatar = canvas.create_line(self._x,self._y,self._x +30,self._y -30)

    def shoot(self):
        """
        Возвращает объект снаряда (класса Ball)
        :return:
        """
        bullet = Ball()
        bullet._x = self._lx
        bullet._y = screen_height - 30
        bullet._Vx = self._lx/10
        bullet._Vy = self._ly/10
        bullet._R = 5
        bullet.fly()
        return bullet

class Ball:
    inition_number = 30
    ball_min_radius = 10
    ball_max_radius = 20
    ball_available_colors = ["green", "blue", "red", "yellow", "magenta","black","green",
                             "cyan","pink","orange", "gray", "lightgray", "darkred", "lightgreen", "darkorange"]

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
        self._avatar = canvas.create_oval(self._x, self._y, self._x + 2 * self._R, self._y + 2 * self._R,
                                          fill=choice(Ball.ball_available_colors), outline='white')

    def fly(self):
        self._y += self._Vy
        self._x += self._Vx
        if self._x < 0:
            self._x = 0
            self._Vx = -self._Vx
        elif self._x + 2*self._R > screen_width:
            self._x = screen_width - 2*self._R
            self._Vx = -self._Vx
        if self._y < 0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y + 2*self._R > screen_height:
            self._y = screen_height - 2*self._R
            self._Vy = -self._Vy
        canvas.coords(self._avatar, self._x,self._y,
                      self._x + 2*self._R,self._y + 2*self._R)

 

def init_main_window():
    global root, canvas, scores_text, scores_value
    root = tkinter.Tk()
    root.title("Пушка")
    scores_value = tkinter.IntVar()
    canvas = tkinter.Canvas(root, width=screen_width, height=screen_height, bg="white")
    scores_text = tkinter.Entry(root, textvariable=scores_value)
    canvas.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0,column=2)
    canvas.bind("<Button-1>",click_event_handler)
    #canvas = tkinter.Canvas(root,background="white", width=400, height=400)

def init_game():
    """
    создаем необходимое для игры количество объектов
     шариков и объект Пушка
    :return:
    """
    global balls, gun, bullets_on_fly
    balls = [Ball() for i in range(Ball.inition_number)]
    gun = Gun()
    bullets_on_fly = []

def timer_event():
    print("New time tick")
    for ball in balls:
        ball.fly()
    for bullet in bullets_on_fly:
        bullet.fly()
    canvas.after(timer_delay, timer_event)
def click_event_handler(event):
    global bullets_on_fly
    bullet = gun.shoot()
    bullets_on_fly.append(bullet)
if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()
print("Тут и сказочке конец")