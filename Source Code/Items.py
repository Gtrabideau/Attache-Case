# Each class holds the name and 2d array of the item in question, with 1 being where the item is and 0 being empty space
class Phone:
    def __init__(self):
        self.name = "Phone"
        self.rows, self.cols = (10, 2)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(10):
            self.arr[i][1] = 1
        for i in range(4, 10):
            self.arr[i][0] = 1


class Papers:
    def __init__(self):
        self.name = "Papers"
        self.rows, self.cols = (5, 4)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class VHS:
    def __init__(self):
        self.name = "VHS"
        self.rows, self.cols = (7, 4)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class Camera:
    def __init__(self):
        self.name = "Camera"
        self.rows, self.cols = (2, 4)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class Calculator:
    def __init__(self):
        self.name = "Calculator"
        self.rows, self.cols = (3, 4)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class Cassette:
    def __init__(self):
        self.name = "Cassette"
        self.rows, self.cols = (3, 4)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class Pen:
    def __init__(self):
        self.name = "Pen"
        self.rows, self.cols = (4, 1)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class SmokingPipe:
    def __init__(self):
        self.name = "Smoking Pipe"
        self.rows, self.cols = (3, 4)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(1, 3):
            for j in range(2):
                self.arr[i][j] = 1
        self.arr[0][2] = 1
        self.arr[0][3] = 1
        self.arr[1][2] = 1


class Keys:
    def __init__(self):
        self.name = "Keys"
        self.rows, self.cols = (5, 4)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(4):
            for j in range(4):
                self.arr[i][j] = 1
        self.arr[4][0] = 1
        self.arr[4][1] = 1


class Notebook:
    def __init__(self):
        self.name = "Notebook"
        self.rows, self.cols = (5, 6)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class MultiTool:
    def __init__(self):
        self.name = "MultiTool"
        self.rows, self.cols = (2, 4)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class Cuffs:
    def __init__(self):
        self.name = "Cuffs"
        self.rows, self.cols = (3, 5)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class Vial:
    def __init__(self):
        self.name = "Vial"
        self.rows, self.cols = (3, 1)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class Watch:
    def __init__(self):
        self.name = "Watch"
        self.rows, self.cols = (4, 3)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(1, 4):
            for j in range(self.cols):
                self.arr[i][j] = 1
        self.arr[0][1] = 1


class MagnifyingGlass:
    def __init__(self):
        self.name = "Magnifying Glass"
        self.rows, self.cols = (5, 3)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(2):
            for j in range(3):
                self.arr[i][j] = 1
        for i in range(2, 5):
            self.arr[i][1] = 1


class ScrewdriverA:
    def __init__(self):
        self.name = "ScrewdriverA"
        self.rows, self.cols = (7, 1)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class ScrewdriverB:
    def __init__(self):
        self.name = "ScrewdriverB"
        self.rows, self.cols = (4, 1)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class ScrewdriverC:
    def __init__(self):
        self.name = "ScrewdriverC"
        self.rows, self.cols = (3, 1)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class AllenKeys:
    def __init__(self):
        self.name = "AllenKeys"
        self.rows, self.cols = (6, 3)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(2, 6):
            self.arr[i][2] = 0


class Caliper:
    def __init__(self):
        self.name = "Caliper"
        self.rows, self.cols = (7, 2)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(1, 7):
            if i != 3:
                self.arr[i][0] = 0


class TWrench:
    def __init__(self):
        self.name = "T-Wrench"
        self.rows, self.cols = (6, 5)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(self.cols):
            self.arr[0][i] = 1
        for j in range(self.rows):
            self.arr[j][2] = 1


class Hammer:
    def __init__(self):
        self.name = "Hammer"
        self.rows, self.cols = (7, 3)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(1, 7):
            self.arr[i][0] = 0
        for j in range(2, 7):
            self.arr[j][2] = 0


class Wrench:
    def __init__(self):
        self.name = "Wrench"
        self.rows, self.cols = (7, 2)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class Pliers:
    def __init__(self):
        self.name = "Pliers"
        self.rows, self.cols = (6, 3)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(3, 6):
            for j in range(self.cols):
                self.arr[i][j] = 1
        for i in range(3):
            self.arr[i][1] = 1


class Mallet:
    def __init__(self):
        self.name = "Mallet"
        self.rows, self.cols = (8, 3)
        self.arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(6, 8):
            for j in range(self.cols):
                self.arr[i][j] = 1
        for i in range(6):
            self.arr[i][1] = 1


class Pencil:
    def __init__(self):
        self.name = "Pencil"
        self.rows, self.cols = (1, 3)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]


class Screws:
    def __init__(self):
        self.name = "Screws"
        self.rows, self.cols = (2, 1)
        self.arr = [[1 for i in range(self.cols)] for j in range(self.rows)]
