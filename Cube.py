import numpy as np

class Center_block:

    def __init__(self, colour):
        self.colour = colour

    def __str__(self):
        return self.colour + " "

class Corner_block:

    def __init__(self, colour, orientation):
        self.colour = colour
        self.orientation = orientation

    def get_colour(self, pos):
        return self.colour[(pos + self.orientation) % 3] + " "

    def __str__(self):
        return self.colour + " "

class Edge_block:

    def __init__(self, colour, orientation):
        self.colour = colour
        self.orientation = orientation

    def get_colour(self, pos):
        return self.colour[(pos + self.orientation) % 2] + " "

    def __str__(self):
        return self.colour + " "

class Cube:

    def __init__(self):
        self.cube = {( 0, 0, 1) : Center_block('w'),
                     ( 0, 0,-1) : Center_block('y'),
                     ( 1, 0, 0) : Center_block('b'),
                     (-1, 0, 0) : Center_block('g'),
                     ( 0, 1, 0) : Center_block('o'),
                     ( 0,-1, 0) : Center_block('r'),
                     (-1,-1, 1) : Corner_block('wrg', 0),
                     ( 1,-1, 1) : Corner_block('wbr', 0),
                     ( 1, 1, 1) : Corner_block('wob', 0),
                     (-1, 1, 1) : Corner_block('wgo', 0),
                     (-1,-1,-1) : Corner_block('ygr', 0),
                     ( 1,-1,-1) : Corner_block('yrb', 0),
                     ( 1, 1,-1) : Corner_block('ybo', 0),
                     (-1, 1,-1) : Corner_block('yog', 0),
                     ( 0,-1, 1) : Edge_block('wr', 0),
                     ( 1, 0, 1) : Edge_block('wb', 0),
                     ( 0, 1, 1) : Edge_block('wo', 0),
                     (-1, 0, 1) : Edge_block('wg', 0),
                     (-1,-1, 0) : Edge_block('rg', 0),
                     ( 1,-1, 0) : Edge_block('rb', 0),
                     ( 1, 1, 0) : Edge_block('ob', 0),
                     (-1, 1, 0) : Edge_block('og', 0),
                     ( 0,-1,-1) : Edge_block('yr', 0),
                     ( 1, 0,-1) : Edge_block('yb', 0),
                     ( 0, 1,-1) : Edge_block('yo', 0),
                     (-1, 0,-1) : Edge_block('yg', 0)
        }

    def r(self):
        r_matrix = [[ 0, 0,-1],
                    [ 0, 1, 0],
                    [ 1, 0, 0]]
        r_face = {}
        for x in list(self.cube.keys()):
            if x[1] == 1:
                item = self.cube.pop(x)

                if x == (0, 1, 0):
                    pass

                elif x[0] * x[2] == 0:
                    item.orientation += 1

                elif x[0] == x[2]:
                    item.orientation -= 1

                else:
                    item.orientation += 1

                r_face[x] = item


        for x in list(r_face.keys()):
            self.cube[tuple(np.dot(r_matrix, x))] = r_face.pop(x)

    def l(self):
        l_matrix = [[ 0, 0, 1],
                    [ 0, 1, 0],
                    [-1, 0, 0]]
        l_face = {}
        for x in list(self.cube.keys()):
            if x[1] == -1:
                item = self.cube.pop(x)

                if x == (0, -1, 0):
                    pass

                elif x[0] * x[2] == 0:
                    item.orientation += 1

                elif x[0] == x[2]:
                    item.orientation += 1

                else:
                    item.orientation -= 1

                l_face[x] = item


        for x in list(l_face.keys()):
            self.cube[tuple(np.dot(l_matrix, x))] = l_face.pop(x)

    def u(self):
        u_matrix = [[ 0, 1, 0],
                    [-1, 0, 0],
                    [ 0, 0, 1]]
        u_face = {}
        for x in list(self.cube.keys()):
            if x[2] == 1:
                u_face[x] = self.cube.pop(x)

        for x in list(u_face.keys()):
            self.cube[tuple(np.dot(u_matrix, x))] = u_face.pop(x)

    def d(self):
        d_matrix = [[ 0,-1, 0],
                    [ 1, 0, 0],
                    [ 0, 0, 1]]
        d_face = {}
        for x in list(self.cube.keys()):
            if x[2] == -1:
                d_face[x] = self.cube.pop(x)

        for x in list(d_face.keys()):
            self.cube[tuple(np.dot(d_matrix, x))] = d_face.pop(x)

    def f(self):
        f_matrix = [[ 1, 0, 0],
                    [ 0, 0, 1],
                    [ 0,-1, 0]]
        f_face = {}
        for x in list(self.cube.keys()):
            if x[0] == 1:
                item = self.cube.pop(x)

                if x[1] * x[2] == 0:
                    pass

                elif x[1] == x[2]:
                    item.orientation += 1

                else:
                    item.orientation -= 1

                f_face[x] = item

        for x in list(f_face.keys()):
            self.cube[tuple(np.dot(f_matrix, x))] = f_face.pop(x)

    def b(self):
        b_matrix = [[ 1, 0, 0],
                    [ 0, 0,-1],
                    [ 0, 1, 0]]
        b_face = {}
        for x in list(self.cube.keys()):
            if x[0] == -1:
                item = self.cube.pop(x)

                if x[1] * x[2] == 0:
                    pass

                elif x[1] == x[2]:
                    item.orientation -= 1

                else:
                    item.orientation += 1

                b_face[x] = item

        for x in list(b_face.keys()):
            self.cube[tuple(np.dot(b_matrix, x))] = b_face.pop(x)


    def __str__(self):

        w_face = "      " + self.cube[(-1, -1, 1)].get_colour(0) + self.cube[(-1, 0, 1)].get_colour(0) + self.cube[(-1, 1, 1)].get_colour(0) + "\n      " + self.cube[(0, -1, 1)].get_colour(0) + str(self.cube[(0, 0, 1)]) + self.cube[(0, 1, 1)].get_colour(0) + "\n      " + self.cube[(1, -1, 1)].get_colour(0) + self.cube[(1, 0, 1)].get_colour(0) + self.cube[(1, 1, 1)].get_colour(0) + "\n"
        w_edge = self.cube[(-1, -1, 1)].get_colour(1) + self.cube[(0, -1, 1)].get_colour(1) + self.cube[(1, -1, 1)].get_colour(2) + self.cube[(1, -1, 1)].get_colour(1) + self.cube[(1, 0, 1)].get_colour(1) + self.cube[(1, 1, 1)].get_colour(2) + self.cube[(1, 1, 1)].get_colour(1) + self.cube[(0, 1, 1)].get_colour(1) + self.cube[(-1, 1, 1)].get_colour(2) + self.cube[(-1, 1, 1)].get_colour(1) + self.cube[(-1, 0, 1)].get_colour(1) + self.cube[(-1, -1, 1)].get_colour(2) + "\n"
        middle = self.cube[(-1, -1, 0)].get_colour(0) + str(self.cube[(0, -1, 0)]) + self.cube[(1, -1, 0)].get_colour(0) + self.cube[(1, -1, 0)].get_colour(1) + str(self.cube[(1, 0, 0)]) + self.cube[(1, 1, 0)].get_colour(1) + self.cube[(1, 1, 0)].get_colour(0) + str(self.cube[(0, 1, 0)]) + self.cube[(-1, 1, 0)].get_colour(0) + self.cube[(-1, 1, 0)].get_colour(1) + str(self.cube[(-1, 0, 0)]) + self.cube[(-1, -1, 0)].get_colour(1) + "\n"
        y_edge = self.cube[(-1, -1, -1)].get_colour(2) + self.cube[(0, -1, -1)].get_colour(1) + self.cube[(1, -1, -1)].get_colour(1) + self.cube[(1, -1, -1)].get_colour(2) + self.cube[(1, 0, -1)].get_colour(1) + self.cube[(1, 1, -1)].get_colour(1) + self.cube[(1, 1, -1)].get_colour(2) + self.cube[(0, 1, -1)].get_colour(1) + self.cube[(-1, 1, -1)].get_colour(1) + self.cube[(-1, 1, -1)].get_colour(2) + self.cube[(-1, 0, -1)].get_colour(1) + self.cube[(-1, -1, -1)].get_colour(1) + "\n"
        y_face = "      " + self.cube[(1, -1, -1)].get_colour(0) + self.cube[(1, 0, -1)].get_colour(0) + self.cube[(1, 1, -1)].get_colour(0) + "\n      " + self.cube[(0, -1, -1)].get_colour(0) + str(self.cube[(0, 0, -1)]) + self.cube[(0, 1, -1)].get_colour(0) + "\n      " + self.cube[(-1, -1, -1)].get_colour(0) + self.cube[(-1, 0, -1)].get_colour(0) + self.cube[(-1, 1, -1)].get_colour(0) + "\n"

        return w_face + w_edge + middle + y_edge + y_face
