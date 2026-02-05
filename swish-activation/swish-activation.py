import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """

    x = np.asarray(x)

    fact = 1 + np.exp(-x)
    fact = 1 / fact

    output = x * fact

    return output.reshape(1) if output.ndim == 0 else output