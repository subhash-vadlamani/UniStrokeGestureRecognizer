Project 2 deliverables are as follows:

Teammates
1.Venkata Satya Sai Subhash Vadlamani :-(UFID 4326-8265)
2.Veera Nitish Mattaparthi:-(UFID 4777-4184)

a. Store the points
When the user starts creating a new unistroke the function 'on_mouse_dragged' in canvas.py file
is invoked in which we are appending and storing the points as we can see in the line 75 into the line_points.

b. Store some Templates
Storage of templates is important because these stored templates are used for the purpouse of recognition.
For the purpouse of live recognition, we have used just one template for each of the 16 gestures.
In Project 2, we have also chosen to implement the $1-algorithm with protractor, for this, we have also
stored the vector representation of points in a seperate variable.

The methods to store the templates and the template vectors are 'addTemplate' and 'addTemplateVector' which are located
starting from lines 190 and 174 respectively in the file recognition.py.

We are calling these methods in the lines 16 and 24 respectively in canvas.py.

c. Implement $1 Algorithm

We have created a class called Recognizer in which all the functions which are used in the $1 Algorithm are present.
Before we go ahead with the process of recognition, we have to preprocess the set of points that are inputted from the user.

In Project 2, we have implemented both the GSS version of the $1 recognition algorithm and also the Protractor version of the
$1 recognition algorithm. For both of them, we have to perform the preprocessing.
The functions in the $1 Recognizer preprocessing are:
Resampling : The code that is responsible for resampling is located from the line 33 to 61 in recognition.py file.
Rotation: method_name -> rotateToZero; line 236 to 243 in recognition.py file.
Scaling : method_name -> scaleToSquare; line 258 to 273 in recognition.py file.
Translation: method_name -> translateToOrigin; line 276 to 287 in recognition.py file.

Vectorization(Only used for Protractor): method_name -> vectorize; line 63 to 92 in recognition.py file.

After the preprocessing of the gesture that is drawn and the templates that are stored in the system is done,
for the purpose of actual recogntion, we call the functions
GSS Recognition : method_name -> recognize; line 337 to 360 in recogntion.py file.
Protractor Recognition : method_name -> protractorRecognize; line 94 to line 116 in recognition.py file.

For the purpose of implementing the recognition algorithm for protractor, we have the following main methods
'recognize', 'vectorize', 'optimalCosineDistance', 'translateToPoint' in recognition.py file.

We have set the 'oSensitive' variable to False in the line 15 of recognition.py file, which makes sure that the Protractor algorithm is not orientation sensitive

d. Data Collection

We collected the gestures using 4 different means. They were, trackpad, mouse, touchscreen, stylus.
We used the code that we submitted for the project 1 part 4 to collect the gestures. We already collected gestures
using the trackpad for project1 part 4 and later on, we collected gestures from 6 people each using the mouse, touchscreen and the stylus
mode. To collect the touchscreen gestures, we just used a laptop that was touch enabled and to collect gestures using the stylus,
we ran our python code from mac to an IPad and we collected the gestures using the stylus of the IPad.

e. Offline Recognition

We have performed offline recognition with both the protractor and the GSS varients. In parse.xml, from line 166 to 170,
we can see that we have used protractor algorithm once and later on we have used GSS. When we want to use protractor,
we comment the GSS part of the code and vice-versa. This way, we generate log file for each and every dataset for both the algorithms.

We have stored the gestures of all the users in the following folders
user_logs -> Gestures that were collected using trackpad
user_logs_mouse -> Gestures that were collected using the mouse
user_logs_touchscreen -> Gestures that were collected using the touchscreen
user_logs_stylus -> Gestures that were collected using the stylus

We have generated the log files for each and every mode of data collection with both Protractor and GSS versions of the
$1 Recognition Algorithm

gesture_logs_gss_trakepad.csv -> Logs corresponding to data that was collected using the trackpad with the GSS variant of the $1 Recognition algorithm
gesture_logs_gss_mouse.csv -> Logs corresponding to data that was collected using the mouse with the GSS variant of the $1 Recognition algorithm
gesture_logs_gss_touchscreen.csv -> Logs corresponding to data that was collected using the touchscreen with the GSS variant of the $1 Recognition algorithm
gesture_logs_gss_stylus.csv -> Logs corresponding to data that was collected using the stylus with the GSS variant of the $1 Recognition algorithm
gesture_logs_protractor_trackpad.csv -> Logs corresponding to data that was collected using the trackpad with the Protractor variant of the $1 Recognition algorithm
gesture_logs_protractor_mouse.csv -> Logs corresponding to data that was collected using the mouse with the Protractor variant of the $1 Recognition algorithm
gesture_logs_protractor_touchscreen.csv -> Logs corresponding to data that was collected using the touchscreen with the Protractor variant of the $1 Recognition algorithm
gesture_logs_protractor_stylus.csv -> Logs corresponding to data that was collected using the stylus with the Protractor variant of the $1 Recognition algorithm

We have also provided the heatmaps of each and every set of gestures that we have collected. In total, there are eight(8)
heatmap images, 4 with the background gestures turned on and 4 without the background gestures turned on which include
all the 4 ways of collecting the gestures(trackpad, mouse, touchscreen, stylus)

