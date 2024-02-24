print("welcome to tip calculator")
bill =int(input("what was the bill\n"))
tip = int(input("what is the percentage of tip 10 12 20\n"))
percentage = tip/100
bill2= bill*percentage
real_bill= bill+bill2
print("the total amount with percentage")
print(real_bill)
split= int(input("split the bill between how much people\n"))
print(round(real_bill/split,2))
