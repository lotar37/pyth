import tkinter
def print_hello(event):
    print(dir(event))
    event.widget['text'] = "yep"
    #print(dir(event))
def button_click():
    print(1,2,2,3,sep="------")
root = tkinter.Tk()
button1 = tkinter.Button(root,text="button1",command=button_click)
button2 = tkinter.Button(root,text="button2")

button1.bind("<Button>",print_hello)
button1.pack()
button2.bind("<Button>",print_hello)
button2.pack()
root.mainloop()