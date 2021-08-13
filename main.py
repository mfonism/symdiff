from typing import Optional


class Term:
    @staticmethod
    def from_parts(coefficient: int, variable: str, power: int):
        assert isinstance(coefficient, int), "argument `coefficient` must be an integer"
        assert (
            isinstance(variable, str) and len(variable) == 1
        ), "argument `variable` must be a string of length 1"
        assert isinstance(power, int), "argument `power` must be an integer"

        if coefficient == 0:
            return Constant(0)
        if power == 0:
            return Constant(coefficient)
        return Term(coefficient, variable, power)

    def __init__(self, coefficient: int, variable: str, power: int):
        self.coefficient = coefficient
        self.variable = variable
        self.power = power

    def __eq__(self, other):
        if not isinstance(other, Term):
            return False
        return (
            self.coefficient == other.coefficient
            and self.variable == other.variable
            and self.power == other.power
        )

    def is_constant(self):
        return False


class Constant:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Constant):
            return False
        return self.value == other.value

    def is_constant(self):
        return True