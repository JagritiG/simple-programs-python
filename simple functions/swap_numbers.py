# Following code swaps values of 2 variables without temporary variable.

def Swap_num(val1, val2):
    a, b = val1, val2
    a, b = b, a
    return (a, b)