heatmap_noback_trackpad.bmp -> Heatmap of the gestures collected using the trackpad without the individual gestures in the background.
heatmap_noback_mouse.bmp -> Heatmap of the gestures collected using the mouse without the individual gestures in the background.
heatmap_noback_touchscreen.bmp -> Heatmap of the gestures collected using the touchscreen without the individual gestures in the background.
heatmap_noback_stylus.bmp -> Heatmap of the gestures collected using the stylus without the individual gestures in the background.
heatmap_withback_trackpad.bmp -> Heatmap of the gestures collected using the trackpad with the individual gestures in the background.
heatmap_withback_mouse.bmp -> Heatmap of the gestures collected using the mouse with the individual gestures in the background.
heatmap_withback_touchscreen.bmp -> Heatmap of the gestures collected using the touchscreen with the individual gestures in the background.
heatmap_withback_stylus.bmp -> Heatmap of the gestures collected using the stylus with the individual gestures in the background.

Feature data for the all the 4 types of gestures:

feature_data_trackpad.csv -> Feature data for the gestures that were collected using a trackpad.
feature_data_mouse.csv -> Feature data for the gestures that were collected using a mouse.
feature_data_touchscreen.csv -> Feature data for the gestures that were collected using a touchscreen.
feature_data_stylus.csv -> Feature data for the gestures that were collected using a stylus.

The consent forms for users from which we collected data using the trackpad method are in the file named "Consent forms HCIRA Project 1 part4.pdf".
The consent forms for the users from which we collected data using the mouse, touchscreen and stylus method are in the file named "Consent forms HCIRA Project 2.pdf".


We have demonstrated the working of our project2 in the video titled 'project2_video1.mp4'.

Final Accuracies:

Protractor, trackpad accuracy

* For E = 1, the average recognition score is 0.746875
* For E = 2, the average recognition score is 0.858125
* For E = 3, the average recognition score is 0.889375
* For E = 4, the average recognition score is 0.86875
* For E = 5, the average recognition score is 0.8925
* For E = 6, the average recognition score is 0.88875
* For E = 7, the average recognition score is 0.888125
* For E = 8, the average recognition score is 0.894375
* For E = 9, the average recognition score is 0.88625

The total average accuracy across all users and E values is 0.871875.

U -------: user2


Recognition score for User : user2, E value : 1 is 0.84375
Recognition score for User : user2, E value : 2 is 0.91875
Recognition score for User : user2, E value : 3 is 0.9375
Recognition score for User : user2, E value : 4 is 0.9375
Recognition score for User : user2, E value : 5 is 0.9625
Recognition score for User : user2, E value : 6 is 0.95
Recognition score for User : user2, E value : 7 is 0.93125
Recognition score for User : user2, E value : 8 is 0.9625
Recognition score for User : user2, E value : 9 is 0.9375
U -------: user5
Recognition score for User : user5, E value : 1 is 0.74375
Recognition score for User : user5, E value : 2 is 0.8
Recognition score for User : user5, E value : 3 is 0.85625
Recognition score for User : user5, E value : 4 is 0.85625
Recognition score for User : user5, E value : 5 is 0.8875
Recognition score for User : user5, E value : 6 is 0.85625
Recognition score for User : user5, E value : 7 is 0.8375
Recognition score for User : user5, E value : 8 is 0.89375
Recognition score for User : user5, E value : 9 is 0.90625
U -------: user4
Recognition score for User : user4, E value : 1 is 0.68125
Recognition score for User : user4, E value : 2 is 0.75625
Recognition score for User : user4, E value : 3 is 0.825
Recognition score for User : user4, E value : 4 is 0.775
Recognition score for User : user4, E value : 5 is 0.78125
Recognition score for User : user4, E value : 6 is 0.79375
Recognition score for User : user4, E value : 7 is 0.80625
Recognition score for User : user4, E value : 8 is 0.81875
Recognition score for User : user4, E value : 9 is 0.83125
U -------: user3
Recognition score for User : user3, E value : 1 is 0.75
Recognition score for User : user3, E value : 2 is 0.8375
Recognition score for User : user3, E value : 3 is 0.8875
Recognition score for User : user3, E value : 4 is 0.90625
Recognition score for User : user3, E value : 5 is 0.925
Recognition score for User : user3, E value : 6 is 0.9125
Recognition score for User : user3, E value : 7 is 0.925
Recognition score for User : user3, E value : 8 is 0.93125
Recognition score for User : user3, E value : 9 is 0.9
U -------: user6
Recognition score for User : user6, E value : 1 is 0.7
Recognition score for User : user6, E value : 2 is 0.875
Recognition score for User : user6, E value : 3 is 0.88125
Recognition score for User : user6, E value : 4 is 0.825
Recognition score for User : user6, E value : 5 is 0.8125
Recognition score for User : user6, E value : 6 is 0.86875
Recognition score for User : user6, E value : 7 is 0.9125
Recognition score for User : user6, E value : 8 is 0.85625
Recognition score for User : user6, E value : 9 is 0.875
U -------: user1
Recognition score for User : user1, E value : 1 is 0.80625
Recognition score for User : user1, E value : 2 is 0.91875
Recognition score for User : user1, E value : 3 is 0.95625
Recognition score for User : user1, E value : 4 is 0.95
Recognition score for User : user1, E value : 5 is 0.975
Recognition score for User : user1, E value : 6 is 0.9625
Recognition score for User : user1, E value : 7 is 0.94375
Recognition score for User : user1, E value : 8 is 0.9625
Recognition score for User : user1, E value : 9 is 0.9375
The total average accuracy is : 0.871875




********************************************

Protractor , stylus accuracy

