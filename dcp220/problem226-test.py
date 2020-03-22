import random
import string

all_lowercase_letters = list(string.ascii_lowercase)
longlist = []
for i in range(1000):
    string = ''
    j = random.randint(1, 15)
    for k in range(j):
        string += random.choice(all_lowercase_letters)
    longlist.append(string)
longlist = sorted(longlist)

print(longlist)