Project 1 Part2 deliverables are as follows:-

Teammates
1.Subhash Vadlamani :-(UFID 4326-8265)
2.Veera Nitish Mattaparthi:-(UFID 4777-4184)
a. Store the Points
When the user starts creating a new unistroke the function  on_mouse_dragged is invoked we are appending and storing the points as we can see in the line 63 into the line_points.


b. Store some Templates
Used the stored gesture templates from the demo on the $1 recognizer which are kept in the file named templates.py.
In this file all the unistrokes are stored with their co-ordinates so that we can compare with the points generated from the input taken when the mouse is dragged.


c. Implement $1 Algorithm
We have created a class called Recognizer in which all the functions which are used in the $1 Algorithm are delpoyed. The samples are first resampled into the standard 64(numPoints).
The main functions in the $1Recognizer are
Resampling:- resample line 17 to 45 In this lines the resampling process is done .
Rotation:-rotatetoZero line 60 to 63
Scaling:-scaletoSquare line 75 to 86
Translation:-translateToOrigin line 89 to 97

Matching the input with the templates we have stored is done by invoking the function distanceAtBestAngle which calculates the score of the users unistroke.
The function is defined in the lines 116-135 which is being called in the line 109




d. Output the Result:-
The result is displayed on tkinter GUI where we are detecting the unistroke along with the score(on a scale range of 100) . The score displayed is compared with the default templates which we have taken from the templates.py.
The template score and the name are displayed when the code in canvas.py line72,73 are called when the function on_mouse_up is triggered.
