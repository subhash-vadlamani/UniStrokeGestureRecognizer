from tkinter import *
# Tkinter Python package contains all the functions that are required for the GUI that is required for the project

"""
on_mouse_down method is responsible for listening to the left-click events of the mouse and performing the action of
deleting everything that is already present on the canvas and creating a small oval shaped pointer at the point where 
the mouse was clicked in order to identify the starting point.
"""
def on_mouse_down(event):
    w.delete("all")
    print("Button press")
    x, y = event.x, event.y
    global start_x, start_y
    start_x, start_y = x, y
    w.create_oval(x-2, y-2, x+2, y+2, fill="black")

"""
on_mouse_dragged method is used to draw the line on the canvas using the 'create_line' method that that 
object of canvas class can access.
"""

def on_mouse_dragged(event):
    x, y = event.x, event.y
    global start_x, start_y
    if not start_x or not start_y:
        start_x , start_y = x, y
    # print("start_x: {}, start_y: {}, x: {}, y: {}".format(start_x, start_y, x, y))
    w.create_line(start_x, start_y, x, y, fill="blue")
    start_x, start_y = x, y

"""
on_mouse_up is triggered when the unistroke is completed. It removes the stored values of 'x' and 'y' coordinates.
"""
def on_mouse_up(event):
    global start_x, start_y
    start_x, start_y = None, None


"""
'on_right_click' method allows user to clear the entire canvas with the help of mouse right click.
"""
def on_right_click(event):
    w.delete("all")

"""
'clear_btn_click' method is triggered when the user clicks the 'clear' button on the canvas. This allows the user to 
clear whatever is present on the canvas.
"""
def clear_btn_click():
    w.delete("all")


top = Tk()
w = Canvas(top, width=500, height=500) # Canvas object to which we will bind the above methods that are triggered by various events.

# clear button that allows the user to clear the canvas input.
button = Button(top, text='Clear', width=25, command=clear_btn_click)
button.pack()


"""
Code to bind different buttons and motions with those buttons to the corresponding methods so that the 
corresponding methods can be triggered by their respective events.
"""
w.pack()
w.bind("<ButtonPress-1>", on_mouse_down)
w.bind("<B1-Motion>", on_mouse_dragged)
w.bind("<ButtonRelease-1>", on_mouse_up)
w.bind("<ButtonPress-2>", on_right_click)


# Start the canvas
start_x,start_y = None, None
top.mainloop()