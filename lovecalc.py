print("The Love Calculator is calculating your score...")
name1 = input() 
name2 = input() 
combine = name1 + name2
lowercase = combine.lower()
t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")

first_digit= t + r+ u + e

l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")

second_digit = l + o + v + e
score = int(str(first_digit)+ str(second_digit))

if (score < 10) or (score > 90) :
  print(f"score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


