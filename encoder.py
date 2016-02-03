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
