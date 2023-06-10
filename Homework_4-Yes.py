def main(n):
    if n < 1:
        return 0.94
    elif n == 1:
        return -0.7
    else:
        return pow(main(n - 2), 2) / 42 + (main(n - 1) + 84)



print(main(4))
print(main(9))
print(main(3))
print(main(5))
print(main(7))

