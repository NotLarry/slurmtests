import random
import os
import errno

outputfile = "/home/notlarry/randomprime/primesearch.results"
os.makedirs(os.path.dirname(outputfile), exist_ok=True)
with open(outputfile, "a") as f:
# generate a random integer between 1 and 100000
    for x in range(0, 100000):
        num = random.randint(1,1000000)
    # prime numbers are greater than 1
        if num > 1:
       # check for factors
           for i in range(2,num):
               if (num % i) == 0:
                   f.write(str (num) + "is not a prime number\n")
                   break
           else:
               f.write(str (num) + "is a prime number\n")
           
    # if input number is less than
    # or equal to 1, it is not prime
        else:
           f.write(str (num) + "is not a prime number\n")



