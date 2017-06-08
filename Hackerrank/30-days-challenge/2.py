# 12.00
# 20
# 8

mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

print "The total meal cost is " + str(int(round(mealCost + (mealCost*tipPercent/100) + (mealCost*taxPercent/100)))) + " dollars."