For E=1: 0.7078125
For E=2: 0.825
For E=3: 0.828125
For E=4: 0.8833333333333333
For E=5: 0.8770833333333333
For E=6: 0.8666666666666667
For E=7: 0.8981481481481481
For E=8: 0.8962962962962963
For E=9: 0.9222222222222223
The total average accuracy is: 0.8679398148148149


U -------: user06
Recognition score for User : user06, E value : 1 is 0.7
Recognition score for User : user06, E value : 2 is 0.9125
Recognition score for User : user06, E value : 3 is 0.8375
Recognition score for User : user06, E value : 4 is 0.9125
Recognition score for User : user06, E value : 5 is 0.90625
Recognition score for User : user06, E value : 6 is 0.925
Recognition score for User : user06, E value : 7 is 0.95625
Recognition score for User : user06, E value : 8 is 0.93125
Recognition score for User : user06, E value : 9 is 0.99375
U -------: user01
Recognition score for User : user01, E value : 1 is 0.60625
Recognition score for User : user01, E value : 2 is 0.76875
Recognition score for User : user01, E value : 3 is 0.79375
Recognition score for User : user01, E value : 4 is 0.8125
Recognition score for User : user01, E value : 5 is 0.80625
Recognition score for User : user01, E value : 6 is 0.84375
Recognition score for User : user01, E value : 7 is 0.8875
Recognition score for User : user01, E value : 8 is 0.88125
Recognition score for User : user01, E value : 9 is 0.85625
U -------: user02
Recognition score for User : user02, E value : 1 is 0.64375
Recognition score for User : user02, E value : 2 is 0.80625
Recognition score for User : user02, E value : 3 is 0.8625
Recognition score for User : user02, E value : 4 is 0.8875
Recognition score for User : user02, E value : 5 is 0.88125
Recognition score for User : user02, E value : 6 is 0.8875
Recognition score for User : user02, E value : 7 is 0.9
Recognition score for User : user02, E value : 8 is 0.875
Recognition score for User : user02, E value : 9 is 0.93125
U -------: user05
Recognition score for User : user05, E value : 1 is 0.7375
Recognition score for User : user05, E value : 2 is 0.93125
Recognition score for User : user05, E value : 3 is 0.90625
Recognition score for User : user05, E value : 4 is 0.90625
Recognition score for User : user05, E value : 5 is 0.925
Recognition score for User : user05, E value : 6 is 0.88125
Recognition score for User : user05, E value : 7 is 0.925
Recognition score for User : user05, E value : 8 is 0.93125
Recognition score for User : user05, E value : 9 is 0.9625
U -------: user04
Recognition score for User : user04, E value : 1 is 0.80625
Recognition score for User : user04, E value : 2 is 0.83125
Recognition score for User : user04, E value : 3 is 0.88125
Recognition score for User : user04, E value : 4 is 0.91875
Recognition score for User : user04, E value : 5 is 0.9375
Recognition score for User : user04, E value : 6 is 0.90625
Recognition score for User : user04, E value : 7 is 0.9375
Recognition score for User : user04, E value : 8 is 0.95
Recognition score for User : user04, E value : 9 is 0.95
U -------: user03
Recognition score for User : user03, E value : 1 is 0.75
Recognition score for User : user03, E value : 2 is 0.81875
Recognition score for User : user03, E value : 3 is 0.84375
Recognition score for User : user03, E value : 4 is 0.86875
Recognition score for User : user03, E value : 5 is 0.8875
Recognition score for User : user03, E value : 6 is 0.83125
Recognition score for User : user03, E value : 7 is 0.875
Recognition score for User : user03, E value : 8 is 0.88125
Recognition score for User : user03, E value : 9 is 0.88125
The total average accuracy is : 0.8679398148148149


************************************

Protractor, Touchscreen accuracy

For E value 1: 0.70833
For E value 2: 0.82917
For E value 3: 0.82847
For E value 4: 0.88229
For E value 5: 0.88125
For E value 6: 0.87604
For E value 7: 0.89583
For E value 8: 0.89479
For E value 9: 0.90833
The total average accuracy is 0.86794, which is the average of all the recognition scores across all users and E values.


