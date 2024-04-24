Authors:

Venkta Satya Sai Subhash Vadlamani(UFID : 4326-8265)
Veera Nitish Mattaparthi (UFID : 4777-4184)

a (Write Gesture Files)

We are collecting the points of each and every gesture example that the user draws in on the Tkinter Canvas. We first
expect the user to enter the anonymized username that we have assigned to the user in the space provided on the canvas.
The code to accept this input is present in the lines 214 to 219 in canvas.py file and line 90 in the canvas.py file. After the
username has been entered, the user has to press the 'Draw Gestures' button when they are ready to draw the gestures. The code
for this is present in the lines 203 to 210 in canvas.py file and line 84 in canvas.py file. Once the user starts drawing the gesture
the points are stored in the list called 'gesturepoints' and each and every gesture's points are stored in the final list called
'allgestures'. This is present in lines 137 of canvas.py and lines 177 to 178 on canvas.py. Once 10 samples of each and every gesture
is collected, we call the function that is responsible for creating the XML files for all the gestures that are stored.
This is present in the lines 180 to 192 in canvas.py file.

The actual storing of XML files is done in the function 'store_gestures_in_xml' function that is present in the file
recognition.py from the lines 248 to 324 in recognition.py file. Here, we are changing the directory to 'user_logs' and
we are creating the folder with the same name as that of the username if the folder does not already exist. After that,
we are creating a new XML file for each and every gesture example and storing the details of X, Y coordinates and epoch timestamp
(Lines 317 to 321 in recognition.py file). We are also storing the name of the gesture, the example number and the subject number
which will be used in the part 5 of the project(lines 315 of recognition.py file)

b( Prompt for Specific Examples)

The code where we are prompting the user for specific templates and the sample number is present in the code lines
186 and lines 192 of canvas.py file. The code responsible for storing 10 samples of each and every gesture is present in the lines
180 to 182 in canvas.py. When the user is comfortable with the gesture that they have drawn, the can click the 'submit'
button for which the code is present in the lines 82 and the entire action is cofered in the lines 169 to 192 in canvas.py

c(Recruit 6 People): We have recruited 6 people and have asked them to sign the consent forms. We have stored their
consent forms in the folder 'consent_forms' that we have submitted on canvas. We have not used their names to store
the gestures so it is not possible to tell which user has drawn the corresponding set of gestures.

d(Submit Full Dataset) : The entire XML file dataset is present in the 'user_logs' folder. Each and every user has drawn 10 examples
of 16 of those gestures. So, each user has generated 160 XML files. Since there are 6 participants in this experiment,
there are 960 XML files in total.