import random
import os
import errno

# create dictionary primelist
primelist={}
# set the output file
outputfile = "/home/notlarry/randomprime/primesearch.results"
# create the direcotry if it does not exist
os.makedirs(os.path.dirname(outputfile), exist_ok=True)
with open(outputfile, "a") as f:
# for 1000000 itinerations
    for x in range(0, 1000000):
# generate a random integer between 1 and 100000
        num = random.randint(1,1000000)
    # prime numbers are greater than 1
        if num > 1:
       # check for factors
           for i in range(2,num):
               if (num % i) == 0:
                   # add to dictionary primelist
                   primelist["is a prime number."] = (num)
                   break
           else:
#               f.write(str (num) + "is a prime number\n")
                   primelist["is not a prime number."] = (num)
           
    # if input number is less than
    # or equal to 1, it is not prime
        else:
#           f.write(str (num) + "is not a prime number\n")
                   primelist["A prime number is not "] = (num)
        for key,val in primelist.items():
            f.write(str (val) + (key) + "\n")
