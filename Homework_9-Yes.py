from datetime import datetime


def main(table):
    new_table = []
    header = table[0]
    unique_columns = set()
    for col_idx in range(len(header)):
        column = [row[col_idx] for row in table]
        if column.count(None) < len(column):
            if header[col_idx] not in unique_columns:
                new_table.append(column)
                unique_columns.add(header[col_idx])

    new_table = [row for row in zip(*new_table) if None not in row]

    for row_idx in range(len(new_table)):
        row = new_table[row_idx]
        date_str, name = row[2].split(':')
        date = datetime.strptime(date_str, '%Y/%m/%d')
        row[2] = name.strip() + ' ' + date.strftime('%d.%m.%Y')

        for col_idx in range(len(row)):
            if row[col_idx] == 'Y':
                row[col_idx] = 'Да'
            elif row[col_idx] == 'N':
                row[col_idx] = 'Нет'
            elif isinstance(row[col_idx], str) and row[col_idx].isdigit():
                row[col_idx] = round(float(row[col_idx]))
    return [header] + new_table


table = [
    ['1', '2', '3'],
    ['Y', 'Y', '2004/09/14:Чивберг М.Б.'],
    ['N', 'N', '1999/04/21:Нидувак Е.И.'],
    ['N', 'N', '2001/04/04:Гифев Г.Г.'],
]
new_table = main(table)
for row in new_table:
    print(' '.join(str(cell) for cell in row))
