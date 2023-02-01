The following Readme covers the first deliverable for the $1 algorithm implementation

Setup a Development Environment:
We have setup a development environment for the Python Programming language. We have decided to use the Pycharm IDE and the Python
3.11 version. We chose Pycharm because it provides inbuilt terminal access which can be used to execute the python files
with the command 'python <file_name>'. It also provides the debugger tool which can be accessed from the top right of the screen.
The output for the python file is visible in the terminal itself. Pycharm also provides Python Console which can be accessed
from the bottom of the screen.

Instantiate the Canvas:
We have used the Tkinter python library to access the features it provides users to create a canvas. We have imported the
tkinter library(line 1). To create a canvas, we first create an object of the 'TK' class and use that object to create a canvas
(lines 53 to 54). We start the canvas window using the code that is present in line 74.

Listening to Mouse Events:
We created four listener methods for each of the events that we are interested in. 'on_mouse_down' listener method(lines 9 to 15)
is responsible for performing the necessary actions when the left mouse button is first clicked. 'on_mouse_dragged' listener method
(lines 22 to 29) is responsible for displaying whatever the user draws on the canvas. 'on_mouse_up' listener method(lines 34 to 36) is responsible for
ending the diagram once the user releases the left mouse button.

Clearing the Canvas:
We have provided the user with two ways to clear the canvas input. The user can click the right mouse button to clear the
canvas input. 'on_right_click' listener method (lines 42 to 43) is responsible for this. We also provided the user with a
'Clear' button on the top center of the screen. When that button is pressed, a listener method with the name 'clear_btn_click'(lines 49 to 50)
is triggered. We define that button and associate that button to the canvas using the code in the lines 57 and 58.
