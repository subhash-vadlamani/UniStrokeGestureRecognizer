import numpy as np


phi = 0.5 * (-1 + np.sqrt(5))
numPoints = 64

class Recognizer(object):
    def __init__(self, angle_range=45., angle_step=2., square_size=250.):
        super(Recognizer, self).__init__()
        self.angle_range = angle_range
        self.angle_step = angle_step
        self.square_size = square_size
        self.templates = []
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


    def addTemplate(self, template):
        """
        This code is responsible for adding each and every one of the 16 templates to the system after doing the prerpocessing steps.
        The preprocessing steps are :
            i) Resampling
            ii) Rotation of the template to make the angle between it's first point and the centroid zero
            iii) Scaling the template to the reference square
            iv) Translating the template on the coordinates such that the centroid becomes (0,0)
        """
        template.points = self.resample(template.points, numPoints)
        template.points = self.rotateToZero(template.points)
        template.points = self.scaleToSquare(template.points)
        template.points = self.translateToOrigin(template.points)
        self.templates.append(template)

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
