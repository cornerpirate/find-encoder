# find-encoder
A series of scripts to help me when I need to determine the encoding strategy used by an application.

find-encoder.py - run this against a file containing tokens for analysis one per line.
		- this will help you find if there is a fixed length for each token.
		- it will also tell you the unique characters encountered, and their distribution. 
		- use that information + Google basically to find the encoding.
encoder.py 	- run this against one string input. This will apply all encoding codecs I could find in python.
decoder.py	- run this against one string input. This will attempt to decode using all the codecs I could find in python.


