import random
import os
import errno
"""
randomprime.py

This small code is intended to be a test for slurm [https://slurm.schedmd.com/] running on a cluster hat [https://clusterhat.com/].  

Nodes on the clusterhat are limited to a single core and in the current configuration 200mb of RAM.

This program will pick a (random?) number between 1 and 1_000_000, check if it is prime, save that information and move on to the next (random?) number.  The idea is to do this 1_000_000 times.  

The final result is saved to a file.

To save ram and just get a list of what is or isn't prime (with no ordering) I will create a bytearray  
"""
# create bytearray primelist
primelist=bytearray(1000000)
# set the output file
outputfile = "/home/notlarry/randomprime/primesearch.results"
# create the direcotry if it does not exist
os.makedirs(os.path.dirname(outputfile), exist_ok=True)
with open(outputfile, "a") as f:
# for 1000000 itinerations
    for x in range(0, 100000):
        # print statement for debugging
        print(str(x) + " x")
# generate a random integer between 1 and 100000
        num = random.randint(1,1000000)
        # print statement for debugging
        print(str(num) + " num")
    # prime numbers are greater than 1
        if num > 1:
       # check for factors
           for i in range(2,num):
               if (num % i) == 0:
                   primelist[(num)] = 3 
                   break
           else:
                   primelist[(num)] = 0
           
    # if input number is less than
    # or equal to 1, it is not prime
        else:
                   primelist[(num)] = 2
    for val in primelist:
#            f.write(str (val) + (key) + "\n")
        print(val)
