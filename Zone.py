from Vertex import *
class Zone():

    def __init__(self, vertexCentre: Vertex, distance, typeZone, areaDicoType):
        self.centre = vertexCentre
        self.distance = distance
        # type of zone: ville, .... for a type we have several option example: 'ville': {0: 'dimgray', 1: 'gray', ...}
        self.typeZone=typeZone
        self.areaDicoType = areaDicoType
        # at initialization we have only the center
        # list (vertex, current_distance), at initialization current_distance = 0 because center of zone
        self.listVertexInTheZone = [(vertexCentre, 0)]

    def printV(self):
        print('coord central zone: ', self.centre)
        print('distance: ', self.distance)
        print('type (area): ', self.areaName)
