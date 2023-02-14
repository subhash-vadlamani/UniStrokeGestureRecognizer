"""
Authors:
Venkata Satya Sai Subhash Vadlamani (UFID : 4326-8265)
Veera Nitish Mattaparthi (UFID : 4777-4184)

"""


from tkinter import *
import time
import math
from recognition import Recognizer
from templates import *

recognizer = Recognizer()
for template in templates:
	recognizer.addTemplate(template)



class Screen(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title = "Sample"

        # self.top = Tk()
        self.detected_shape = StringVar()
        self.detected_score = StringVar()
        Label(self, text="Detected shape:").grid(row=0, column=0, sticky="W", padx=5, pady=5)
        Label(self, text="Detected score:").grid(row=1, column=0, sticky="W", padx=5, pady=5)

        Label(self, textvariable=self.detected_shape).grid(row=0, column=1, sticky="W", padx=5, pady=5)
        Label(self, textvariable=self.detected_score).grid(row=1, column=1, sticky="W", padx=5, pady=5)


        self.canvas = Canvas(self, width=500, height=500)
        self.canvas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        # self.canvas.pack()
        self.button = Button(self, text='Clear', width=25, command=self.clear_btn_click)
        self.button.grid()
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_dragged)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.canvas.bind("<ButtonPress-2>", self.on_right_click)
        self.line_points = []
        # self.top.mainloop()

    def on_mouse_down(self, event):
        self.canvas.delete("all")
        global global_x, global_y
        global_x, global_y = event.x, event.y

        x1, y1 = (event.x - 3), (event.y - 3)
        x2, y2 = (event.x + 3), (event.y + 3)

        self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

    def on_mouse_dragged(self, event):
        global global_x, global_y
        x, y = event.x, event.y
        # print("start_x: {}, start_y: {}, x: {}, y: {}".format(start_x, start_y, x, y))
        self.canvas.create_line(global_x, global_y,  x, y, fill="blue", width=3)
        self.line_points.append((x, y))
        global_x, global_y = event.x, event.y

    def on_right_click(self, event):
        self.canvas.delete("all")

    def on_mouse_up(self, event):
        matched_template, score = recognizer.recognize(self.line_points)

        self.detected_shape.set(matched_template.name)
        self.detected_score.set("{0:.2f}".format(score * 100))
        self.line_points = []

    def clear_btn_click(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    w = Screen()
    w.mainloop()
