def main(args):
    return hex(
        (args[5] << 33)
        + (args[4] << 23)
        + (args[3] << 17)
        + (args[2] << 12)
        + (args[1] << 5)
        + args[0]
    )
