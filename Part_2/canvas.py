from tkinter import *
from jspython import *
# import time
# import math
# from recognition import Recognizer
# from templates import *

# recognizer = Recognizer()
# for template in templates:
# 	recognizer.addTemplate(template)



class Screen:
    def __init__(self):
        self.title = "Sample"

        self.top = Tk()
        self.detected_shape = StringVar()
        self.detected_score = StringVar()
        Label(self.top, text="Detected shape:").grid(row=0, column=0, sticky="W", padx=5, pady=5)
        Label(self.top, text="Detected score:").grid(row=1, column=0, sticky="W", padx=5, pady=5)

        Label(self.top, textvariable=self.detected_shape).grid(row=0, column=1, sticky="W", padx=5, pady=5)
        Label(self.top, textvariable=self.detected_score).grid(row=1, column=1, sticky="W", padx=5, pady=5)

        self.line_points = []
        self.canvas = Canvas(self.top, width=500, height=500)
        self.canvas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        # self.canvas.pack()
        self.button = Button(self.top, text='Clear', width=25, command=self.clear_btn_click)
        self.button.grid()
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_dragged)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.canvas.bind("<ButtonPress-2>", self.on_right_click)
        self.top.mainloop()

    def on_mouse_down(self, event):
        self.canvas.delete("all")
        print("Button press")
        self.x, self.y = event.x, event.y
        self.start_x, self.start_y = self.x, self.y
        self.canvas.create_oval(self.x - 3, self.y - 3, self.x + 3, self.y + 3, fill="black")

    def on_mouse_dragged(self, event):
        self.x, self.y = event.x, event.y
        # print("start_x: {}, start_y: {}, x: {}, y: {}".format(start_x, start_y, x, y))
        self.canvas.create_line(self.start_x, self.start_y, self.x, self.y, fill="blue", width=3)
        self.start_x, self.start_y = self.x, self.y
        self.line_points.append([self.start_x, self.start_y])

    def on_right_click(self, event):
        self.canvas.delete("all")
        self.line_points = []

    def on_mouse_up(self, event):
        self.start_x, self.start_y = None, None
        print(self.line_points)
        print("The length of line_points in the main file is : {}".format(len(self.line_points)))
        res = Recognize(self.line_points)
        matched_template, score = res.name, res.score

        self.detected_shape.set(matched_template)
        self.detected_score.set("{0:.2f}".format(score))
        # print("###############")
        # print("The Matched template is : {}".format(matched_template.name))
        # print("The score is : {}".format(score * 100))
        # print("###############")
        self.line_points = []

    def clear_btn_click(self):
        self.canvas.delete("all")
        self.line_points = []


if __name__ == "__main__":
    w = Screen()
