from __future__ import division

def cel_to_fah(c):
    temp = c*9/5 + 32
    return temp

    
def fah_to_cel(f):
    temp = (f - 32)*5/9
    return temp


celsius = 37
fahrenheit = 72

print "{} degrees F = {} degrees C".format(fahrenheit, fah_to_cel(fahrenheit))
print "{} degrees C = {} degrees F".format(celsius, cel_to_fah(celsius) )                                         
