"""
Authors:
Venkata Satya Sai Subhash Vadlamani (UFID : 4326-8265)
Veera Nitish Mattaparthi (UFID : 4777-4184)

"""

from tkinter import *
from recognition import Recognizer
from templates import *
import time
from PIL import ImageTk,Image
from tkinter import ttk

recognizer = Recognizer()
for template in templates:
    recognizer.addTemplate(template)
templatenames = ['triangle', 'x', 'rectangle', 'circle', 'check', 'caret', 'zig_zag', 'arrow',
             'left_square_bracket', 'right_square_bracket', 'v', 'delete',
             'left_curly_brace', 'right_curly_brace', 'star', 'pigtail']






class Screen():
    def __init__(self):
        self.title = "Canvas"
        self.gesturepoints = []
        self.templatecount = 0
        self.counter = 1
        self.user = ''
        self.allgestures = {}
        self.username = None

        self.top = Tk()

        # canvasImage = Canvas(self.top, width=100, height=100)
        # canvasImage.grid()
        # img = ImageTk.PhotoImage(Image.open("gestures.png"))
        # canvasImage.create_image(1, 1, anchor=N, image=img)

        def open_new_win():
            top = Toplevel(self.top)
            canvasImage = Canvas(self.canvas, height=180, width=100, bg="#aaaffe")
            canvasImage.grid()
            img = ImageTk.PhotoImage(Image.open("gestures.png"))
            canvasImage.create_image(1, 1, anchor=N, image=img)

            # Label(canvas1, text="You can modify this text", font='Helvetica 18 bold').grid()
        # img = ImageTk.PhotoImage(Image.open("gestures.png"))
        # self.top.create_image(2, 2, anchor=NW, image=img)
        """
            Creating variables to store the shape and score.
        """
        self.shape = StringVar()
        self.score = StringVar()
        self.shapename = StringVar()
        self.shapename.set("Shape:")

        self.scorename = StringVar()
        self.scorename.set("Score:")
        Label(self.top, textvariable=self.shapename).grid(row=0, column=0, sticky="W", padx=5, pady=5)
        Label(self.top, textvariable=self.scorename).grid(row=1, column=0, sticky="W", padx=5, pady=5)

        Label(self.top, textvariable=self.shape).grid(row=0, column=1, sticky="W", padx=5, pady=5)
        Label(self.top, textvariable=self.score).grid(row=1, column=1, sticky="W", padx=5, pady=5)


        self.canvas = Canvas(self.top, width=500, height=500)

        # button = ttk.Button(self.canvas, text="Open Window", command=open_new_win)
        # button.grid()



        self.canvas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.button = Button(self.top, text='Clear', width=25, command=self.clear_btn_click)
        self.submit_button = Button(self.top, text='Submit', width=25, command=self.submit_btn_click)
        self.draw_button = Button(self.top, text='Draw Gestures', width=25, command=self.draw_button_click)
        self.inputtxt = Text(self.top,
                           height=5,
                           width=20)
        self.username_entry = Entry(self.top)
        self.username_entry.grid()
        self.username_button = Button(self.top, text='Submit Username', command = self.get_username)
        self.username_button.grid()



        self.button.grid()
        self.submit_button.grid()
        self.draw_button.grid()
        # self.inputtxt.grid()
        """
            Binding various actions to the canvas.
        """
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_dragged)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.canvas.bind("<ButtonPress-2>", self.on_right_click)
        self.line_points = []
        self.top.mainloop()
        # self.top.mainloop()

    """
    on_mouse_down method is responsible for listening to the left-click events of the mouse and performing the action of
    deleting everything that is already present on the canvas and creating a small oval shaped pointer at the point where 
    the mouse was clicked in order to identify the starting point.
    """

    def on_mouse_down(self, event):
        self.canvas.delete("all")
        global global_x, global_y
        global_x, global_y = event.x, event.y

        x1, y1 = (event.x - 3), (event.y - 3)
        x2, y2 = (event.x + 3), (event.y + 3)

        self.canvas.create_oval(x1, y1, x2, y2, fill="blue")

    """
    on_mouse_dragged method is used to draw the line on the canvas using the 'create_line' method that that 
    object of canvas class can access.
    """

    def on_mouse_dragged(self, event):
        global global_x, global_y
        x, y = event.x, event.y
        self.canvas.create_line(global_x, global_y, x, y, fill="blue", width=3)
        self.line_points.append((x, y))
        self.gesturepoints.append((x, y, time.time()))
        global_x, global_y = event.x, event.y

    """
    'on_right_click' method allows user to clear the entire canvas with the help of mouse right click.
    """

    def on_right_click(self, event):
        self.canvas.delete("all")

    """
    on_mouse_up is triggered when the unistroke is completed. It removes the stored values of 'x' and 'y' coordinates.
    """

    def on_mouse_up(self, event):
        pass
        matched_template, score = recognizer.recognize(self.line_points)

        self.shape.set(matched_template.name)
        self.score.set("{0:.2f}".format(score * 100))

        self.line_points = []

    """
    'clear_btn_click' method is triggered when the user clicks the 'clear' button on the canvas. This allows the user to 
    clear whatever is present on the canvas.
    """

    def clear_btn_click(self):
        self.canvas.delete("all")

    def submit_btn_click(self):
        # print(self.gesturepoints)



        self.user = self.inputtxt.get(1.0, "end-1c")
        # print("The username is as follows : {}".format(self.username))
        self.allgestures[templatenames[self.templatecount] + str(self.counter).zfill(2)] = self.gesturepoints
        self.gesturepoints = []
        # Counter value is set to 10 to collect 10 samples of each gesture from the user.
        if self.counter == 10:
            self.templatecount += 1
            self.counter = 0
        self.counter += 1
        self.canvas.delete('all')
        try:
            self.shape.set(templatenames[self.templatecount])
        except IndexError:
            self.top.destroy()
            self.top.update()
            recognizer.store_gesture_in_xml(self.username, self.allgestures)
            return
        self.score.set(str((self.counter)))


        # matched_template, score = recognizer.recognize(self.line_points)
        #
        # self.shape.set(matched_template.name)
        # self.score.set("{0:.2f}".format(score * 100))
        # self.line_points = []

    def draw_button_click(self):
        self.scorename.set("Sample Number:")
        self.score.set("")
        self.shape.set("")
        self.canvas.bind("<ButtonRelease-1>", self.dummy)
        self.on_right_click('')
        self.shape.set(templatenames[self.templatecount])
        self.score.set(self.counter)

    def get_username(self):
        self.canvas.delete("userdisplay_label")
        username = self.username_entry.get()
        self.username = username
        display_message = 'The username is : {}'.format(username)
        self.canvas.create_text(100, 100, text=display_message, tags=('userdisplay_label',))


    def dummy(self, event):
        pass


if __name__ == "__main__":
    w = Screen()
