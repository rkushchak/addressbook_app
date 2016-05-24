'''
Created on May 19, 2016

@author: rkushchak
'''
import random, string


[chr(ord('a')+i) for i in range(12)]

def random_letters(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))

def random_number(length):
    return ''.join(random.choice(string.digits) for i in range(length))
