def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    
    percents = []
    for i in range(1, len(series)):
        curr_ele = series[i]
        prev_ele = series[i - 1]
        if prev_ele != 0:
            frac = (curr_ele - prev_ele) / prev_ele
        else:
            frac = 0.0
        percents.append(frac)
    
    return percents
