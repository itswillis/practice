import math

length = float(input("Enter a length: "))
width = float(input("Enter a width: "))
height = float(input("Enter a height: "))

volume = length * width * height

result = (f"Volume of the cube is {math.floor(volume)} cubic cm.")

print(result)

