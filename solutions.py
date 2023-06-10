#1
import math


def main(z, y):
    return math.sqrt(27*z**2-92*y) - 62*(math.floor(98*z**2-(z**3)/20-83*y))**3

#2
import math


def main(y):
    if y < 109:
        return (1 + y ** 2) ** 5 - 39 * (39 * y) ** 7 - (y / 96 - 61) \
            ** 6
    if 109 <= y < 128:
        return math.fabs(y - 0.01 - 50 * y ** 3) ** 4 - 52 * y \
                - (55 * y ** 3) ** 7
    if 128 <= y < 225:
        return 0.5 - y ** 2
    if 225 <= y < 248:
        return y ** 3 + y ** 7 + math.fabs(y ** 3) ** 2 / 62
    if 248 <= y:
        return y / 10 + y ** 2

#3
import math


def main(
    m,
    p,
    a,
    b,
):
    part1 = 0
    part2 = 1
    for c in range(1, m + 1):
        part1 += c ** 6 - math.cos(c ** 3 + 1 + c ** 2) ** 2 - p ** 4
    for c in range(1, m + 1):
        sum = 0
        for i in range(1, b + 1):
            for k in range(1, a + 1):
                sum += c ** 4 + i ** 6 + 3 * math.floor(k)
        part2 *= sum
    return part1 + part2

#4
import math


def main(n):
    if n == 0:
        return -0.04
    if n == 1:
        return -0.15
    if n >= 2:
        return (main(n - 1) + main(n - 1) ** 2) ** 2 + 26 \
            * math.sin(main(n - 2)) ** 3

#5
import math


def main(z, y):
    sum = 0
    for i in range(1, len(z) + 1):
        sum += z[math.ceil(i / 4) - 1] / 10 + y[math.ceil(i / 3) - 1] \
            ** 2
    return sum

#6
def main(*r):
    s = (
        {"JFLEX", 1982, "APEX"},
        {"JFLEX", 1982, "ECL"},
        {"JFLEX", 2010},
        {"JFLEX", 1984, "SHELL"},
        {"JFLEX", 1984, "JULIA"},
        {"JFLEX", 1984, "XML", "IOKE"},
        {"JFLEX", 1984, "XML", "HCL"},
        {"JFLEX", 1984, "XML", "P4"},
        {"GOSU", "APEX", "SHELL"},
        {"GOSU", "APEX", "JULIA"},
        {"GOSU", "APEX", "XML"},
        {"GOSU", "ECL"},
        {"ALLOY"},
    )
    s1 = set(*r)
    return [i for i in range(len(s)) if not (len(s[i] - s1))][0]

#7
def main(args):
    return hex(
        (int(args[3], 16) << 24)
        + (int(args[2], 16) << 19)
        + (int(args[1], 16) << 11)
        + (int(args[0], 16) << 6)
    )

#8
def main(s):
    dict = {}
    s = s.replace('\n', ' ')
    s = s.replace('{', ' ')
    s = s.replace('}', ' ')
    s = s.replace('<=', ' ')
    s = s.replace(')', ' ')
    s = s.replace('q(', ' ')
    s = s.replace(';', ' ')
    s = s.split(' ')
    try:
        while True:
            s.remove('')
    except ValueError:
        pass
    s.remove('(')
    for i in range(0, len(s) - 1):
        if s[i] == 'define':
            key = s[i + 1]
            value = s[i + 2]
            dict[key] = value
    return dict

#9
def main(list1):
    new_list = []
    new_list.extend(list1)
    new_list = [[new_list[j][i] for j in range(len(new_list))] for i in
                range(len(new_list[0]))]
    no_duplicates = list()
    for row in new_list:
        if row not in no_duplicates:
            no_duplicates.append(row)
    new_list = [[no_duplicates[j][i] for j in
                range(len(no_duplicates))] for i in
                range(len(no_duplicates[0]))]
    list2 = []
    list2.extend(new_list)
    for i in range(0, len(list2)):
        if list2[i][1][list2[i][1].index(':') + 1] == 'N':
            list2[i][0] = '0'
        else:
            list2[i][0] = '1'
        list2[i][1] = (list2[i][1])[0:list2[i][1].index(':')]
        list2[i][1] = (list2[i][1])[3:]
        list2[i][1] = (list2[i][1])[0:3] + (list2[i][1])[4:]
        list2[i][1] = (list2[i][1])[0:6] + (list2[i][1])[7:]
        list2[i][1] = (list2[i][1])[0:8] + (list2[i][1])[9:]
        list2[i][2] = (list2[i][2])[0:list2[i][2].index('[')]
    return list2

#10
class MealyError(Exception):

    pass


class Mealy:

    def __init__(self):
        self.state = 'A'

    def rig(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        elif self.state == 'F':
            self.state = 'B'
            return 8
        elif self.state == 'B':
            self.state = 'B'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise MealyError('rig')

    def type(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'F'
            return 7
        else:
            raise MealyError('type')


def test():

    mealy1 = Mealy()
    assert mealy1.state == 'A'
    assert mealy1.rig() == 1
    assert mealy1.type() == 7
    assert mealy1.rig() == 8
    assert mealy1.rig() == 3
    assert mealy1.type() == 2
    assert mealy1.rig() == 4
    assert mealy1.type() == 5
    assert mealy1.rig() == 6
    mealy2 = main()
    assert mealy2.type() == 0
    assert mealy2.rig() == 3
    assert mealy2.type() == 2
    assert mealy2.rig() == 4
    assert mealy2.type() == 5
    assert mealy2.rig() == 6
    assert mealy2.type() == 7
    assert mealy2.rig() == 8
    mealy3 = main()
    try:
        mealy3.rig()
        mealy3.rig()
        mealy3.type()
        mealy3.rig()
        mealy3.rig()
    except MealyError as e:
        assert str(e) == 'rig'
    mealy4 = main()
    try:
        mealy4.rig()
        mealy4.rig()
        mealy4.type()
        mealy4.type()
    except MealyError as e:
        assert str(e) == 'type'


def main():
    return Mealy()

#11
import struct


def main(data):
    signature = b'\x59\x4c\x55\x41\x68'
    if not data.startswith(signature):
        return None
    result = {}
    offset = len(signature)
    b_data = data[offset:]
    b_size = struct.calcsize('> H 3s i h I H H 7b')
    b_values = struct.unpack_from('> H 3s i h I H H 7b', data, offset)
    b = {'B1': b_values[0],
         'B2': b_values[1].decode('utf-8'),
         'B3': b_values[2],
         'B4': b_values[3],
         'B5': b_values[4],
         'B6': [],
         'B7': list(b_values[7:])}
    c_offset = b_values[6]
    c_size = b_values[5]
    for i in range(2):
        c_values = struct.unpack_from('> d i', data, c_offset)
        c = {'C1': c_values[0],
             'C2': c_values[1]}
        b['B6'].append(c)
        c_offset += struct.calcsize('> d i')
    result['A1'] = b
    d_data = data[offset + b_size:]
    d_size = struct.calcsize('> H I B Q')
    d_values = struct.unpack_from('> H I B Q', d_data)
    d = {'D1': d_values[0],
         'D2': d_values[1],
         'D3': d_values[2],
         'D4': d_values[3]}
    result['A2'] = d
    a31 = struct.unpack_from('> I I', data, offset + b_size + d_size)
    a3_size = a31[0]
    a3_offset = a31[1]
    a3 = []
    for i in range(a3_size):
        a3_value = struct.unpack_from('> b', data, a3_offset)
        a3.extend(a3_value)
        a3_offset += struct.calcsize('> b')
    result['A3'] = a3
    return result
