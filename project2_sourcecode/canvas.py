"""
Authors:
Venkata Satya Sai Subhash Vadlamani (UFID : 4326-8265)
Veera Nitish Mattaparthi (UFID : 4777-4184)

"""


from tkinter import *
from recognition import Recognizer
from templates import *

recognizer = Recognizer()
for template in templates:
    # temp_template = template
    recognizer.addTemplate(template)
    # recognizer.addTemplateVector(temp_template)


# print("Templates2 is as follows")
# print(templates2)
for template in templates2:
    # print("Adding template vectors")
    recognizer.addTemplateVector(template)


class Screen():
    def __init__(self):
        self.title = "Canvas"

        self.top = Tk()

        """
            Creating variables to store the shape and score.
        """
        self.shape = StringVar()
        self.score = StringVar()
        self.selected_algorithm = StringVar()
        Label(self.top, text="Shape:").grid(row=0, column=0, sticky="W", padx=5, pady=5)
        Label(self.top, text="Score:").grid(row=1, column=0, sticky="W", padx=5, pady=5)

        Label(self.top, textvariable=self.shape).grid(row=0, column=1, sticky="W", padx=5, pady=5)
        Label(self.top, textvariable=self.score).grid(row=1, column=1, sticky="W", padx=5, pady=5)

        self.option1 = Radiobutton(self.top, text='GSS', variable=self.selected_algorithm, value='GSS')
        self.option2 = Radiobutton(self.top, text='Protractor', variable=self.selected_algorithm, value='Protractor')


        self.canvas = Canvas(self.top, width=500, height=500)
        self.canvas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.button = Button(self.top, text='Clear', width=25, command=self.clear_btn_click)
        self.button.grid()
        self.option1.grid()
        self.option2.grid()

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
        self.canvas.create_line(global_x, global_y,  x, y, fill="blue", width=3)
        self.line_points.append((x, y))
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
        # matched_template, score = recognizer.recognize(self.line_points)
        if self.selected_algorithm.get() == 'GSS':
            matched_template, score = recognizer.recognize(self.line_points)
            self.shape.set(matched_template.name)
            self.score.set("{0:.2f}".format(score))
            self.line_points = []
        elif self.selected_algorithm.get() == 'Protractor':
            print("Flow has entered protractor")
            matched_template, score = recognizer.protractorRecognize(self.line_points)
            self.shape.set(matched_template)
            self.score.set("{0:.2f}".format(score))
            self.line_points = []

        # matched_template, score = recognizer.protractorRecognize(self.line_points)

        # self.shape.set(matched_template.name)
        # self.score.set("{0:.2f}".format(score * 100))
        # self.line_points = []

        # self.shape.set(matched_template)
        # self.score.set("{0:.2f}".format(score))
        # self.line_points = []

    """
    'clear_btn_click' method is triggered when the user clicks the 'clear' button on the canvas. This allows the user to 
    clear whatever is present on the canvas.
    """
    def clear_btn_click(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    w = Screen()
