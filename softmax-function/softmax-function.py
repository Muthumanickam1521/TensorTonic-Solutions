import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """

    x = np.array(x)

    if x.ndim < 2:
        xmax = np.max(x)
    else:
        xmax = np.max(x, axis=1, keepdims=True)

    exp = np.exp(x - xmax)

    if x.ndim < 2:
        sexp = np.sum(exp)
    else:
        sexp = np.sum(exp, axis=1, keepdims=True)
    return exp / sexp