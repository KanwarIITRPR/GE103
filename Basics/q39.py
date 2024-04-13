import math

n = int(input("Enter the value of the radius of the circle: "))

def circle_area(r):
    area = math.pi * (r**2) # Area of a circle is (pi)(r)^2
    return area

print(f"The area of the given circle will be {circle_area(n)}.")