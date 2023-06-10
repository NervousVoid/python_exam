def main(n):
    x = 0.94
    y = -0.7
    for i in range(n - 1):
        v = pow(main(n - 2), 2) / 42 + (main(n - 1) + 84)
        x = y
        y = v
    return y



print(main(4))
print(main(9))
print(main(3))
print(main(5))
print(main(7))