U -------: user06
Recognition score for User : user06, E value : 1 is 0.80625
Recognition score for User : user06, E value : 2 is 0.9125
Recognition score for User : user06, E value : 3 is 0.88125
Recognition score for User : user06, E value : 4 is 0.93125
Recognition score for User : user06, E value : 5 is 0.90625
Recognition score for User : user06, E value : 6 is 0.925
Recognition score for User : user06, E value : 7 is 0.8875
Recognition score for User : user06, E value : 8 is 0.91875
Recognition score for User : user06, E value : 9 is 0.9375
U -------: user01
Recognition score for User : user01, E value : 1 is 0.91875
Recognition score for User : user01, E value : 2 is 0.925
Recognition score for User : user01, E value : 3 is 0.96875
Recognition score for User : user01, E value : 4 is 0.975
Recognition score for User : user01, E value : 5 is 0.9625
Recognition score for User : user01, E value : 6 is 0.95
Recognition score for User : user01, E value : 7 is 0.95
Recognition score for User : user01, E value : 8 is 0.95
Recognition score for User : user01, E value : 9 is 0.9625
U -------: user02
Recognition score for User : user02, E value : 1 is 0.8625
Recognition score for User : user02, E value : 2 is 0.925
Recognition score for User : user02, E value : 3 is 0.95
Recognition score for User : user02, E value : 4 is 0.95
Recognition score for User : user02, E value : 5 is 0.98125
Recognition score for User : user02, E value : 6 is 0.95
Recognition score for User : user02, E value : 7 is 0.9625
Recognition score for User : user02, E value : 8 is 0.96875
Recognition score for User : user02, E value : 9 is 0.98125
U -------: user05
Recognition score for User : user05, E value : 1 is 0.7125
Recognition score for User : user05, E value : 2 is 0.8
Recognition score for User : user05, E value : 3 is 0.86875
Recognition score for User : user05, E value : 4 is 0.86875
Recognition score for User : user05, E value : 5 is 0.8875
Recognition score for User : user05, E value : 6 is 0.9125
Recognition score for User : user05, E value : 7 is 0.8875
Recognition score for User : user05, E value : 8 is 0.925
Recognition score for User : user05, E value : 9 is 0.925
U -------: user04
Recognition score for User : user04, E value : 1 is 0.825
Recognition score for User : user04, E value : 2 is 0.88125
Recognition score for User : user04, E value : 3 is 0.9125
Recognition score for User : user04, E value : 4 is 0.89375
Recognition score for User : user04, E value : 5 is 0.9375
Recognition score for User : user04, E value : 6 is 0.9125
Recognition score for User : user04, E value : 7 is 0.93125
Recognition score for User : user04, E value : 8 is 0.93125
Recognition score for User : user04, E value : 9 is 0.95
U -------: user03
Recognition score for User : user03, E value : 1 is 0.9375
Recognition score for User : user03, E value : 2 is 0.95
Recognition score for User : user03, E value : 3 is 0.96875
Recognition score for User : user03, E value : 4 is 0.9625
Recognition score for User : user03, E value : 5 is 0.975
Recognition score for User : user03, E value : 6 is 0.95
Recognition score for User : user03, E value : 7 is 0.9625
Recognition score for User : user03, E value : 8 is 0.96875
Recognition score for User : user03, E value : 9 is 0.96875
The total average accuracy is : 0.922337962962963



*********************

Protractor, online data

E=1 -> 0.970625
E=2 -> 0.99
E=3 -> 0.99
E=4 ->  0.9925
E = 5 -> 0.993125
E = 6 -> 0.995625
E = 7 -> 0.995625
E = 8 -> 0.994375
E = 9 -> 0.994375

U -------: s05
Recognition score for User : s05, E value : 1 is 0.975
Recognition score for User : s05, E value : 2 is 0.99375
Recognition score for User : s05, E value : 3 is 0.99375
Recognition score for User : s05, E value : 4 is 0.99375
Recognition score for User : s05, E value : 5 is 1.0
Recognition score for User : s05, E value : 6 is 1.0
Recognition score for User : s05, E value : 7 is 1.0
Recognition score for User : s05, E value : 8 is 1.0
Recognition score for User : s05, E value : 9 is 1.0
U -------: s02
Recognition score for User : s02, E value : 1 is 0.9875
Recognition score for User : s02, E value : 2 is 0.99375
Recognition score for User : s02, E value : 3 is 1.0
Recognition score for User : s02, E value : 4 is 1.0
Recognition score for User : s02, E value : 5 is 1.0
Recognition score for User : s02, E value : 6 is 1.0
Recognition score for User : s02, E value : 7 is 1.0
Recognition score for User : s02, E value : 8 is 1.0
Recognition score for User : s02, E value : 9 is 1.0
U -------: s03
Recognition score for User : s03, E value : 1 is 0.975
Recognition score for User : s03, E value : 2 is 1.0
Recognition score for User : s03, E value : 3 is 0.99375
Recognition score for User : s03, E value : 4 is 0.9875
Recognition score for User : s03, E value : 5 is 0.99375
Recognition score for User : s03, E value : 6 is 0.99375
Recognition score for User : s03, E value : 7 is 1.0
Recognition score for User : s03, E value : 8 is 1.0
Recognition score for User : s03, E value : 9 is 1.0
U -------: s04
Recognition score for User : s04, E value : 1 is 0.99375
Recognition score for User : s04, E value : 2 is 0.99375
Recognition score for User : s04, E value : 3 is 1.0
Recognition score for User : s04, E value : 4 is 0.99375
Recognition score for User : s04, E value : 5 is 0.99375
Recognition score for User : s04, E value : 6 is 0.99375
Recognition score for User : s04, E value : 7 is 0.99375
Recognition score for User : s04, E value : 8 is 1.0
Recognition score for User : s04, E value : 9 is 0.99375
U -------: s10
Recognition score for User : s10, E value : 1 is 0.975
Recognition score for User : s10, E value : 2 is 0.99375
Recognition score for User : s10, E value : 3 is 1.0
Recognition score for User : s10, E value : 4 is 1.0
Recognition score for User : s10, E value : 5 is 1.0
Recognition score for User : s10, E value : 6 is 1.0
Recognition score for User : s10, E value : 7 is 1.0
Recognition score for User : s10, E value : 8 is 1.0
Recognition score for User : s10, E value : 9 is 1.0
U -------: s11
Recognition score for User : s11, E value : 1 is 0.94375
Recognition score for User : s11, E value : 2 is 0.99375
Recognition score for User : s11, E value : 3 is 0.9875
Recognition score for User : s11, E value : 4 is 1.0
Recognition score for User : s11, E value : 5 is 0.99375
Recognition score for User : s11, E value : 6 is 0.99375
Recognition score for User : s11, E value : 7 is 0.99375
Recognition score for User : s11, E value : 8 is 0.98125
Recognition score for User : s11, E value : 9 is 0.9875
U -------: s06
Recognition score for User : s06, E value : 1 is 0.9375
Recognition score for User : s06, E value : 2 is 0.9625
Recognition score for User : s06, E value : 3 is 0.95625
Recognition score for User : s06, E value : 4 is 0.98125
Recognition score for User : s06, E value : 5 is 0.975
Recognition score for User : s06, E value : 6 is 0.99375
Recognition score for User : s06, E value : 7 is 1.0
Recognition score for User : s06, E value : 8 is 0.9875
Recognition score for User : s06, E value : 9 is 0.9875
U -------: s08
Recognition score for User : s08, E value : 1 is 0.91875
Recognition score for User : s08, E value : 2 is 0.96875
Recognition score for User : s08, E value : 3 is 0.96875
Recognition score for User : s08, E value : 4 is 0.96875
Recognition score for User : s08, E value : 5 is 0.975
Recognition score for User : s08, E value : 6 is 0.98125
Recognition score for User : s08, E value : 7 is 0.96875
Recognition score for User : s08, E value : 8 is 0.975
Recognition score for User : s08, E value : 9 is 0.975
U -------: s09
Recognition score for User : s09, E value : 1 is 1.0
Recognition score for User : s09, E value : 2 is 1.0
Recognition score for User : s09, E value : 3 is 1.0
Recognition score for User : s09, E value : 4 is 1.0
Recognition score for User : s09, E value : 5 is 1.0
Recognition score for User : s09, E value : 6 is 1.0
Recognition score for User : s09, E value : 7 is 1.0
Recognition score for User : s09, E value : 8 is 1.0
Recognition score for User : s09, E value : 9 is 1.0
U -------: s07
Recognition score for User : s07, E value : 1 is 1.0
Recognition score for User : s07, E value : 2 is 1.0
Recognition score for User : s07, E value : 3 is 1.0
Recognition score for User : s07, E value : 4 is 1.0
Recognition score for User : s07, E value : 5 is 1.0
Recognition score for User : s07, E value : 6 is 1.0
Recognition score for User : s07, E value : 7 is 1.0
Recognition score for User : s07, E value : 8 is 1.0
Recognition score for User : s07, E value : 9 is 1.0
The total average accuracy is : 0.9906944444444444



