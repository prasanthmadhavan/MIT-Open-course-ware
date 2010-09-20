"""
Problem 2
Write the function subStringMatchExact. This function takes two arguments: a target string,
and a key string. It should return a tuple of the starting points of matches of the key string in the target
string, when indexing starts at 0. Complete the definition for
def subStringMatchExact(target,key):
"""
from string import *

def subStringMatchExact(target,key):
    a=[find(target,key)]
    target=target[find(target,key)+len(key):]
    for i in range(len(target)):
        if find(target,key)!=-1:
            a.append(find(target,key)+len(key)+a[-1])
            target=target[find(target,key)+len(key):]
    return a

"""Uncomment the following lines to test the program.
print subStringMatchExact("atgacatgcacaagtatgcat","a")
print subStringMatchExact("atgaatgcatggatgtaaatgcag","a")
print subStringMatchExact("atgacatgcacaagtatgcat","atg")
print subStringMatchExact("atgaatgcatggatgtaaatgcag","atg")
print subStringMatchExact("atgacatgcacaagtatgcat","atgc")
print subStringMatchExact("atgaatgcatggatgtaaatgcag","atgc")
print subStringMatchExact("atgacatgcacaagtatgcat","atgca")
print subStringMatchExact("atgaatgcatggatgtaaatgcag","atgca")
"""


