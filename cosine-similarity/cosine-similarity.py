import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)

    ab = np.dot(a, b)
    a_ = np.linalg.norm(a)
    b_ = np.linalg.norm(b)
    a_b_ = a_ * b_

    if a_b_ == 0:
        return 0.0
    return float(ab / (a_ * b_))