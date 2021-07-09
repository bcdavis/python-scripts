
length = int(input("Length of lot -- "))
width = int(input("Width of lot --- "))
houseSize = int(input("Size of house -- "))

area = length * width
#print(area)


# 25/hr = 0.0069/sec
hourCost = 0.00694444
speed = 10800 # # square feet per hour
grassSize = area - houseSize

newSize = grassSize - speed
newTime = int(newSize/3)

extratime = 3600 + newTime  #4100 seconds
totalCost = hourCost * extratime

season = totalCost * 26
seasonCost = season - (0.05 * season) # -5%


print("\nSize of lot ------------- %d square feet"% area)
print("Cost for one mowing ----- $%0.2f"% totalCost)
print("Cost for entire season -- $%0.2f"% seasonCost)




