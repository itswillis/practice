# result is an integer value 
# rounded to the nearest whole number 

# 2 miles and 12 yards is approx 3230 m

# use round()

miles = float(input("Enter the miles: "))
yards = float(input("Enter the yards: "))

# 1760 yards in a mile 
# 0.9144 metres in a yard

#convert miles into yards

yards_1 = 1760 * miles

metre_1_conv = yards_1 * 0.9144

metre_2_conv = yards * 0.9144

result = metre_1_conv + metre_2_conv

print(f"{int(miles)} miles {int(yards)} yards is approximately {round(result)} metres.")