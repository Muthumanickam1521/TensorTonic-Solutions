import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: scalar, list, or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """

    x = np.asarray(x)

    x_ = x / np.sqrt(2)
    erfs = np.vectorize(math.erf)(x_)

    fact = 0.5 * (erfs + 1)

    return fact * x



