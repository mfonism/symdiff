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

    def is_axis(self):
        return self.pow == 1

    def differentiate(self):
        if self.is_constant():
            return Term(coeff=0, var=self.var, pow=None)
        return Term(coeff=self.coeff * self.pow, var=self.var, pow=self.pow - 1)

    def __str__(self):
        if self.coeff == 0:
            return "0"
        rest = self._get_formatted_var_and_pow()
        if self.coeff == 1:
            return rest
        if rest == "1":
            return str(self.coeff)
        return f"{self.coeff}{rest}"

    def _get_formatted_var_and_pow(self):
        if self.is_constant():
            return "1"
        if self.is_axis():
            return self.var
        return f"{self.var}^{self.pow}"

    def __repr__(self):
        return str(self)
