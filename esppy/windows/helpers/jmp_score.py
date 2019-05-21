import math
import numpy as np

# ----------------------------------------------------------------
# jmp_score.py
# Helper module with functions supporting the Python language
# scoring code generated by JMP
#
# Required by customer code: Yes
# ----------------------------------------------------------------


# return the index of the max value found in an array
# or -1 if all are missing
def max_array(len, lst):
    maxval = -float('inf')
    maxidx = 0
    count_miss = 0

    for i in range(0, len):
        if is_missing(lst[i]):
            count_miss = count_miss + 1
        elif maxval < lst[i]:
            maxval = lst[i]
            maxidx = i
    return -1 if (count_miss == len) else maxidx


# return the index of the min value found in an array
# or -1 if all are missing
def min_array(len, lst):
    minval = float('inf')
    minidx = 0
    count_miss = 0

    for i in range(0, len):
        if is_missing(lst[i]):
            count_miss = count_miss + 1
        elif minval > lst[i]:
            minval = lst[i]
            minidx = i
    return -1 if (count_miss == len) else minidx


def is_missing(x):
    return math.isnan(x) or math.isinf(x) or x is None


def exp(x):
    try:
        return math.exp(x)
    except OverflowError:
        return float('inf')


def pow(a, b=2):
    try:
        return math.pow(a, b)
    except OverflowError:
        return float('inf')


# Also known as logist or logistic
def squish(x):
    return 1.0 / (1.0 + exp(-x))


def squash(x):
    return 1.0 / (1.0 + exp(x))


# Returns true if the numbers are identical using straight comparison.
# If necessary, replace with a suitable comparison using a value of EPSILON
# appropriate for your domain.
def numeq(x, y):
    return x == y
    # return Math.abs(a - b) < EPSILON;


def vec_diag(M):
    """
    Returns the diagonal elements of the square matrix as a vector.
    """
    return np.diag(M).reshape(M.shape[0], 1)


def vec_quadratic(S, X):
    """
    Evaluates as Vec Diag( X * S * X` ).
    """
    if S.shape[1] == X.shape[0]:
        return vec_diag(np.dot(X.T, np.dot(S, X)))
    return vec_diag(np.dot(X, np.dot(S, X.T)))


def sum(S):
    """
    Return the sum of array elements treating missing (NaN) as zero.

    To match JMP's behavior, check if all elements are missing in
    which case missing is returned.
    """
    if np.all(np.isnan(S)):
        return np.nan
    return np.nansum(S)
