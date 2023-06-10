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


def read_e(reader):
    e1 = reader.read(Types.uint64)
    e2 = reader.read(Types.uint32)
    e3 = reader.read(Types.float)
    e4 = reader.read(Types.float)
    e5 = reader.read(Types.int16)
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5)


def read_d(reader):
    d1 = reader.read(Types.uint16)
    d2_size = reader.read(Types.uint16)
    d2_offset = reader.read(Types.uint32)
    d2_reader = reader.jump(d2_offset)
    d2 = [d2_reader.read(Types.int64) for i in range(d2_size)]
    d3 = reader.read(Types.uint32)
    d4 = reader.read(Types.uint32)
    d5 = reader.read(Types.float)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5)


def read_c(reader):
    c1_size = reader.read(Types.uint32)
    c1_offset = reader.read(Types.uint16)
    c1_reader = reader.jump(c1_offset)
    c1 = ''.join([c1_reader.read(Types.char).decode('utf-8')
                  for i in range(c1_size)])
    d_offset = reader.read(Types.uint16)
    d_reader = reader.jump(d_offset)
    c2 = read_d(d_reader)
    return dict(C1=c1, C2=c2)


def read_b(reader):
    b1 = reader.read(Types.uint16)
    b2 = reader.read(Types.int8)
    b3 = reader.read(Types.int32)
    b4 = reader.read(Types.uint8)
    b5 = reader.read(Types.int64)
    c_offset = reader.read(Types.uint32)
    c_reader = reader.jump(c_offset)
    b6 = read_c(c_reader)
    b7 = reader.read(Types.double)
    b8 = reader.read(Types.uint16)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8)


def read_a(reader):
    a1 = reader.read(Types.float)
    a2 = reader.read(Types.int32)
    a3 = read_b(reader)
    a4 = [read_e(reader.jump(reader.read(Types.uint32))) for i in range(2)]
    a5 = reader.read(Types.uint64)
    a6 = reader.read(Types.uint16)
    a7 = [reader.read(Types.uint16) for i in range(5)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def main(stream):
    return read_a(BinaryReader(stream, 4))

if __name__ == '__main__':
    print(main(b'CRXS\x16\x13%\xbf\x10d\x15\xdc\nD0\x86\x9e;\xc5)p\x88]\x04t\xac\xa4\xfc'
 b'l\x00\x00\x00\xf8\xe5\xedf\xf28\xdd?\xbb\x8et\x00\x00\x00\x8a\x00'
 b'\x00\x00\xcd>\xbe\xa5\x93Ph\x9f\xa2\x0b\xe5\x8fm\xc9\x84\xa4d\xb8\x90@xi'
 b'4%\xe1\x13\xddJ\xf83\x85\xec\x06*\xcc\x84\x0c\xaa+\xa4\x02\x00H\x00\x00\x00'
 b'\xe4\xc8-\xd68QeD\xf3:@?\x02\x00\x00\x00F\x00X\x00\xf7m\xd2\xbe\xc30\xda\xce'
 b'\x9c\x8c\xbb\xd6^\xc8y\xbf\x0c@\xf5\xbe\x9av\xfa\x9c~\x04\x02\xb9'
 b'\xef\x149\xc5w\x13\xfbK6>&\x0c\x9c\xbe\xb7\x88'))