import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """


    
    x_ = np.array(x, dtype=float)


    if type(x) is float:
        return np.zeros(1) if x_ < 0 else x_.reshape(1)

    else:
        return x_.clip(0)