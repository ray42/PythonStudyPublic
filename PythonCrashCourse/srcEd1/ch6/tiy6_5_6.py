#!/usr/bin/env python

# p108

#6-5
riverAndLocations = {
    "amazon river": "the amazon",
    "niles": "Egypt",
    "yangtze river": "china",
    }

for river, location in riverAndLocations.items():
    print(river.title() + " runs through " + location.title())

print("\nName of each river:")
for river in riverAndLocations.keys():
    print(river.title())

print("\nLocations:")
for location in riverAndLocations.values():
    print(location.title())

#6-6


