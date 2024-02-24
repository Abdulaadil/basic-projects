import random 
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number =["0","1","2","3","4","5","6","7","8","9"]
symbol = ["#","$","%","^","&","*","(",")"]

print("welcome to the password generator")
alphabet = int(input(f"howmany alphabet you need to generate\n"))
num = int(input(f"howmany number you need to generate\n"))
sym = int(input(f"howmany symbol you need to generate\n"))
password = []
for i in range(1,alphabet+1):
   password.append(random.choice(alpha))
for j in range(1,num+1):
   password.append(random.choice(number))
for k in range(1,sym+1):
   password.append(random.choice(symbol))
random.shuffle(password)
r = ""
for y in range(0,len(password)-1):
   r = r +password[y]
print(r)