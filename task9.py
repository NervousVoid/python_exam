import re


def main(table):
    res = []
    for i in range(len(table)):
        if None in table[i]:
            continue
        cur = [1, 1, 1]
        s = table[i][0].split('|')
        if s[1] == 'false':
            cur[0] = 'нет'
        elif s[1] == 'true':
            cur[0] = 'да'
        cur[2] = s[0].replace('.', '/')
        m = re.search(r'\d{3}-\d{2}-\d{2}', table[i][1])
        cur[1] = m.group(0).replace('-', '')
        res.append(cur)
    return res

x = [
        ["12.10.04|false", '(218) 799-75-98', '(218) 799-75-98'],
        ["10.05.00|true",'(278) 506-20-21','(278) 506-20-21'],
        [None, None, None],
        ["12.08.04|true",'(927) 044-07-26','(927) 044-07-26'],
    ]

main(x)