******************************

GSS, Stylus

For E = 1, the average recognition score is 0.684375.
For E = 2, the average recognition score is 0.83125.
For E = 3, the average recognition score is 0.8765625.
For E = 4, the average recognition score is 0.894375.
For E = 5, the average recognition score is 0.8921875.
For E = 6, the average recognition score is 0.8703125.
For E = 7, the average recognition score is 0.91875.
For E = 8, the average recognition score is 0.900625.
For E = 9, the average recognition score is 0.9020833.
The total average accuracy, calculated as the average of all recognition scores, is 0.866550925925926.


U -------: user06
Recognition score for User : user06, E value : 1 is 0.69375
Recognition score for User : user06, E value : 2 is 0.79375
Recognition score for User : user06, E value : 3 is 0.875
Recognition score for User : user06, E value : 4 is 0.91875
Recognition score for User : user06, E value : 5 is 0.8875
Recognition score for User : user06, E value : 6 is 0.9125
Recognition score for User : user06, E value : 7 is 0.95
Recognition score for User : user06, E value : 8 is 0.9375
Recognition score for User : user06, E value : 9 is 0.94375
U -------: user01
Recognition score for User : user01, E value : 1 is 0.5625
Recognition score for User : user01, E value : 2 is 0.79375
Recognition score for User : user01, E value : 3 is 0.84375
Recognition score for User : user01, E value : 4 is 0.85625
Recognition score for User : user01, E value : 5 is 0.84375
Recognition score for User : user01, E value : 6 is 0.79375
Recognition score for User : user01, E value : 7 is 0.85625
Recognition score for User : user01, E value : 8 is 0.9
Recognition score for User : user01, E value : 9 is 0.8625
U -------: user02
Recognition score for User : user02, E value : 1 is 0.7125
Recognition score for User : user02, E value : 2 is 0.825
Recognition score for User : user02, E value : 3 is 0.85
Recognition score for User : user02, E value : 4 is 0.88125
Recognition score for User : user02, E value : 5 is 0.8625
Recognition score for User : user02, E value : 6 is 0.8625
Recognition score for User : user02, E value : 7 is 0.93125
Recognition score for User : user02, E value : 8 is 0.89375
Recognition score for User : user02, E value : 9 is 0.875
U -------: user05
Recognition score for User : user05, E value : 1 is 0.74375
Recognition score for User : user05, E value : 2 is 0.875
Recognition score for User : user05, E value : 3 is 0.9
Recognition score for User : user05, E value : 4 is 0.89375
Recognition score for User : user05, E value : 5 is 0.95625
Recognition score for User : user05, E value : 6 is 0.94375
Recognition score for User : user05, E value : 7 is 0.9375
Recognition score for User : user05, E value : 8 is 0.95
Recognition score for User : user05, E value : 9 is 0.95
U -------: user04
Recognition score for User : user04, E value : 1 is 0.7625
Recognition score for User : user04, E value : 2 is 0.875
Recognition score for User : user04, E value : 3 is 0.90625
Recognition score for User : user04, E value : 4 is 0.9125
Recognition score for User : user04, E value : 5 is 0.9125
Recognition score for User : user04, E value : 6 is 0.9375
Recognition score for User : user04, E value : 7 is 0.94375
Recognition score for User : user04, E value : 8 is 0.9
Recognition score for User : user04, E value : 9 is 0.94375
U -------: user03
Recognition score for User : user03, E value : 1 is 0.65
Recognition score for User : user03, E value : 2 is 0.8625
Recognition score for User : user03, E value : 3 is 0.86875
Recognition score for User : user03, E value : 4 is 0.86875
Recognition score for User : user03, E value : 5 is 0.8625
Recognition score for User : user03, E value : 6 is 0.85
Recognition score for User : user03, E value : 7 is 0.9
Recognition score for User : user03, E value : 8 is 0.86875
Recognition score for User : user03, E value : 9 is 0.9
The total average accuracy is : 0.866550925925926


