from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans


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

kmeans = KMeans(n_clusters = 2)

fulldata = len(protrainingdata)
halfdata = len(protrainingdata)/2
newtrain = features_train_transformed[0:halfdata].toarray()
#newtrain = bag_of_words[0:halfdata].toarray()

kmeans.fit(features_test_transformed )
pred = kmeans.predict(features_train_transformed)


print accuracy_score(pred,labels)
