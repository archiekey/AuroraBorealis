from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn import svm
from sklearn.metrics import accuracy_score



from preprocesstest import testdata
from preprocesstrainingdata import labels
from preprocesstrainingdata import protrainingdata

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 stop_words='english')
features_train_transformed = vectorizer.fit_transform(protrainingdata)
features_test_transformed  = vectorizer.transform(testdata)



bagvectorizer = CountVectorizer()

bag_of_words = bagvectorizer.fit(protrainingdata)
bag_of_words = bagvectorizer.transform(protrainingdata)

clf = svm.SVC()

fulldata = len(protrainingdata)
halfdata = len(protrainingdata)/2
print (halfdata)
print fulldata
#newtrain = features_train_transformed[0:halfdata]
newtrain = bag_of_words[0:halfdata]
clf.fit(newtrain ,labels[0:halfdata])

pred = clf.predict(bag_of_words[halfdata+1:fulldata])#features_train_transformed[halfdata+1:fulldata])

#print features_t_transformed[3]
#print pred

print accuracy_score(pred,labels[halfdata+1:fulldata])
#for testing in range(0,20):
	#print features_test_transformed[testing]




