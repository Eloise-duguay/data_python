# TODO: it's a playground, let's write some code (no unit tests to run here)
from math import pi

def circle_math(radius):
    perimeter = 2 * pi * radius
    area = pi * radius * radius
    return [ perimeter, area ]
    

values = circle_math(5)
print(f"radius=5, perimeter={round(values[0], 1)}, area={round(values[1], 1)}")

#radius = int('5')
#perimeter = radius * 2
#area = perimeter * pi
#print (area)


#sentence = f"the radius is set to {radius}"
#print (sentence)
#sentence2 = f"Perimeter of the circle is {perimeter}"
#print (sentence2)
#sentence3 = f"Area of the disk is {area}"
#print (sentence3)

 
 
 