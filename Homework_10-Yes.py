class MealyError(Exception):
    pass


class Mealy:
    def __init__(self):
        self.state = 'A'

    def base(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'E':
            self.state = 'F'
            return 5
        elif self.state == 'F':
            self.state = 'F'
            return 8
        else:
            raise MealyError('base')

    def turn(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 3
        elif self.state == 'E':
            self.state = 'A'
            return 7
        else:
            raise MealyError('turn')

    def share(self):
        if self.state == 'D':
            self.state = 'B'
            return 4
        elif self.state == 'E':
            self.state = 'B'
            return 6
        else:
            raise MealyError('share')


def test():
    a1 = Mealy()
    assert a1.state == 'A'
    assert a1.base() == 0
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.turn() == 7
    a1 = main()
    assert a1.base() == 0
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.share() == 4
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.turn() == 7
    a1 = main()
    assert a1.base() == 0
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.share() == 4
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.share() == 6
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.turn() == 7
    a1 = main()
    assert a1.base() == 0
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.share() == 6
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.turn() == 7
    a1 = main()
    assert a1.base() == 0
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.base() == 5
    assert a1.base() == 8
    a1 = main()
    assert a1.base() == 0
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.share() == 4
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.base() == 5
    assert a1.base() == 8
    a1 = main()
    assert a1.base() == 0
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.share() == 4
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.share() == 6
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.base() == 5
    assert a1.base() == 8
    a1 = main()
    assert a1.base() == 0
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.share() == 6
    assert a1.turn() == 1
    assert a1.turn() == 2
    assert a1.turn() == 3
    assert a1.base() == 5
    assert a1.base() == 8
    try:
        a1.turn()
    except MealyError as e:
        assert str(e) == 'turn'
    try:
        a1.share()
    except MealyError as e:
        assert str(e) == 'share'
    try:
        a1 = main()
        a1.base()
        a1.base()
    except MealyError as e:
        assert str(e) == 'base'


def main():
    return Mealy()