********************
GSS touch screen

For E value 1: 0.8614583333333333
For E value 2: 0.9166666666666666
For E value 3: 0.9326388888888888
For E value 4: 0.9284722222222221
For E value 5: 0.9298611111111111
For E value 6: 0.9569444444444444
For E value 7: 0.9402777777777778
For E value 8: 0.9402777777777778
For E value 9: 0.9548611111111112
The total average accuracy is 0.9224537037037037.



U -------: user06
Recognition score for User : user06, E value : 1 is 0.7875
Recognition score for User : user06, E value : 2 is 0.89375
Recognition score for User : user06, E value : 3 is 0.88125
Recognition score for User : user06, E value : 4 is 0.9375
Recognition score for User : user06, E value : 5 is 0.89375
Recognition score for User : user06, E value : 6 is 0.94375
Recognition score for User : user06, E value : 7 is 0.93125
Recognition score for User : user06, E value : 8 is 0.9375
Recognition score for User : user06, E value : 9 is 0.9375
U -------: user01
Recognition score for User : user01, E value : 1 is 0.90625
Recognition score for User : user01, E value : 2 is 0.9375
Recognition score for User : user01, E value : 3 is 0.94375
Recognition score for User : user01, E value : 4 is 0.95
Recognition score for User : user01, E value : 5 is 0.95
Recognition score for User : user01, E value : 6 is 0.975
Recognition score for User : user01, E value : 7 is 0.9625
Recognition score for User : user01, E value : 8 is 0.95625
Recognition score for User : user01, E value : 9 is 0.96875
U -------: user02
Recognition score for User : user02, E value : 1 is 0.9125
Recognition score for User : user02, E value : 2 is 0.95625
Recognition score for User : user02, E value : 3 is 0.975
Recognition score for User : user02, E value : 4 is 0.9375
Recognition score for User : user02, E value : 5 is 0.95625
Recognition score for User : user02, E value : 6 is 0.9625
Recognition score for User : user02, E value : 7 is 0.9625
Recognition score for User : user02, E value : 8 is 0.98125
Recognition score for User : user02, E value : 9 is 0.96875
U -------: user05
Recognition score for User : user05, E value : 1 is 0.7
Recognition score for User : user05, E value : 2 is 0.84375
Recognition score for User : user05, E value : 3 is 0.85625
Recognition score for User : user05, E value : 4 is 0.875
Recognition score for User : user05, E value : 5 is 0.8875
Recognition score for User : user05, E value : 6 is 0.925
Recognition score for User : user05, E value : 7 is 0.88125
Recognition score for User : user05, E value : 8 is 0.9
Recognition score for User : user05, E value : 9 is 0.90625
U -------: user04
Recognition score for User : user04, E value : 1 is 0.775
Recognition score for User : user04, E value : 2 is 0.9
Recognition score for User : user04, E value : 3 is 0.89375
Recognition score for User : user04, E value : 4 is 0.9
Recognition score for User : user04, E value : 5 is 0.91875
Recognition score for User : user04, E value : 6 is 0.925
Recognition score for User : user04, E value : 7 is 0.9125
Recognition score for User : user04, E value : 8 is 0.925
Recognition score for User : user04, E value : 9 is 0.9375
U -------: user03
Recognition score for User : user03, E value : 1 is 0.91875
Recognition score for User : user03, E value : 2 is 0.95625
Recognition score for User : user03, E value : 3 is 0.98125
Recognition score for User : user03, E value : 4 is 0.95625
Recognition score for User : user03, E value : 5 is 0.94375
Recognition score for User : user03, E value : 6 is 0.9625
Recognition score for User : user03, E value : 7 is 0.975
Recognition score for User : user03, E value : 8 is 0.95625
Recognition score for User : user03, E value : 9 is 0.99375
The total average accuracy is : 0.9224537037037037





***********************
GSS, trackpad


E = 1: 0.79125
E = 2: 0.8775
E = 3: 0.8921875
E = 4: 0.90234375
E = 5: 0.9140625
E = 6: 0.89921875
E = 7: 0.909375
E = 8: 0.9015625
E = 9: 0.90859375
And the total average accuracy is 0.8793981481481481.




