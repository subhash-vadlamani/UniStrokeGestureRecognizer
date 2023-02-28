Authors:

Venkta Satya Sai Subhash Vadlamani(UFID : 4326-8265)
Veera Nitish Mattaparthi (UFID : 4777-4184)

a (Read in the Dataset):
We have successfully read in the XML logs of all the gestures of all the users using the xml.etree.ElementTree
class. We are storing all the points of the gestures as a form of dictionary of a dictionary of a dictionary
where they keys are the user, the gesture name and the number of the gesture respectively. This is the most efficient
way to store the points as it will be very easy to access the points later on. The code for this is in the lines
25 to 63 in the parse_xml.py file

b (connect to recognizer):
In this steps using the stored points of the gestures, we connect to the previously implemented recognition algorithm.
We preprocess the points of all the gestures before using them as templates and candidates. The code for the preprocessing
is in the lines 73 to 77 in parse_xml.py file.

The call for the recognition algorithm is made for each and every candidate and it is done in the line 160 of the parse_xml.py file

c(Loop over the dataset):

Here, we are looping over each and every user for E values from 1 to 9 and we are doing this 10 times. We are also buidling
a stratified collection of the training data and the testing data. The code for this is from the lines 95 to 205 in parse_xml.py
The loops specifically are in the lines 95, 103, 119, 154.

d(output the result):
We are calculating the accuracy per user per E for all the 10 iterations and outputting that. We are also calculating the
total average accuracy(total_correct_recognitions/total_number_of_calls) and we are outputting the the results in a log file.
The total final accuracy that we got is 0.9905(99.05 %). In most cases, the accuracy peaked at around E=3. This shows that there
is no considerable advantage of going beyond E=3. The code for outputting the result is between the lines 153 to 208 in parse_xml.py
file. Here, we are first calculating all the values that have to be inputed in the row and then we are creating the
csv row.


Below is the output on the terminal that we got.

U -------: s05
Recognition score for User : s05, E value : 1 is 1.0
Recognition score for User : s05, E value : 2 is 1.0
Recognition score for User : s05, E value : 3 is 1.0
Recognition score for User : s05, E value : 4 is 1.0
Recognition score for User : s05, E value : 5 is 1.0
Recognition score for User : s05, E value : 6 is 1.0
Recognition score for User : s05, E value : 7 is 1.0
Recognition score for User : s05, E value : 8 is 1.0
Recognition score for User : s05, E value : 9 is 1.0
U -------: s02
Recognition score for User : s02, E value : 1 is 0.99375
Recognition score for User : s02, E value : 2 is 1.0
Recognition score for User : s02, E value : 3 is 0.99375
Recognition score for User : s02, E value : 4 is 1.0
Recognition score for User : s02, E value : 5 is 1.0
Recognition score for User : s02, E value : 6 is 1.0
Recognition score for User : s02, E value : 7 is 1.0
Recognition score for User : s02, E value : 8 is 1.0
Recognition score for User : s02, E value : 9 is 1.0
U -------: s03
Recognition score for User : s03, E value : 1 is 0.9875
Recognition score for User : s03, E value : 2 is 0.9875
Recognition score for User : s03, E value : 3 is 0.99375
Recognition score for User : s03, E value : 4 is 1.0
Recognition score for User : s03, E value : 5 is 1.0
Recognition score for User : s03, E value : 6 is 1.0
Recognition score for User : s03, E value : 7 is 1.0
Recognition score for User : s03, E value : 8 is 1.0
Recognition score for User : s03, E value : 9 is 1.0
U -------: s04
Recognition score for User : s04, E value : 1 is 0.98125
Recognition score for User : s04, E value : 2 is 0.98125
Recognition score for User : s04, E value : 3 is 1.0
Recognition score for User : s04, E value : 4 is 0.99375
Recognition score for User : s04, E value : 5 is 0.9875
Recognition score for User : s04, E value : 6 is 1.0
Recognition score for User : s04, E value : 7 is 0.99375
Recognition score for User : s04, E value : 8 is 0.99375
Recognition score for User : s04, E value : 9 is 1.0
U -------: s10
Recognition score for User : s10, E value : 1 is 1.0
Recognition score for User : s10, E value : 2 is 1.0
Recognition score for User : s10, E value : 3 is 0.99375
Recognition score for User : s10, E value : 4 is 1.0
Recognition score for User : s10, E value : 5 is 0.99375
Recognition score for User : s10, E value : 6 is 1.0
Recognition score for User : s10, E value : 7 is 1.0
Recognition score for User : s10, E value : 8 is 1.0
Recognition score for User : s10, E value : 9 is 1.0
U -------: s11
Recognition score for User : s11, E value : 1 is 0.95625
Recognition score for User : s11, E value : 2 is 0.99375
Recognition score for User : s11, E value : 3 is 0.9875
Recognition score for User : s11, E value : 4 is 0.9875
Recognition score for User : s11, E value : 5 is 1.0
Recognition score for User : s11, E value : 6 is 0.9875
Recognition score for User : s11, E value : 7 is 1.0
Recognition score for User : s11, E value : 8 is 0.9875
Recognition score for User : s11, E value : 9 is 1.0
U -------: s06
Recognition score for User : s06, E value : 1 is 0.9375
Recognition score for User : s06, E value : 2 is 0.975
Recognition score for User : s06, E value : 3 is 0.98125
Recognition score for User : s06, E value : 4 is 0.975
Recognition score for User : s06, E value : 5 is 0.98125
Recognition score for User : s06, E value : 6 is 0.96875
Recognition score for User : s06, E value : 7 is 0.96875
Recognition score for User : s06, E value : 8 is 0.99375
Recognition score for User : s06, E value : 9 is 0.98125
U -------: s08
Recognition score for User : s08, E value : 1 is 0.8875
Recognition score for User : s08, E value : 2 is 0.95
Recognition score for User : s08, E value : 3 is 0.95
Recognition score for User : s08, E value : 4 is 0.95625
Recognition score for User : s08, E value : 5 is 0.96875
Recognition score for User : s08, E value : 6 is 0.975
Recognition score for User : s08, E value : 7 is 0.975
Recognition score for User : s08, E value : 8 is 0.96875
Recognition score for User : s08, E value : 9 is 0.9875
U -------: s09
Recognition score for User : s09, E value : 1 is 0.99375
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
The total average accuracy is : 0.9905555555555555

