from sklearn.naive_bayes import GaussianNB
import numpy as np

# Training data
features = np.asarray([[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [1, 4], [1, 5], [2, 5], [3, 5], [3, 3], [4, 4], [5, 3], [5, 1], [6, 2]])

labels = np.asarray(['A', 'A', 'A', 'A', 'A', 'B',  'B',  'B',  'B',  'B',  'B',  'B',  'B',  'B'])

classifier = GaussianNB()
classifier.fit(features, labels) # train model

# test model
features_input = np.asarray([[0, 2], [3, 2], [7, 5]])
predictions = classifier.predict(features_input)
print(predictions)

# Accuracy test

from sklearn.metrics import accuracy_score
#print(accuracy_score(predictions, labels))
