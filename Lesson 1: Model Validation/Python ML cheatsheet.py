#splitting data between features and labels, training data and test data

from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    features, labels, test_size=0.4, random_state=0)


#getting the accuracy score using various methods

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

# The decision tree classifier
clf1 = DecisionTreeClassifier()
clf1.fit(features_train,labels_train)
print "Decision Tree has accuracy: ",accuracy_score(clf1.predict(features_test),labels_test)
# The naive Bayes classifier

clf2 = GaussianNB()
clf2.fit(features_train,labels_train)
print "GaussianNB has accuracy: ",accuracy_score(clf2.predict(features_test),labels_test)

answer = { 
 "Naive Bayes Score": accuracy_score(clf1.predictpredict(features_test),labels_test, 
 "Decision Tree Score": accuracy_score(clf2.predictpredict(features_test),labels_test)
}
