class Vertex():

    def __init__(self, coord, terrain, alt):
        self.coord = coord
        self.terrain = terrain # String with the type of the terrain
        self.altitude = alt

    def printV(self):
        print('Le point de coord: ', self.coord)
        print('a un terrain de type: ', self.terrain)
        print('et une altitude: ', self.altitude)
