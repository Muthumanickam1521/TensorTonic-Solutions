import numpy as np
from collections import Counter
def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """

    x = np.asarray(x)

    mean = float(np.mean(x))
    median = float(np.median(x))
    c = Counter(x)

    k = sorted(c.items(), key=lambda x: x[1], reverse=True)[0][0]

    return (mean, median, k)