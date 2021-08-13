from typing import Optional


class Term:
    def __init__(self, *, coeff: int, var: str, pow: Optional[int]):
        self.coeff = coeff
        self.var = var
        self.pow = pow

    def __eq__(self, other):
        if not isinstance(other, Term):
            return False

        if self.is_constant() and other.is_constant():
            return self.coeff == other.coeff

        return (
            self.coeff == other.coeff
            and self.var == other.var
            and self.pow == other.pow
        )

    def is_constant(self):
        return self.pow is None or self.pow == 0
