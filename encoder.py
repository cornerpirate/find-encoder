#!/usr/bin/python
# script used to apply all encoding codecs within python
# well at least the ones I could find.
#
# calling: ./encoder.py <texttoencode>
# for example: ./encoder.py "aaaaa"
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
	print codec + ": " + codecs.encode(input, codec)

# Do some specific baseX encodings
print 'base64: ' + base64.b64encode(input)
print 'base32: ' + base64.b32encode(input)
print 'base16: ' + base64.b16encode(input)

#Do some specific ascii encodings
print 'hexlify: ' + binascii.hexlify(input)
print 'ascii-hex: ' + input.encode('hex')
