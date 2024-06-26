"""
Authors:
Venkata Satya Sai Subhash Vadlamani (UFID : 4326-8265)
Veera Nitish Mattaparthi (UFID : 4777-4184)

"""

import numpy as np
import math


phi = 0.5 * (-1 + np.sqrt(5))
numPoints = 64
numPointsProtractor = 16
oSensitive = False

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

class Recognizer(object):
    def __init__(self, angle_range=45., angle_step=2., square_size=250.):
        super(Recognizer, self).__init__()
        self.angle_range = angle_range
        self.angle_step = angle_step
        self.square_size = square_size
        self.templates = []
        self.templateVectors = []
        self.gestures = []
        self.gestureVectors = []

    def resample(self, points, n):
        """
        This function calculates the distance that each point should be from the next consecutive points if there are
        supposed to be 'n' points in the figure and makes sure to either reduce the number of points or increase the points
        to match the required number of points 'n' in the figure.
        """
        I = pathLength(points) / float(n-1)
        newPoints = [points[0]] # stores the resampled number of points
        D = 0.0
        i=1

        while i < len(points):
            currentPoint = points[i - 1]
            nextPoint = points[i]
            d = getDistance(currentPoint, nextPoint)
            if D + d >= I:
                distanceDifference = float((I - D) / d)
                q = [0., 0.]
                q[0] = currentPoint[0] + distanceDifference * (nextPoint[0] - currentPoint[0]) # calculates the x coordinate of new point
                q[1] = currentPoint[1] + distanceDifference * (nextPoint[1] - currentPoint[1]) # calculates the y coordinate of the new point
                newPoints.append(q)
                points.insert(i, q) # insert the point calculated during the resampling in the set of original points
                D = 0.0
            else:
                D += d
            i += 1
        if len(newPoints) == n - 1:  # code to make sure that there are always 'n' number of points in the new set of points.
            newPoints.append(points[len(points) - 1])
        return newPoints

    def vectorize(self, points, oSensitive):

        """
        This part of the code is responsible for converting the array of points to a single array
        which contains the vectors of all the points that are created according to the logic below.
        This vector is later used to calculate the optimal cosine distance
        """
        centroid = np.mean(points, 0)
        points = self.translateToPoint(points, centroid)
        indicativeAngle = np.arctan2(points[0][1], points[0][0])

        if oSensitive:
            baseOrientation = (math.pi/4) * math.floor((indicativeAngle + math.pi/8)/(math.pi/4))
            delta = baseOrientation - indicativeAngle
        else:
            delta = indicativeAngle * -1
        sum = 0
        preProcessVector = []
        for point in points:
            newX = point[0] * math.cos(delta) - point[1] * math.sin(delta)
            newY = point[1] * math.cos(delta) + point[0] * math.sin(delta)
            preProcessVector.append(newX)
            preProcessVector.append(newY)
            sum += newX * newX + newY * newY
        magnitude = math.sqrt(sum)
        vector = []
        for e in preProcessVector:
            e = e/magnitude
            vector.append(e)
        return vector

    def protractorRecognize(self, points):
        """
        This is the main recognize function that is used for the Protractor. It uses the optimal
        cosine distance to calculate the score and recognizes the figure that is drawn based on
        the value of that score.
        """

        current_points = self.resample(list(points), numPointsProtractor)
        current_points = self.rotateToZero(current_points)
        current_points = self.scaleToSquare(current_points)
        current_points = self.translateToOrigin(current_points)

        vector = self.vectorize(current_points, oSensitive)

        maxScore = 0
        match = None
        for templateVector in self.templateVectors:
            distance = self.optimalCosineDistance(templateVector.points, vector)
            score = 1 / distance
            if score > maxScore:
                maxScore = score
                match = templateVector.name
        return match, maxScore

    def protractorRecognizeWithNBestList(self, points):
        """
        This function is responsible for finding the best match for the given set of points that are drawn
        and also generates the NBestList which is displayed in the log files.
        """
        vector = self.vectorize(points, oSensitive)
        n_best_list = []
        min_distance = np.inf
        selected_gestureVector = None

        for gestureVector in self.gestureVectors:
            distance = self.optimalCosineDistance(gestureVector.vector, vector)
            current_score = 1 / distance
            gestureVector_user = gestureVector.user
            gestureVector_name = gestureVector.name
            gestureVector_example_count = gestureVector.example_count
            element_tuple = (gestureVector_user, gestureVector_name, gestureVector_example_count, current_score)
            n_best_list.append(element_tuple)
            if distance < min_distance:
                min_distance = distance
                selected_gestureVector = gestureVector
        final_score = 1 / min_distance
        sorted_n_best_list = sorted(n_best_list, key=lambda x:x[3], reverse=True)
        if len(sorted_n_best_list) > 50:
            sorted_n_best_list = sorted_n_best_list[:50]
        return selected_gestureVector, final_score, sorted_n_best_list


    def optimalCosineDistance(self, vector1, vector2):
        """
        This function calculates the optimal cosine distance between the points that are represented
        by the two vectors.
        """

        a = 0
        b = 0
        for i in range(0, len(vector1), 2):
            a += (vector1[i] * vector2[i]) + (vector1[i+1] * vector2[i+1])
            b += (vector1[i] * vector2[i+1]) - (vector1[i+1] * vector2[i])
        angle = np.arctan(b/a)
        return np.arccos(a * np.cos(angle) + b * np.sin(angle))

    def translateToPoint(self, points, translationPoint):
        """
        This function is responsible for translating the given set of points about another point.
        """
        centroid = np.mean(points, 0)
        new_points = []
        for point in points:
            q = [0.0, 0.0]
            q[0] = point[0] + translationPoint[0] - centroid[0]
            q[1] = point[1] + translationPoint[1] - centroid[1]
            new_points.append(q)
        return new_points


    def addTemplateVector(self, template):
        # temp_template = template
        """
        This funciton is responsible for adding the template vector to
        the list that stores all the templates.
        Here, after all the preprocessing, instead of just storing the
        raw set of points, we store the vector representation of those points.
        """
        template.points = self.resample(template.points, numPointsProtractor)
        template.points = self.rotateToZero(template.points)
        template.points = self.scaleToSquare(template.points)
        template.points = self.translateToOrigin(template.points)

        template.points = self.vectorize(template.points, oSensitive)
        self.templateVectors.append(template)

    def addTemplate(self, template):
        """
        This code is responsible for adding each and every one of the 16 templates to the system after doing the prerpocessing steps.
        The preprocessing steps are :
            i) Resampling
            ii) Rotation of the template to make the angle between it's first point and the centroid zero
            iii) Scaling the template to the reference square
            iv) Translating the template on the coordinates such that the centroid becomes (0,0)
        """
        # temp_template = template
        template.points = self.resample(template.points, numPoints)
        template.points = self.rotateToZero(template.points)
        template.points = self.scaleToSquare(template.points)
        template.points = self.translateToOrigin(template.points)
        self.templates.append(template)

        # might have to change this
        # temp_template.points = self.vectorize(temp_template.points, oSensitive)
        # self.templateVectors.append(temp_template)

    def addGesture(self, gesture):
        """
            This code is responsible for adding the gesture to the list of stored gestures for the purpose of
            training. Preprocessing is not required in this function as the gestures that are passed to this function
            have already undergone through the process of preprocessing.
        """
        # gesture.points = self.resample(gesture.points, numPoints)
        # gesture.points = self.rotateToZero(gesture.points)
        # template.points = self.scaleToSquare(template.points)
        # template.points = self.translateToOrigin(template.points)
        self.gestures.append(gesture)

    def addGestureVector(self, gesture):
        self.gestureVectors.append(gesture)



    def arctanAngle(self, points):
        """
        Calculates the angle by which we have to rotate the figure to make the angle between it's first point and the centroid
        zero.
        """
        centroid = np.mean(points, 0)
        rotationAngle = np.arctan2(centroid[1] - points[0][1], centroid[0] - points[0][0])
        return rotationAngle

    def rotateToZero(self, points):
        """
        Calls the function which is responsible for calculating the angle by which we have to rotate to make the angle
        between the first point and the centroid zero and then calls the function that returns new set of points after the rotation
        """
        rotationAngle = self.arctanAngle(points)
        newPoints = rotate2D(points, 0, -rotationAngle)
        return newPoints

    def rotateBy(self, points, angle):
        """
        Roattes the set of points by the given angle and returns the new set of points
        """
        centroid = np.mean(points, 0)
        newPoints = np.zeros((1, 2))
        for point in points:
            q = np.array([0., 0.])
            q[0] = (point[0] - centroid[0]) * np.cos(angle) - (point[1] - centroid[1]) * np.sin(angle) + centroid[0]
            q[1] = (point[0] - centroid[0]) * np.sin(angle) + (point[1] - centroid[1]) * np.cos(angle) + centroid[1]
            newPoints = np.append(newPoints, [q], 0)
        return newPoints[1:]

    def scaleToSquare(self, points):
        """
        Non-uniform scaling of points is done by calculating the minimum and maximum y coordinates and the size of the
        reference square.
        """
        max_x, max_y = np.max(points, 0)
        min_x, min_y = np.min(points, 0)
        b_width = max_x - min_x
        b_height = max_y - min_y
        newPoints = np.zeros((1, 2))
        for point in points:
            q = np.array([0., 0.])
            q[0] = point[0] * (self.square_size / b_width)
            q[1] = point[1] * (self.square_size / b_height)
            newPoints = np.append(newPoints, [q], 0)
        return newPoints[1:]


    def translateToOrigin(self, points):
        """
        Considers the centroid as origin and translates the set of points by considering the centroid as origin
        """
        centroid = np.mean(points, 0)
        newPoints = np.zeros((1, 2))
        for point in points:
            q = np.array([0., 0.])
            q[0] = point[0] - centroid[0]
            q[1] = point[1] - centroid[1]
            newPoints = np.append(newPoints, [q], 0)
        return newPoints[1:]

    def preprocess(self, points):

        """
        This function is responsible for preprocessing the points which represent a gesture.
        """

        current_points = self.resample(list(points), numPoints)
        current_points = self.rotateToZero(current_points)
        current_points = self.scaleToSquare(current_points)
        current_points = self.translateToOrigin(current_points)

        return current_points

    def recognize_with_nbest_list(self, points):

        """

            This function does not contain the preprocessing of the points as this is called with all
            the points already preprocessed.

            This function performs the recognition and outputs the n-best list of length 50 or N, which ever is less
        """
        b = np.inf
        selected_gesture = None
        n_best_list = []
        # print(self.gestures)
        for gesture in self.gestures:
            d = self.distanceAtBestAngle(points, gesture.points, -self.angle_range, self.angle_range,
                                         self.angle_step)
            current_score = 1 - d / (0.5 * np.sqrt(self.square_size ** 2 + self.square_size ** 2))
            gesture_user = gesture.user
            gesture_name = gesture.name
            gesture_example_count = gesture.example_count
            element_tuple = (gesture_user, gesture_name, gesture_example_count, current_score)
            n_best_list.append(element_tuple)
            if d < b:
                b = d
                selected_gesture = gesture
        final_score = 1 - b / (0.5 * np.sqrt(self.square_size ** 2 + self.square_size ** 2))
        # Sorting the N best list based on the score
        sorted_n_best_list = sorted(n_best_list, key=lambda x:x[3], reverse=True)
        if len(sorted_n_best_list) > 50:
            sorted_n_best_list = sorted_n_best_list[:50]
        # a score that is in range of 0 to 1, the closer it is to 1 the better the match is.
        return selected_gesture, final_score, sorted_n_best_list



    def recognize(self, points):

        """
        The function that performs the recognition process. It first preprocesses the given input and compares it with
        all the templates and stores the best templates
        """

        current_points = self.resample(list(points), numPoints)
        current_points = self.rotateToZero(current_points)
        current_points = self.scaleToSquare(current_points)
        current_points = self.translateToOrigin(current_points)

        b = np.inf
        selected_template = None
        for template in self.templates:
            # Calculates the distance at the best angle of rotation of the set of input points within the given range and angle step

            d = self.distanceAtBestAngle(current_points, template.points, -self.angle_range, self.angle_range, self.angle_step)
            if d < b:
                b = d
                selected_template = template
        score = 1 - b / (0.5 * np.sqrt(self.square_size ** 2 + self.square_size ** 2))
        # a score that is in range of 0 to 1, the closer it is to 1 the better the match is.
        return selected_template, score

    def distanceAtBestAngle(self, points, template, angle_a, angle_b, angle_step):
        """
        Search of the least distance between the set of input points and the template
        using the golden ratio scheme.
        """
        angle_1 = phi * angle_a + (1 - phi) * angle_b
        distance_1 = self.distanceAtCurrentAngle(points, template, angle_1)
        angle_2 = (1 - phi) * angle_a + phi * angle_b
        distance_2 = self.distanceAtCurrentAngle(points, template, angle_2)

        while np.abs(angle_b - angle_a) > angle_step:
            if distance_1 < distance_2:
                angle_b = angle_2
                angle_2 = angle_1
                distance_2 = distance_1
                angle_1 = phi * angle_a + (1 - phi) * angle_b
                distance_1 = self.distanceAtCurrentAngle(points, template, angle_1)
            else:
                angle_a = angle_1
                angle_1 = angle_2
                distance_1 = distance_2
                angle_2 = (1 - phi) * angle_a + phi * angle_b
                distance_2 = self.distanceAtCurrentAngle(points, template, angle_2)
        return min(distance_1, distance_2)

    def distanceAtCurrentAngle(self, points, template, angle):
        """
        Calculates the distance between the new set of point after rotating it by a certain 'angle' and the template
        """
        newPoints = self.rotateBy(points, angle)
        d = pathDistance(newPoints, template)
        return d



def rotate2D(pts, cnt, angle= np.pi / 4):
    # Rotates the set of points about the 'angle' and returns new set of points.
    return np.dot(np.array(pts) - cnt, np.array([[np.cos(angle), np.sin(angle)], [-np.sin(angle), np.cos(angle)]])) + cnt


def getDistance(point1, point2):
    """
    Method to get the Euclidian distance between two points.
    """
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]

    distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def pathLength(points):
    """
    Method to get the length of the path.
    """
    d = 0.0
    for i in range(1, len(points)):
        d += getDistance(points[i-1], points[i])
    return d


def pathDistance(path1, path2):
    """
    Getting the distances between the two sets of points.
    """
    if len(path1) != len(path2):
        raise Exception("Path lengths have to be the same to do the comparision")
    d = 0

    for i in range(0, len(path1)):
        d = d + getDistance(path1[i], path2[i])
    return d / len(path1)
