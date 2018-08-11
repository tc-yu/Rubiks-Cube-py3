import Cube
#import Scrambler
from PIL import Image
import random




def image(str1):
    im = Image.open("Untitled.png")

    colourscheme = [(201, 51, 249, 99), (251, 51, 299, 99), (301, 51, 349, 99), (201, 101, 249, 149), (251, 101, 299, 149), (301, 101, 349, 149), (201, 151, 249, 199), (251, 151, 299, 199), (301, 151, 349, 199), (51, 201, 99, 249), (101, 201, 149, 249), (151, 201, 199, 249), (201, 201, 249, 249), (251, 201, 299, 249), (301, 201, 349, 249), (351, 201, 399, 249), (401, 201, 449, 249), (451, 201, 499, 249), (501, 201, 549, 249), (551, 201, 599, 249), (601, 201, 649, 249), (51, 251, 99, 299), (101, 251, 149, 299), (151, 251, 199, 299), (201, 251, 249, 299), (251, 251, 299, 299), (301, 251, 349, 299), (351, 251, 399, 299), (401, 251, 449, 299), (451, 251, 499, 299), (501, 251, 549, 299), (551, 251, 599, 299), (601, 251, 649, 299), (51, 301, 99, 349), (101, 301, 149, 349), (151, 301, 199, 349), (201, 301, 249, 349), (251, 301, 299, 349), (301, 301, 349, 349), (351, 301, 399, 349), (401, 301, 449, 349), (451, 301, 499, 349), (501, 301, 549, 349), (551, 301, 599, 349), (601, 301, 649, 349), (201, 351, 249, 399), (251, 351, 299, 399), (301, 351, 349, 399), (201, 401, 249, 449), (251, 401, 299, 449), (301, 401, 349, 449), (201, 451, 249, 499), (251, 451, 299, 499), (301, 451, 349, 499)]
    colour = {"w":(255,255,255),"o":(255,129,0),"b":(65,105,255),"g":(50,205,50),"y":(255,211,0),"r":(255,0,0)}
    color = ['w','o','b','g','y','r']
    
    for i in range(54):
        im.paste(colour[str1[i]], colourscheme[i])

    im.show()
    im.save("Sample.png", "png")

#region.show()

