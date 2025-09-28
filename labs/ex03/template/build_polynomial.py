# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # N = x.shape[0]
    # d = degree + 1
    # poly = np.zeros(shape=(N, d))

    # for i in range(N):
    #     for j in range(d):
    #         poly[i, j] = x[i] ** j

    # return poly

    # This is a vectorized version of the nested for loops.
    # It uses numpy's broadcasting to compute the powers.
    # x[:, np.newaxis] has shape (N, 1)
    # np.arange(degree + 1) has shape (degree+1,)
    # The result of the power operation is a (N, degree+1) array.
    return x[:, np.newaxis] ** np.arange(degree + 1)
