import math 

def selu(x):
    """
    Apply SELU activation to each element.
    """
    lambda_ = 1.0507009873554804934193349852946
    alpha = 1.6732632423543772848170429916717
    output = []

    for e in x:
        if e <= 0:
            fact = alpha * (math.exp(e) - 1)
        else:
            fact = e
        output.append(lambda_ * fact)

    return output

