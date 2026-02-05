import math

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    
    output = []
    for e in x:
        if e <= 0:
            e = alpha * (math.exp(e) - 1)
        output.append(e)
    return output
    
