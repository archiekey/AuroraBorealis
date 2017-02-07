import glob 
import numpy as np
#http://www.aaai.org/ocs/index.php/ICWSM/ICWSM11/paper/viewFile/2886/3262
# for name in glob.glob('tweet_log/*'):   # gets the filenames of the data text files
#	print name

filenames = glob.glob('tweet_log/*')

predata = []
textdata = []
for ele in filenames:
	with open(ele) as reading:
		for line in reading:
			array = line.split(",")
			for word in array:
				if word.startswith('"text":"'):
					#print(word)
					predata.append(word)

for indata in predata:
	textdata.append(indata[8:-1])
	print(indata[8:-1])


