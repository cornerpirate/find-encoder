#!/usr/bin/python
# script used to review a file of tokens line by line.
# it will work out the character set used and give you
# a clue as to what you are dealing with.
#
# calling: ./find-encoder.py <fileoftokens>
# for example: ./find-encoder.py cookies.txt          
# 
# Copyright 2016 cornerpirate.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# == Developers
# cornerpirate - https://twitter.com/cornerpirate
import sys
# Dictionary of characters
characters = {}

# function to loop throug every character and add to he characters dictionary
def updateCharacterSet(cookie):
    for char in cookie:

        # if char doesn't already exist add it
        if char not in characters:
            characters[char] = 1
        # if it already exists increment the count
        if char in characters:
            characters[char] = characters.get(char) + 1

# display analysis of the character set
def displayCharacterSet():
    # display the key set to show what characters existed in Cookies
    uniquecharacters = ""
    for character in characters:
        uniquecharacters = uniquecharacters + character

    # sort the uniquecharacters alphabetically
    uniquecharacters = ''.join(sorted(uniquecharacters))
    print "Unique Characters in values: " + uniquecharacters
    print "You can use that list to identify encoding scheme"
    print "===================="
    print "The following shows the number of occurences of each character"

    # display the number of occurances for each characters
    # ordered alphabetically by the character
    for character, count in sorted(characters.items()):
        print character + " : " + str(count)

    print "===================="

# Check command line arguments
if len(sys.argv)!=2:
    print "Usage: " + sys.argv[0] + " <cookie_file>"
    sys.exit(0)

file=sys.argv[1]
print "Analysing File: " + file
print "===================="


f=open(file)

min=0
max=0
count=0

# loop through every line
for cookie in f:

    cookie = cookie.strip()

    if count == 0:
        min = len(cookie)
        max = len(cookie)

    if len(cookie) < min:
        min = len(cookie)

    if len(cookie) > max:
        max = len(cookie)

    count= count + 1

    # update character set dictionary with this cookie
    updateCharacterSet(cookie)

# release lock on the file
f.close()

# display high level summary
print "Number of values: " + str(count)
print "Minimum Length: " + str(min)
print "Maximum Length: " + str(max)
print "===================="
# display character set analysis
displayCharacterSet()
