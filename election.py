from __future__ import division
from random import random
#Issues with this one

def election():
    A = 0
    B = 0

    count = 0

    for i in range(1, 4):
        print "Region ", i, ":"
        while count < 10000:
            vote = random()
            if vote < .5:
                A +=1
            else:
                B += 1
            count += 1

        print A, B
        
        a_chance = A/B
        b_chance = B/A

        print "Candidate A has a {}% chance of winning".format(a_chance)
        print "Candidate B has a {}% chance of winning".format(b_chance)

election()
    
