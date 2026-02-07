import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """

    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    mse = np.sum((y_pred - y_true) ** 2)
    mse /= len(y_true)

    return mse