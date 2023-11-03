import numpy as np
from sklearn.naive_bayes import BernoulliNB

X_train = np.array([
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0],
    [1, 1, 0],
])

Y_train = ['Y', 'N', 'Y', 'Y']

X_test = np.array([
    [1, 1, 0]
])

clf = BernoulliNB(alpha=1.0, fit_prior=True)

clf.fit(X_train, Y_train)

pred_prob = clf.predict_proba(X_test)

pred = clf.predict(X_test)

print(pred)
