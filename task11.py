# from struct import unpack_from, calcsize
# from typing import Any, Callable


# class Types:
#     char = 'c'
#     int8 = 'b'
#     uint8 = 'B'
#     int16 = 'h'
#     uint16 = 'H'
#     int32 = 'i'
#     uint32 = 'I'
#     int64 = 'q'
#     uint64 = 'Q'
#     float = 'f'
#     double = 'd'


# class BinaryReader:
#     def __init__(self, stream, offset, order=">"):
#         self.stream = stream
#         self.offset = offset
#         self.order = order

#     def jump(self, offset):
#         reader = BinaryReader(self.stream, offset, self.order)
#         return reader

#     def read(self, pattern):
#         size = calcsize(pattern)
#         data = unpack_from(self.order + pattern, self.stream, self.offset)
#         self.offset += size
#         return data[0]


# def read_d(reader):
#     d1 = reader.read(Types.uint8)
#     d2_size = reader.read(Types.uint16)
#     d2_offset = reader.read(Types.uint16)
#     d2_reader = reader.jump(d2_offset)
#     d2 = [d2_reader.read(Types.double) for _ in range(d2_size)]
#     d3 = [reader.read(Types.uint16) for _ in range(2)]
#     d4 = reader.read(Types.uint8)
#     d5 = reader.read(Types.int64)
#     d6 = reader.read(Types.uint64)
#     return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6)


# def read_c(reader):
#     c1 = reader.read(Types.uint32)
#     c2 = reader.read(Types.int8)
#     c3 = reader.read(Types.int64)
#     c4 = reader.read(Types.int8)
#     return dict(C1=c1, C2=c2, C3=c3, C4=c4)


# def read_b(reader):
#     b1 = reader.read(Types.double)
#     b2_size = reader.read(Types.uint16)
#     b2_offset = reader.read(Types.uint32)
#     b2_reader = reader.jump(b2_offset)
#     b2 = [read_c(b2_reader) for _ in range(b2_size)]
#     b3 = b''.join([reader.read(Types.char) for _ in range(6)]).decode('utf-8')
#     b4_offset = reader.read(Types.uint16)
#     b4_reader = reader.jump(b4_offset)
#     b4 = read_d(b4_reader)
#     b5 = reader.read(Types.float)
#     b6 = reader.read(Types.uint16)
#     return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6)


# def read_a(reader):
#     b_offset = reader.read(Types.uint16)
#     b_reader = reader.jump(b_offset)
#     a1 = read_b(b_reader)
#     a2 = reader.read(Types.int64)
#     return dict(A1=a1, A2=a2)


# def main(stream):
#     return read_a(BinaryReader(stream, 5))

# x = (b'qUANN\x00U\xb3\xed\x83;`_\xe4\xeel\x9a\n\xa2\\F\xb3t\xa9\xdc\x17\x93_'
#  b'\x9c\xa3z\x19\xa3\x8cx\xb3R\xea\x8clg\x89\xd2\xbf\xd4p\x05\xc0\xf22\xec?'
#  b'\xbac\xe5*\xe0\xbe\x80?\x00\x02\x00+\x9736/\xff \x14O\x18rJ\xa4\xb4N\x05\x06'
#  b'\xb3q\xe7\xe0\xc3\xbf\xe5\xce\xc3\x8d\x91\\\xfa\x00\x02\x00\x00\x00\x0feanyj'
#  b'r\x00;\xbfQ=\xbdJq')

# print(main(x))

from struct import unpack_from, calcsize
from typing import Any, Callable


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


class BinaryReader:
    def __init__(self, stream, offset, order="<"):
        self.stream = stream
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_d(reader):
    d1 = [reader.read(Types.uint16) for _ in range(3)]
    d2 = reader.read(Types.int32)
    d3 = reader.read(Types.uint32)
    return dict(D1=d1, D2=d2, D3=d3)


def read_c(reader):
    c1 = b''.join([reader.read(Types.char) for _ in range(2)]).decode('utf-8')
    c2 = reader.read(Types.uint8)
    c3 = read_d(reader)
    c4_size = reader.read(Types.uint16)
    c4_offset = reader.read(Types.uint16)
    c4_reader = reader.jump(c4_offset)
    c4 = [c4_reader.read(Types.int32) for _ in range(c4_size)]
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_b(reader):
    b1 = reader.read(Types.double)
    b2 = reader.read(Types.int32)
    return dict(B1=b1, B2=b2)


def read_a(reader):
    a1 = reader.read(Types.float)
    b_offset = reader.read(Types.uint32)
    b_reader = reader.jump(b_offset)
    a2 = read_b(b_reader)
    a3 = [read_c(reader) for _ in range(2)]
    a4_size = reader.read(Types.uint32)
    a4_offset = reader.read(Types.uint32)
    a4_reader = reader.jump(a4_offset)
    a4 = [a4_reader.read(Types.int8) for _ in range(a4_size)]
    a5 = reader.read(Types.double)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5)


def main(stream):
    return read_a(BinaryReader(stream, 3))

x = b'UPB\x9e\x97\xc5\xbeE\x00\x00\x00fm\xca\xf2E\xdb\x8aq\xe6X3k\xf7\xd0\xfb \xdd' \
    b'\x03\x00Q\x00jr!\x84:\xce\xc3\x8fw\xc4u\x80\x9ei\xc0~\xb0\x02\x00]' \
    b'\x00\x04\x00\x00\x00e\x00\x00\x00\x1c\x99\xf1~\xd6o\xeb?\xa4\x8fw' \
    b'T\xae\x05\xd2?\x9b\nS\x99]\xf8\\\xec\xbfPZ\xbe\x13\xdb%8\xa9\x07(Yc\x14W' \
    b'D\xf4\x81A\x1d'

print(main(x))
