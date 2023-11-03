import numpy as np
from collections import defaultdict


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


def get_label_indices(labels):
    label_indices = defaultdict(list)

    for index, label in enumerate(labels):
        label_indices[label].append(index)

    return label_indices


label_indices = get_label_indices(Y_train)

print(label_indices)


def get_prior(label_indices):
    prior = {label: len(indices) for label, indices in label_indices.items()}

    total = sum(prior.values())

    for label in prior:
        prior[label] /= total

    return prior


prior = get_prior(label_indices)

print(prior)


def get_likelihood(features, label_indices, smoothing=0):
    likelihood = {}

    for label, indices in label_indices.items():
        likelihood[label] = features[indices].sum(axis=0) + smoothing

        total_count = len(indices)
        likelihood[label] = likelihood[label] / (total_count + 2 * smoothing)

    return likelihood


likelihood = get_likelihood(X_train, label_indices, 1)

print(likelihood)


def get_posterior(X, prior, likelihood):
    posteriors = []

    for x in X:
        posterior = prior.copy()

        for label, likelihood_label in likelihood.items():
            for i, feature in enumerate(x):
                posterior[label] *= likelihood_label[i] if feature else (
                    1 - likelihood_label[i])

        sum_posteriors = sum(posterior.values())

        for label in posterior:
            if posterior[label] == float('inf'):
                posterior[label] = 1.0
            else:
                posterior[label] /= sum_posteriors

        posteriors.append(posterior.copy())

    return posteriors


posterior = get_posterior(X_test, prior, likelihood)

print(posterior)
