import random

userInp = input ("Hello, Welcome to my board ")

userInp_age = input('What is your age?')

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['`', '~', '!', '@', '#', '&', '*']

rs = random.choice(small)
rs2 = random.choice(small)
rc = random.choice(caps)
rc2 = random.choice(caps)
rn = random.choice(num)
rn2 = random.choice(num)
ry = random.choice(sym)
ry2 = random.choice(sym)

password =  rs + userInp_age + rc + rs2 + rn + ry + rn2 + rc2 + ry2

print(password)