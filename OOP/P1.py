class Line():

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        (x1,y1) = self.coor1
        (x2,y2) = self.coor2
        dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
        print("Distance = {}".format(dist))

    def slope(self):
        (x1,y1) = self.coor1
        (x2,y2) = self.coor2
        slope = (y2-y1)/(x2-x1)
        print("slope = {}".format(slope))


    
line1 = Line((0,0),(1,1))
line1.distance()
line1.slope()