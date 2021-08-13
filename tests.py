from collections import namedtuple

import pytest

from .main import Constant, Term


@pytest.mark.parametrize("coeff", (0,))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (0, 1, 2))
def test_term_from_parts_with_coefficient_zero(coeff, var, pow):
    term = Term.from_parts(coeff, var, pow)
    assert isinstance(term, Constant)
    assert term.value == 0


@pytest.mark.parametrize("coeff", (0, 1, 2))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (0,))
def test_term_from_parts_with_power_zero(coeff, var, pow):
    term = Term.from_parts(coeff, var, pow)
    assert isinstance(term, Constant)
    assert term.value == coeff


@pytest.mark.parametrize("coeff", (1, 2))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (1, 2))
def test_term_from_parts(coeff, var, pow):
    term = Term.from_parts(coeff, var, pow)
    assert isinstance(term, Term)
    assert term.coefficient == coeff
    assert term.variable == var
    assert term.power == pow


@pytest.mark.parametrize("coeff", (0, 1, 2))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (0, 1, 2))
def test_term_equality(coeff, var, pow):
    assert Constant(coeff) == Constant(coeff)
    assert Term(coeff, var, pow) == Term(coeff, var, pow)

    C = namedtuple("Constant", ["value"])
    T = namedtuple("Term", ["coefficient", "variable", "power"])

    assert C(coeff) != Constant(coeff)
    assert T(coeff, var, pow) != Term(coeff, var, pow)


@pytest.mark.parametrize("coeff", (0, 1, 2))
def test_differentiation_of_constant(coeff):
    assert Constant(coeff).differentiate() == Constant(0)
