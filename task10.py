class MealyError(Exception):
    pass


class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def mix(self):
        match self.state:
            case 'A':
                self.state = 'B'
                return 0
            case 'D':
                self.state = 'A'
                return 5
            case 'E':
                self.state = 'A'
                return 7
            case 'B':
                self.state = 'E'
                return 2
            case _:
                raise MealyError('mix')

    def mass(self):
        match self.state:
            case 'C':
                self.state = 'D'
                return 3
            case 'D':
                self.state = 'E'
                return 4
            case 'E':
                self.state = 'F'
                return 6
            case _:
                raise MealyError('mass')

    def melt(self):
        match self.state:
            case 'B':
                self.state = 'C'
                return 1
            case 'E':
                self.state = 'C'
                return 8
            case _:
                raise MealyError('melt')


def main():
    return MealyMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.mix() == 0
    assert o.mix() == 2
    assert o.melt() == 8
    assert o.mass() == 3
    assert o.mass() == 4
    assert o.mix() == 7
    assert o.mix() == 0
    assert o.melt() == 1
    assert o.mass() == 3
    assert o.mix() == 5
    assert o.mix() == 0
    assert o.mix() == 2
    assert o.mass() == 6
    raises(lambda: o.mix(), MealyError)
    raises(lambda: o.melt(), MealyError)
    raises(lambda: o.mass(), MealyError)

