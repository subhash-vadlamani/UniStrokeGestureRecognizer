Authors:

Venkta Satya Sai Subhash Vadlamani(UFID : 4326-8265)
Veera Nitish Mattaparthi (UFID : 4777-4184)

a (Run an Offline Recognition Test):
We have successfully read in the XML logs of all the gestures of all the users using the xml.etree.ElementTree
class. We are storing all the points of the gestures as a form of dictionary of a dictionary of a dictionary
where they keys are the user, the gesture name and the number of the gesture respectively. This is the most efficient
way to store the points as it will be very easy to access the points later on. The code for this is in the lines
25 to 67 in the parse_xml.py file.

After this, we connect to the recognizer.

In this step, using the stored points of the gestures, we connect to the previously implemented recognition algorithm.
We preprocess the points of all the gestures before using them as templates and candidates. The code for the preprocessing
is in the lines 77 to 81 in parse_xml.py file.

Now, we loop over the dataset.

Here, we are looping over each and every user for E values from 1 to 9 and we are doing this 10 times. We are also buidling
a stratified collection of the training data and the testing data. The code for this is from the lines 99 to 209 in parse_xml.py
The loops specifically are in the lines 99, 107, 123, 158.


The call for the recognition algorithm is made for each and every candidate and it is done in the line 164 of the parse_xml.py file


b(output the result):
We are calculating the accuracy per user per E for all the 10 iterations and outputting that. We are also calculating the
total average accuracy(total_correct_recognitions/total_number_of_calls) and we are outputting the the results in a log file.
The total final accuracy that we got is 0.8803(88.03 %). This output is comparitively less than the output that was obtained
during the part 3 of this project. This is because of the variability of the gestures drawn by the 6 users that were involved
in our study. The variability of the samples can be seen through the heatmaps of the gestures that are generated by the Ghost software.
Because of this, higher values of E generally tend to give higher accuracy. The code for outputting the result is between the lines 158 to 212 in parse_xml.py
file. Here, we are first calculating all the values that have to be inputed in the row and then we are creating the
csv row.

The final gesture logs are generated as a csv file named 'gesture_logs_part5.csv'.

Below is the output on the terminal that we got.

U -------: user2
Recognition score for User : user2, E value : 1 is 0.86875
Recognition score for User : user2, E value : 2 is 0.94375
Recognition score for User : user2, E value : 3 is 0.94375
Recognition score for User : user2, E value : 4 is 0.94375
Recognition score for User : user2, E value : 5 is 0.96875
Recognition score for User : user2, E value : 6 is 0.94375
Recognition score for User : user2, E value : 7 is 0.95625
Recognition score for User : user2, E value : 8 is 0.96875
Recognition score for User : user2, E value : 9 is 0.96875
U -------: user5
Recognition score for User : user5, E value : 1 is 0.7375
Recognition score for User : user5, E value : 2 is 0.7625
Recognition score for User : user5, E value : 3 is 0.8375
Recognition score for User : user5, E value : 4 is 0.825
Recognition score for User : user5, E value : 5 is 0.85625
Recognition score for User : user5, E value : 6 is 0.84375
Recognition score for User : user5, E value : 7 is 0.9125
Recognition score for User : user5, E value : 8 is 0.88125
Recognition score for User : user5, E value : 9 is 0.9125
U -------: user4
Recognition score for User : user4, E value : 1 is 0.7
Recognition score for User : user4, E value : 2 is 0.7875
Recognition score for User : user4, E value : 3 is 0.825
Recognition score for User : user4, E value : 4 is 0.78125
Recognition score for User : user4, E value : 5 is 0.81875
Recognition score for User : user4, E value : 6 is 0.78125
Recognition score for User : user4, E value : 7 is 0.79375
Recognition score for User : user4, E value : 8 is 0.775
Recognition score for User : user4, E value : 9 is 0.79375
U -------: user3
Recognition score for User : user3, E value : 1 is 0.8
Recognition score for User : user3, E value : 2 is 0.9125
Recognition score for User : user3, E value : 3 is 0.94375
Recognition score for User : user3, E value : 4 is 0.9125
Recognition score for User : user3, E value : 5 is 0.89375
Recognition score for User : user3, E value : 6 is 0.94375
Recognition score for User : user3, E value : 7 is 0.93125
Recognition score for User : user3, E value : 8 is 0.93125
Recognition score for User : user3, E value : 9 is 0.96875
U -------: user6
Recognition score for User : user6, E value : 1 is 0.63125
Recognition score for User : user6, E value : 2 is 0.8125
Recognition score for User : user6, E value : 3 is 0.83125
Recognition score for User : user6, E value : 4 is 0.8875
Recognition score for User : user6, E value : 5 is 0.9375
Recognition score for User : user6, E value : 6 is 0.89375
Recognition score for User : user6, E value : 7 is 0.91875
Recognition score for User : user6, E value : 8 is 0.8875
Recognition score for User : user6, E value : 9 is 0.90625
U -------: user1
Recognition score for User : user1, E value : 1 is 0.88125
Recognition score for User : user1, E value : 2 is 0.93125
Recognition score for User : user1, E value : 3 is 0.93125
Recognition score for User : user1, E value : 4 is 0.95625
Recognition score for User : user1, E value : 5 is 0.925
Recognition score for User : user1, E value : 6 is 0.96875
Recognition score for User : user1, E value : 7 is 0.9375
Recognition score for User : user1, E value : 8 is 0.95625
Recognition score for User : user1, E value : 9 is 0.975
The total average accuracy is : 0.8803240740740741

c(Analyze Dataset using GHoST)

We have successfully downloaded the GHoST windows executable and analyzed the gestrues of each and every user.
In total, we analyzed 960 gestures. We made sure that our XML files had the 'X' and 'Y' coordinates along with 'T'.
We selected our dataset from the 'Gesture dataset' menu and confirmed the Heatmap settings. After that we computed the heatmap image
and the feature data from the export menu and have included their submissions along with our code. The names of the files are
'heatmap_data.bmp' and 'feature_data.csv'.

d(Extract User Articulation Insights)
From the heatmap generated, Some of the things that can be seen are
i) There is a lot of user articulation variability near the head of the pigtail gesture. This is because different users
have different way of drawing the head of the pigtail. Some users drew bigger heads compared to other users and the distance
of the head from the tails was also different for different users.

ii) There is also a lot of user articulation variability at the end points of the star gesture because each user has a different way
of drawing a start at the edges(angle between two lines at the edge of a start is different for different users)

iii) There is a lot of similarity in user articulation at the middle of the left square bracket gesture and the check mark gesture.
This is most probably because these points are formed just by drawing a straight line which is similar for different users.