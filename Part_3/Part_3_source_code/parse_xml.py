"""
Authors:
Venkata Satya Sai Subhash Vadlamani(UFID : 4326-8265)
Veera Nitish Mattaparthi(UFID : 4777-4184)

"""


from ast import Set
import os
from sys import platform
import xml.etree.ElementTree as ET
from collections import OrderedDict

from recognition import Recognizer
import random
from templates import Template,Unistroke
import csv

recognizer = Recognizer()

print(platform)

cwd = os.getcwd() + '/xml_logs'
print(cwd)

dataset = []

dataDict = {}
gestureList = []
for folderName in os.listdir(cwd):
    if folderName.startswith('.DS_Store'):
        continue

    userFolder = cwd + '/' + folderName
    speedFolder = userFolder + '/medium'
    gestureList = []
    gestureMap = {}
    for xml in os.listdir(speedFolder):

        xml = speedFolder + '/' + xml
        tree = ET.parse(xml)
        root = tree.getroot()
        name = root.attrib.get('Name')[:-2]
        subject = root.attrib.get('Subject')
        speed = root.attrib.get('Speed')
        number = int(root.attrib.get('Number'))
        numpts = root.attrib.get('NumPts')
        points = []

        for i in range(0, len(root)):
            x = int(root[i].attrib.get('X'))
            y = int(root[i].attrib.get('Y'))
            points.append((x,y))
        if name in gestureMap:
            gestureMap[name][number] = points
        else:
            gestureMap[name] = {}
            gestureMap[name][number] = points

        gestureMap = OrderedDict(sorted(dict.items(gestureMap)))
    dataDict[folderName] = gestureMap


"""
    Storing the preprocessed Data in the data dictionary in the code below.
    The datastructure is a dictionary with keys as the user. This dictionary contains another dictionary
    with keys as the gesture and this dictionary contains another dictionary with keys as the number of the 
    of the sample. This finally contains the list of preprocessed points.
    
"""
for user in dataDict.keys():
    for gesture in dataDict[user].keys():
        for number in dataDict[user][gesture].keys():
            current_point_list = dataDict[user][gesture][number]
            dataDict[user][gesture][number] = recognizer.preprocess(current_point_list)



with open("gesture_logs.csv", 'w', newline='') as file:
    writer = csv.writer(file)

    """
        writing a row of the column headers
    """

    writer.writerow(["User", "GestureType", "IterationNumber", "#TrainingExamples", "TrainingSetSize", "TrainingSetContents",
                     "Candidate", "RecoResultGestureType", "Correct/Incorrect", "RecoResultScore", "RecoResultBestMatch",
                     "RecoResultNBestSorted"])

    total_correct_count = 0
    total_count = 0

    for U in (dataDict.keys()):

        """
            Printing the user number that is currently being processed
        """
        print("U -------: {}".format(U))


        for E in range(1, 10):
            recognition_score = 0

            for i in range(1, 11):

                """
                    Creating lists to store the template list and the candidate list
                """
                templatelist = []
                candidatelist = []

                training_set_contents = ""
                """
                    This string will be used to store the contents of the training set.
                    The information that is contained is the user number, the template name and the number of the sample
                """
                for gesture in dataDict[U].keys():

                    """
                        randomly storing 'E' numbers in the templatelistnumberlist list
                    """
                    templatelistnumberlist = random.sample(range(1,11), E)
                    """
                        randomly storing 1 number from the list of numbers obtained after subtracting the previously generated list of numbers
                    """
                    candidatelistnumber = random.sample(list(set([i for i in range(1,11)]) - set(templatelistnumberlist)), 1)[0]
                    for number in templatelistnumberlist:
                        """
                            Creating a template list of unistrokes
                        """
                        new_template = Unistroke(gesture, list(dataDict[U][gesture][number]), U, number)
                        templatelist.append(new_template)
                        """
                            Storing the Training set contents in the form of a string
                        """
                        training_set_contents += "{}-{}-{}:::".format(U, new_template.name, number)
                    # Candidate Gesture
                    new_candidate = Unistroke(gesture, dataDict[U][gesture][candidatelistnumber], U, candidatelistnumber)
                    candidatelist.append(new_candidate)
                recognizer = Recognizer()
                # Iterating over the template list
                for template in templatelist:
                    # print(template.name)
                    # print(template.points)

                    # Adding the template in the list of store gestures for the purpose of training.

                    recognizer.addGesture(template)
                correct_recognitions = 0


                for candidate in candidatelist:
                    """
                        Calling the recognize function for each and every candidate present in the candidatelist
                    """
                    total_count += 1
                    row = []
                    matched_gesture, score, n_best_list = recognizer.recognize_with_nbest_list(candidate.points)
                    user = U
                    gesture_type = candidate.name
                    iteration_number = i
                    number_of_training_examples = E
                    total_training_set_size = E * 16
                    current_candidate = "{}-{}-{}".format(U, gesture_type, candidate.example_count)
                    recognition_result = matched_gesture.name
                    recognition_correct = 0
                    recognition_result_score = score
                    n_best_list_string = ""
                    matched_template_string = "{}-{}-{}".format(matched_gesture.user, matched_gesture.name, matched_gesture.example_count)
                    for entry in n_best_list:
                        n_best_list_string += "{}-{}-{}-{}:::".format(entry[0], entry[1], entry[2], entry[3])


                    if matched_gesture.name == candidate.name:
                        # Incrementing the total correct count to calculate the final average accuracy of the algorithm
                        total_correct_count += 1
                        recognition_correct = 1
                        # Incrementing the correct recognitions per user per E to give that accuracy
                        correct_recognitions += 1

                    """
                        Appending the details to the row for all the details that are required.
                    """
                    row.append(user)
                    row.append(gesture_type)
                    row.append(iteration_number)
                    row.append(number_of_training_examples)
                    row.append(total_training_set_size)
                    row.append(training_set_contents)
                    row.append(current_candidate)
                    row.append(recognition_result)
                    row.append(recognition_correct)
                    row.append(recognition_result_score)
                    row.append(matched_template_string)
                    row.append(n_best_list_string)
                    writer.writerow(row)


                recognition_score += (correct_recognitions/ len(candidatelist))

            recognition_score /= 10

            print("Recognition score for User : {}, E value : {} is {}".format(U, E, recognition_score))


    total_average_accuracy = total_correct_count/total_count
    print("The total average accuracy is : {}".format(total_average_accuracy))
    row = []
    row.append("Total Average Accuracy")
    row.append(total_average_accuracy)
    writer.writerow(row)
