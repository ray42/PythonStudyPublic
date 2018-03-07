#!/usr/bin/env python3

l1 = ['one', ['two_one','two_two'], 'three']

# https://docs.python.org/3/library/copy.html
lcopy = l1.copy() # shallow copy
ldeepcopt = l1.copy() # deep copy
lcolon = l1[:] # shallow copy


def getdict():
    return {"k": 'val'}

print(getdict())

