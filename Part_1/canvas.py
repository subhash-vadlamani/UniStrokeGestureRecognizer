from tkinter import *
def on_mouse_down(event):
    w.delete("all")
    print("Button press")
    x, y = event.x, event.y
    global start_x, start_y
    start_x, start_y = x, y
    w.create_oval(x-2, y-2, x+2, y+2, fill="black")

def on_mouse_dragged(event):
    x, y = event.x, event.y
    global start_x, start_y
    if not start_x or not start_y:
        start_x , start_y = x, y
    print("start_x: {}, start_y: {}, x: {}, y: {}".format(start_x, start_y, x, y))
    w.create_line(start_x, start_y, x, y, fill="black")
    start_x, start_y = x, y

def on_mouse_up(event):
    global start_x, start_y
    start_x, start_y = None, None

def on_right_click(event):
    w.delete("all")

top = Tk()
w = Canvas(top, width=500, height=500)
w.pack()
w.bind("<ButtonPress-1>", on_mouse_down)
w.bind("<B1-Motion>", on_mouse_dragged)
w.bind("<ButtonRelease-1>", on_mouse_up)
w.bind("<ButtonPress-2>", on_right_click)

start_x,start_y = None, None
top.mainloop()