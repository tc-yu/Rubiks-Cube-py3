from numpy import random
import Cube
import image_output

def alg(n):

    move = [["R","L"], ["U","D"], ["F","B"]]
    direction = [" ","'","2"]

    algorithm = ""
    algor_list = []
    parallel = False
    prevMove = "A"
    prevY = 0
    i = 0

    while i < n:
        x = random.randint(2)
        y = random.randint(3)
        newMove = move[y][x]

        if newMove == prevMove:
            pass

        elif newMove in move[prevY]:
            if not parallel:
                algor_list.append(newMove + direction[random.randint(3)])
                algorithm += algor_list[-1] + " "
                prevMove = newMove
                prevY = y
                parallel = True
                i += 1

        else:
            algor_list.append(newMove + direction[random.randint(3)])
            algorithm += algor_list[-1] + " "
            prevMove = newMove
            prevY = y
            parallel = False
            i += 1

    print (algorithm + "\n")
    return algor_list

def scrambler(n):
    algor_list = alg(n)
    cube = Cube.Cube()

    for x in algor_list:
        if x[1] == " ":
            repeat = 1
        elif x[1] == "2":
            repeat = 2
        elif x[1] == "'":
            repeat = 3

        for i in range(repeat):
            if x[0] == "R":
                cube.r()

            elif x[0] == "L":
                cube.l()

            elif x[0] == "U":
                cube.u()

            elif x[0] == "D":
                cube.d()

            elif x[0] == "F":
                cube.f()

            else:
                cube.b()

    #print (str(cube))
    image_output.image((str(cube)))

def main():

    print ("Rubik's Cube scrambler by Ching, input the length of random algorithm you want and the resulting cube will be shown\nThis scrambler assume the use of Western color sheme with white face to the top and blue to the player")
    cube2 = Cube.Cube()
    print ("Basic orientation:")
    print (cube2)
    
    moves = input("Please input the number of steps you want the crambler to have: ")
    print ("For the meaning of algorithm, please refer to: \nhttp://w.astro.berkeley.edu/~converse/rubiks.php?id1=basics&id2=notation")
    scrambler(int(moves))
    
main()
