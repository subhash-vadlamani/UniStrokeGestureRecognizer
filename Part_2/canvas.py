from tkinter import *
import time
import math
from recognition import Recognizer
from templates import *

recognizer = Recognizer()
for template in templates:
	recognizer.addTemplate(template)



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
        matched_template, score = recognizer.recognize(self.line_points)

        self.detected_shape.set(matched_template.name)
        self.detected_score.set("{0:.2f}".format(score * 100))
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

# class MyApp(wx.App):
# 	def OnInit(self):
# 		self.frame = MyFrame(None, "Sample")  # add two lines here
# 		self.frame.Centre()
# 		self.frame.Show(True)
# 		return True
#
#
# class MyFrame(wx.Frame):
# 	def __init__(self, parent, title):
# 		wx.Frame.__init__(self, parent, title=title)
# 		wx.StaticText(self, label='Detected shape:', pos=(10, 10))
# 		wx.StaticText(self, label='Detected score:', pos=(10, 30))
# 		self.detected_shape = wx.StaticText(self, label='', pos=(95, 10))
# 		self.detected_score = wx.StaticText(self, label='', pos=(93, 30))
# 		self.previous_points = []
#
# 		self.Bind(wx.EVT_MOTION, self.OnMotion)
# 		self.Bind(wx.EVT_PAINT, self.OnPaint)
# 		self.Bind(wx.EVT_LEFT_UP, self.LeftUp)
# 		self.Bind(wx.EVT_LEFT_DOWN, self.LeftDown)
#
# 	def OnMotion(self, event):
# 		if event.LeftIsDown() and event.Dragging():
# 			x, y = event.GetPosition()
# 			self.previous_points.append([x, y])
# 			dc = wx.ClientDC(self)
# 			dc.SetPen(wx.Pen(wx.BLACK, 1))
# 			dc.DrawCircle(x, y, 3)
#
# 	def LeftUp(self, event):
# 		matched_template, score = recognizer.recognize(self.previous_points)
# 		self.detected_shape.SetLabel(matched_template.name)
# 		self.detected_score.SetLabel("{0:.2f}".format(score*100))
# 		self.previous_points = []
#
# 	def LeftDown(self, event):
# 		dc = wx.ClientDC(self)
# 		dc.Clear()
#
# if __name__ == '__main__':
# 	app = MyApp(recognizer)
# 	app.MainLoop()
#
# # Tkinter Python package contains all the functions that are required for the GUI that is required for the project
#
# """
# on_mouse_down method is responsible for listening to the left-click events of the mouse and performing the action of
# deleting everything that is already present on the canvas and creating a small oval shaped pointer at the point where
# the mouse was clicked in order to identify the starting point.
# """
# def on_mouse_down(event):
#     w.delete("all")
#     print("Button press")
#     x, y = event.x, event.y
#     global start_x, start_y
#     start_x, start_y = x, y
#     w.create_oval(x-2, y-2, x+2, y+2, fill="black")
#
# """
# on_mouse_dragged method is used to draw the line on the canvas using the 'create_line' method that that
# object of canvas class can access.
# """
#
# def on_mouse_dragged(event):
#     x, y = event.x, event.y
#     global start_x, start_y
#     if not start_x or not start_y:
#         start_x , start_y = x, y
#     # print("start_x: {}, start_y: {}, x: {}, y: {}".format(start_x, start_y, x, y))
#     w.create_line(start_x, start_y, x, y, fill="blue")
#     start_x, start_y = x, y
#     line_points.append([start_x, start_y])
#
# """
# on_mouse_up is triggered when the unistroke is completed. It removes the stored values of 'x' and 'y' coordinates.
# """
# def on_mouse_up(event):
#     global start_x, start_y
#     start_x, start_y = None, None
#     print(line_points)
#     matched_template, score = recognizer.recognize(line_points)
#     print("The Matched template is : {}".format(matched_template.name))
#     print("The score is : {}".format(score * 100))
#     line_points = []
#
#
# """
# 'on_right_click' method allows user to clear the entire canvas with the help of mouse right click.
# """
# def on_right_click(event):
#     w.delete("all")
#
# """
# 'clear_btn_click' method is triggered when the user clicks the 'clear' button on the canvas. This allows the user to
# clear whatever is present on the canvas.
# """
# def clear_btn_click():
#     w.delete("all")
#
#
# top = Tk()
# w = Canvas(top, width=500, height=500) # Canvas object to which we will bind the above methods that are triggered by various events.
#
# # clear button that allows the user to clear the canvas input.
# button = Button(top, text='Clear', width=25, command=clear_btn_click)
# button.pack()
#
# global line_points
#
#
# """
# Code to bind different buttons and motions with those buttons to the corresponding methods so that the
# corresponding methods can be triggered by their respective events.
# """
# w.pack()
# w.bind("<ButtonPress-1>", on_mouse_down)
# w.bind("<B1-Motion>", on_mouse_dragged)
# w.bind("<ButtonRelease-1>", on_mouse_up)
# w.bind("<ButtonPress-2>", on_right_click)
#
#
# # Start the canvas
# start_x,start_y = None, None
# top.mainloop()