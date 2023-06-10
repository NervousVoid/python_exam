def main(bit_fields):
    return hex(
        int(bit_fields[3][1] << 15) +
        int(bit_fields[2][1] << 9) +
        int(bit_fields[1][1] << 5) +
        int(bit_fields[0][1])
    )

print(main([('T1', 6), ('T2', 0), ('T3', 35), ('T4', 14)]))#'0x74606'
#print(main([('T1', 5), ('T2', 14), ('T3', 43), ('T4', 10)]))#'0x557c5'
#print(main([('T1', 14), ('T2', 2), ('T3', 49), ('T4', 25)]))#'0xce24e'
#print(main([('T1', 13), ('T2', 8), ('T3', 22), ('T4', 24)]))#'0xc2d0d'