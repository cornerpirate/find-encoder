#!/usr/bin/python
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
print "Number of Cookies: " + str(count)
print "Minimum Length: " + str(min)
print "Maximum Length: " + str(max)
print "===================="
# display character set analysis
displayCharacterSet()
