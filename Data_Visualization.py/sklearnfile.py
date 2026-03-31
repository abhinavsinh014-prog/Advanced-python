from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np
from sklearn.utils import check_X_y
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


class MostFrequentClassClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self):
        self.most_frequent = None

    def fit(self, X, y):
        
        X, y = check_X_y(X, y)

        y = np.ravel(y)

        unique_classes, counts = np.unique(y, return_counts=True)
        self.most_frequent_ = unique_classes[np.argmax(counts)]

        return self    
    
    def predict(self, X):
        if self.most_frequent_ is None:
            raise ValueError("This classifier instance is not fitted yet.")
        
        return np.full(shape=(X.shape[0],), fill_value=self.most_frequent_)

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

  
classifier = MostFrequentClassClassifier()
classifier.fit(X_train, y_train)

predictions = classifier.predict(X_test)
print(f"Predicted class for all test instances: {predictions[0]}")

print(classifier.most_frequent_)