U -------: user2
Recognition score for User : user2, E value : 1 is 0.9125
Recognition score for User : user2, E value : 2 is 0.91875
Recognition score for User : user2, E value : 3 is 0.94375
Recognition score for User : user2, E value : 4 is 0.9625
Recognition score for User : user2, E value : 5 is 0.95
Recognition score for User : user2, E value : 6 is 0.9375
Recognition score for User : user2, E value : 7 is 0.96875
Recognition score for User : user2, E value : 8 is 0.95
Recognition score for User : user2, E value : 9 is 0.94375
U -------: user5
Recognition score for User : user5, E value : 1 is 0.69375
Recognition score for User : user5, E value : 2 is 0.85625
Recognition score for User : user5, E value : 3 is 0.7875
Recognition score for User : user5, E value : 4 is 0.925
Recognition score for User : user5, E value : 5 is 0.89375
Recognition score for User : user5, E value : 6 is 0.88125
Recognition score for User : user5, E value : 7 is 0.88125
Recognition score for User : user5, E value : 8 is 0.89375
Recognition score for User : user5, E value : 9 is 0.89375
U -------: user4
Recognition score for User : user4, E value : 1 is 0.75
Recognition score for User : user4, E value : 2 is 0.7625
Recognition score for User : user4, E value : 3 is 0.7875
Recognition score for User : user4, E value : 4 is 0.78125
Recognition score for User : user4, E value : 5 is 0.8375
Recognition score for User : user4, E value : 6 is 0.7875
Recognition score for User : user4, E value : 7 is 0.8125
Recognition score for User : user4, E value : 8 is 0.7875
Recognition score for User : user4, E value : 9 is 0.80625
U -------: user3
Recognition score for User : user3, E value : 1 is 0.75
Recognition score for User : user3, E value : 2 is 0.8625
Recognition score for User : user3, E value : 3 is 0.91875
Recognition score for User : user3, E value : 4 is 0.94375
Recognition score for User : user3, E value : 5 is 0.94375
Recognition score for User : user3, E value : 6 is 0.91875
Recognition score for User : user3, E value : 7 is 0.925
Recognition score for User : user3, E value : 8 is 0.94375
Recognition score for User : user3, E value : 9 is 0.93125
U -------: user6
Recognition score for User : user6, E value : 1 is 0.7125
Recognition score for User : user6, E value : 2 is 0.83125
Recognition score for User : user6, E value : 3 is 0.84375
Recognition score for User : user6, E value : 4 is 0.8625
Recognition score for User : user6, E value : 5 is 0.91875
Recognition score for User : user6, E value : 6 is 0.88125
Recognition score for User : user6, E value : 7 is 0.88125
Recognition score for User : user6, E value : 8 is 0.875
Recognition score for User : user6, E value : 9 is 0.89375
U -------: user1
Recognition score for User : user1, E value : 1 is 0.83125
Recognition score for User : user1, E value : 2 is 0.90625
Recognition score for User : user1, E value : 3 is 0.94375
Recognition score for User : user1, E value : 4 is 0.94375
Recognition score for User : user1, E value : 5 is 0.9125
Recognition score for User : user1, E value : 6 is 0.93125
Recognition score for User : user1, E value : 7 is 0.94375
Recognition score for User : user1, E value : 8 is 0.9625
Recognition score for User : user1, E value : 9 is 0.96875
The total average accuracy is : 0.8793981481481481
(base) subhash_vadlamani@subhash project2_sourcecode %


**********************
User logs mouse gestures gss

E=1 -> 0.7375
E=2 -> 0.85
E=3 -> 0.8834
E=4 -> 0.8916
E=5 -> 0.9104
E=6 -> 0.9041
E=7 -> 0.9177
E=8 -> 0.90834
E=9 -> 0.9229
The total average accuracy is : 0.8806712962962963

U -------: user01mouse
Recognition score for User : user01mouse, E value : 1 is 0.6875
Recognition score for User : user01mouse, E value : 2 is 0.85625
Recognition score for User : user01mouse, E value : 3 is 0.8625
Recognition score for User : user01mouse, E value : 4 is 0.90625
Recognition score for User : user01mouse, E value : 5 is 0.8625
Recognition score for User : user01mouse, E value : 6 is 0.86875
Recognition score for User : user01mouse, E value : 7 is 0.9
Recognition score for User : user01mouse, E value : 8 is 0.9
Recognition score for User : user01mouse, E value : 9 is 0.91875
U -------: user06mouse
Recognition score for User : user06mouse, E value : 1 is 0.70625
Recognition score for User : user06mouse, E value : 2 is 0.875
Recognition score for User : user06mouse, E value : 3 is 0.9
Recognition score for User : user06mouse, E value : 4 is 0.9125
Recognition score for User : user06mouse, E value : 5 is 0.9
Recognition score for User : user06mouse, E value : 6 is 0.95
Recognition score for User : user06mouse, E value : 7 is 0.9375
Recognition score for User : user06mouse, E value : 8 is 0.91875
Recognition score for User : user06mouse, E value : 9 is 0.9625
U -------: user05mouse
Recognition score for User : user05mouse, E value : 1 is 0.73125
Recognition score for User : user05mouse, E value : 2 is 0.81875
Recognition score for User : user05mouse, E value : 3 is 0.83125
Recognition score for User : user05mouse, E value : 4 is 0.88125
Recognition score for User : user05mouse, E value : 5 is 0.9
Recognition score for User : user05mouse, E value : 6 is 0.90625
Recognition score for User : user05mouse, E value : 7 is 0.9125
Recognition score for User : user05mouse, E value : 8 is 0.90625
Recognition score for User : user05mouse, E value : 9 is 0.9
U -------: user04mouse
Recognition score for User : user04mouse, E value : 1 is 0.9
Recognition score for User : user04mouse, E value : 2 is 0.93125
Recognition score for User : user04mouse, E value : 3 is 0.94375
Recognition score for User : user04mouse, E value : 4 is 0.925
Recognition score for User : user04mouse, E value : 5 is 0.95625
Recognition score for User : user04mouse, E value : 6 is 0.9375
Recognition score for User : user04mouse, E value : 7 is 0.98125
Recognition score for User : user04mouse, E value : 8 is 0.95625
Recognition score for User : user04mouse, E value : 9 is 0.9625
U -------: user03mouse
Recognition score for User : user03mouse, E value : 1 is 0.6875
Recognition score for User : user03mouse, E value : 2 is 0.81875
Recognition score for User : user03mouse, E value : 3 is 0.86875
Recognition score for User : user03mouse, E value : 4 is 0.85
Recognition score for User : user03mouse, E value : 5 is 0.9125
Recognition score for User : user03mouse, E value : 6 is 0.86875
Recognition score for User : user03mouse, E value : 7 is 0.8625
Recognition score for User : user03mouse, E value : 8 is 0.88125
Recognition score for User : user03mouse, E value : 9 is 0.90625
U -------: user02mouse
Recognition score for User : user02mouse, E value : 1 is 0.7125
Recognition score for User : user02mouse, E value : 2 is 0.8
Recognition score for User : user02mouse, E value : 3 is 0.89375
Recognition score for User : user02mouse, E value : 4 is 0.875
Recognition score for User : user02mouse, E value : 5 is 0.93125
Recognition score for User : user02mouse, E value : 6 is 0.89375
Recognition score for User : user02mouse, E value : 7 is 0.9125
Recognition score for User : user02mouse, E value : 8 is 0.8875
Recognition score for User : user02mouse, E value : 9 is 0.8875
The total average accuracy is : 0.8806712962962963


