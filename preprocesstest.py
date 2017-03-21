import glob 
import numpy as np
import re
import preprocessor as p
#http://www.aaai.org/ocs/index.php/ICWSM/ICWSM11/paper/viewFile/2886/3262
# for name in glob.glob('tweet_log/*'):   # gets the filenames of the data text files
#	print name

filenames = glob.glob('tweet_log/*')

predata = []
textdata = []
cleaningdata = []
testdata = []
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

for hellodata in range(0,len(textdata)):
	#print(textdata[hellodata])
	tempphrase = re.sub(r'[^\x00-\x7F]',' ', textdata[hellodata])
	newphrase = re.sub(r'#',' ', tempphrase)
	cleaningdata.append(newphrase)

p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION,p.OPT.RESERVED,p.OPT.SMILEY)
for pro in range(0,len(cleaningdata)):
	testdata.append(p.clean(cleaningdata[pro]))
	
#for testing in range(0,len(testdata)):
	#print testdata[testing]

#testdata is the final output
