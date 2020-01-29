import tkinter

def print_hello(event):
    print("hello")

def button_command():
    print("button_command")

def init_main_window():
    """
    Инициализация главного окна, создание всех необходимых виджетов
    и их упаковка
    :return:
    """
    global root, button1, button2, label, text, scale

    root = tkinter.Tk()
    button1 = tkinter.Button(root, text="Button1", command="button_command")
    button1.bind("<Button>", print_hello)

    button2 = tkinter.Button(root, text="Button2", command="button_command")
    button2.bind("<Button>", print_hello)

    variable = tkinter.IntVar(0)
    label = tkinter.Label(root, textvariable=variable)
    scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL, length=300, from_=0, to=100, tickinterval=10, variable=variable)
    text = tkinter.Entry(root, textvariable=variable)



    for obj in button1, button2, label, text, scale:
        obj.pack()


if __name__ == "__main__":
    init_main_window()

    root.mainloop()