import json
import preprocessor as p
import re
#parses a json file
with open('labeled_data.json')as f:
	data = f.read()
	jsondata = json.loads(data)
labels = []
prelabel = []
trainingdata = []
cleanedtrainingdata = [];
protrainingdata = [];
# takes the tweets and labels and puts them in seperate arrays
for tw in jsondata['info']:
	prelabel.append(tw['label'])
	trainingdata.append(tw['tweet'])

# if the label is Aurora a 1 is added to the labels array if not a 0 is added

for stuff in range(0,len(prelabel)):
    #print(trainingdata[stuff])
    if prelabel[stuff] == 'Aurora':
	labels.append(1)
    else:
	labels.append(0)

#preprocess the training data( gets rid of non unicode characters and hashtags)

for pro in range(0,len(trainingdata)):
	
	#p.clean(trainingdata[pro])
	#print trainingdata[pro]
	tempphrase = re.sub(r'[^\x00-\x7F]',' ', trainingdata[pro])
	newphrase = re.sub(r'#',' ', tempphrase)
	cleanedtrainingdata.append(newphrase)
	


#gets rid of all unnecessary twitter featuers such as urls retweets, mentions etc...
p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION,p.OPT.RESERVED,p.OPT.SMILEY)


for check in range(0,len(labels)):
#	print(prelabel[check], " " ,labels[check]);
#	print cleanedtrainingdata[check]
	protrainingdata.append(p.clean(cleanedtrainingdata[check]))



# print statement to test

#for pro1 in range(0,len(trainingdata)):
	#print protrainingdata[pro1]


#the final output is protrainingdata[] which is the tweets and labels[] which determines whether a tweet is aurora or not



