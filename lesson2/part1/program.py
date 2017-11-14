# The random library provides the randint function for generating a random
# integer in a range. It also provides a random function to generate a random
# decimal in the range [0.0, 1.0).
from random import randint, random

# We will try to generate a random integer and then print it out.
x = randint(1, 10)
print(x)

# We can also generate a random decimal.
y = random()
print(y)
