#!/usr/bin/python
# script used to apply decode all codecs within python
# well at least the ones I could find.
#
# calling: ./decoder.py <texttodecode>
# for example: ./decoder.py "636F726E6572706972617465"          
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
import codecs
import sys
import base64 
import binascii
from colorama import init, Fore

init() # initialise colour support

# Verify if the codec is likely to be the encoding mechanism
# print in GREEN if possibly the answer, and RED if not
def checkAnswer(input, answer, codec):
	if input==answer:
		# here the answer is the same as decoded value, not the answer
		print(Fore.RED + codec + ": " + answer + Fore.RESET)
	else:
		# here there is a chance we decoded the value
		print(Fore.GREEN +  codec + ": " + answer + Fore.RESET)
		
# Check that the user has input a string
if len(sys.argv) != 2:
	print "Usage : ./" + sys.argv[0] + " <input_text> "
	sys.exit(-1)

input = sys.argv[1]

all_codecs= [
'ascii',
'idna',
'punycode',
'bz2_codec',
'hex_codec',
'quopri_codec',
'string_escape',
'uu_codec',
'zlib_codec',
]

# Loop through each of the common built in codecs
# And display the result
for codec in all_codecs:
	try:
		answer = codecs.decode(input, codec)
		checkAnswer(input, answer, codec)
	except:
		print(Fore.RED + codec + ": <decoding error>" + Fore.RESET)

# Do some specific baseX encodings
try:
	answer = base64.b64decode(input)
	checkAnswer(input, answer, "base64")
except:
	print(Fore.RED +  "base64: <decoding error>" + Fore.RESET)

try:
	answer = base64.b32decode(input)
	checkAnswer(input, answer, "base32")
except:
	print(Fore.RED +  "base32: <decoding error>" + Fore.RESET)

try:
	answer = base64.b16decode(input)
	checkAnswer(input, answer, "base16")
except:
	print(Fore.RED +  "base16: <decoding error>" + Fore.RESET)

#Do some specific ascii encodings
try:
	answer = binascii.unhexlify(input) 
	checkAnswer(input, answer, "unhexlify")
except TypeError:
	print(Fore.RED +  "unhexlify: <decoding error>" + Fore.RESET)

try:
	answer = input.decode('hex')
	checkAnswer(input, answer, "ascii-hex")
except TypeError:
	print(Fore.RED +  "ascii-hex: <decoding error>" + Fore.RESET)
