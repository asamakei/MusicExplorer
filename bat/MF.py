# simple matrix factorization
import numpy as np
import pandas as pd

def matrix_factorization(ratings, K, steps=5000, alpha=0.0002, beta=0.02):
    P = np.random.rand(ratings.shape[0], K)
    Q = np.random.rand(K, ratings.shape[1])
    Q = Q.T
    for step in range(steps):
        for i in range(len(ratings)):
            for j in range(len(ratings[i])):
                if ratings[i][j] > 0:
                    eij = ratings[i][j] - np.dot(P[i,:], Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = np.dot(P, Q)
        e = 0
        for i in range(len(ratings)):
            for j in range(len(ratings[i])):
                if ratings[i][j] > 0:
                    e = e + pow(ratings[i][j] - np.dot(P[i,:], Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * (pow(P[i][k], 2) + pow(Q[k][j], 2))
        if e < 0.001:
            break
    return P, Q.T
    