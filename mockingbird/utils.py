def safe_range(min_val, max_val):

    min_val = abs(min_val)
    max_val = max(min_val, abs(max_val))
    
    delta = max_val - min_val

    # do we have a range error ?
    if delta == 0:
        max_val = max_val + 1

    return (min_val, max_val)