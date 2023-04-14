#Abdulkadir Parlak 2210765025
import sys
try:
    twoPoints = int(sys.argv[1])
    threePoints = int(sys.argv[2])
    onePoints = int(sys.argv[3])
    totalPoints = twoPoints*2 + threePoints*3 + onePoints*1
    print(totalPoints)  # I didn't print result with string!

except (IndexError):

    def healthStatus(height, mass):
        float(height)
        float(mass)
        BMI = mass / (height**2)
        if BMI > 30:
            return "obeze"
        elif BMI > 24.9:
            return "overweight"
        elif BMI > 18.5:
            return "healthy"
        elif BMI > 0:
            return "underweight"


