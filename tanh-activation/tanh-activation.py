import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """       

    x = np.array(x)


    pexp = np.exp(x)
    nexp = np.exp(-x)

    n = pexp - nexp
    d = pexp + nexp
    vals = n / d

    return vals.reshape(1) if vals.ndim == 0 else vals