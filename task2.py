
def main(x):
    if x < 66:
        return (47 * x**9) + x**6
    elif x >= 66 and x < 92:
        return x**7 - (8 * x * x)**5
    elif x >= 92 and x < 187:
        return x**7
    return 8 * x**5