*****************************

User logs mouse protractor
E=1 -> 0.75625
E=2 ->  0.859375
E=3 -> 0.8677
E=4 -> 0.8802
E=5 -> 0.8927
E=6 -> 0.9073
E= 7 -> 0.9145
E=8 ->  0.925
E=9 -> 0.9239

The total average accuracy is : 0.8807870370370371


U -------: user01mouse
Recognition score for User : user01mouse, E value : 1 is 0.79375
Recognition score for User : user01mouse, E value : 2 is 0.8
Recognition score for User : user01mouse, E value : 3 is 0.825
Recognition score for User : user01mouse, E value : 4 is 0.8625
Recognition score for User : user01mouse, E value : 5 is 0.9
Recognition score for User : user01mouse, E value : 6 is 0.9
Recognition score for User : user01mouse, E value : 7 is 0.925
Recognition score for User : user01mouse, E value : 8 is 0.925
Recognition score for User : user01mouse, E value : 9 is 0.89375
U -------: user06mouse
Recognition score for User : user06mouse, E value : 1 is 0.775
Recognition score for User : user06mouse, E value : 2 is 0.93125
Recognition score for User : user06mouse, E value : 3 is 0.875
Recognition score for User : user06mouse, E value : 4 is 0.89375
Recognition score for User : user06mouse, E value : 5 is 0.925
Recognition score for User : user06mouse, E value : 6 is 0.93125
Recognition score for User : user06mouse, E value : 7 is 0.95
Recognition score for User : user06mouse, E value : 8 is 0.95
Recognition score for User : user06mouse, E value : 9 is 0.975
U -------: user05mouse
Recognition score for User : user05mouse, E value : 1 is 0.70625
Recognition score for User : user05mouse, E value : 2 is 0.83125
Recognition score for User : user05mouse, E value : 3 is 0.8125
Recognition score for User : user05mouse, E value : 4 is 0.8875
Recognition score for User : user05mouse, E value : 5 is 0.88125
Recognition score for User : user05mouse, E value : 6 is 0.85
Recognition score for User : user05mouse, E value : 7 is 0.86875
Recognition score for User : user05mouse, E value : 8 is 0.9125
Recognition score for User : user05mouse, E value : 9 is 0.8875
U -------: user04mouse
Recognition score for User : user04mouse, E value : 1 is 0.85625
Recognition score for User : user04mouse, E value : 2 is 0.96875
Recognition score for User : user04mouse, E value : 3 is 0.95625
Recognition score for User : user04mouse, E value : 4 is 0.95
Recognition score for User : user04mouse, E value : 5 is 0.96875
Recognition score for User : user04mouse, E value : 6 is 0.975
Recognition score for User : user04mouse, E value : 7 is 0.95
Recognition score for User : user04mouse, E value : 8 is 0.96875
Recognition score for User : user04mouse, E value : 9 is 0.95625
U -------: user03mouse
Recognition score for User : user03mouse, E value : 1 is 0.66875
Recognition score for User : user03mouse, E value : 2 is 0.81875
Recognition score for User : user03mouse, E value : 3 is 0.88125
Recognition score for User : user03mouse, E value : 4 is 0.80625
Recognition score for User : user03mouse, E value : 5 is 0.8125
Recognition score for User : user03mouse, E value : 6 is 0.91875
Recognition score for User : user03mouse, E value : 7 is 0.88125
Recognition score for User : user03mouse, E value : 8 is 0.875
Recognition score for User : user03mouse, E value : 9 is 0.90625
U -------: user02mouse
Recognition score for User : user02mouse, E value : 1 is 0.7375
Recognition score for User : user02mouse, E value : 2 is 0.80625
Recognition score for User : user02mouse, E value : 3 is 0.85625
Recognition score for User : user02mouse, E value : 4 is 0.88125
Recognition score for User : user02mouse, E value : 5 is 0.86875
Recognition score for User : user02mouse, E value : 6 is 0.86875
Recognition score for User : user02mouse, E value : 7 is 0.9125
Recognition score for User : user02mouse, E value : 8 is 0.91875
Recognition score for User : user02mouse, E value : 9 is 0.925
The total average accuracy is : 0.8807870370370371




