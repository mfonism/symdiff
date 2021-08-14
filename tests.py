from collections import namedtuple

from .main import Term

import pytest

T = namedtuple("Term", ["coeff", "var", "pow"])


@pytest.mark.parametrize("coeff", (0, 1, 2))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (0, 1, 2))
def test_term_equality(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)
    another_term = Term(coeff=coeff, var=var, pow=pow)
    term_ish = T(coeff=coeff, var=var, pow=pow)

    assert term == another_term
    assert term != term_ish


@pytest.mark.parametrize("coeff", (0, 1, 2))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (0, None))
def test_term_is_constant_when_pow_is_zero_or_none(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.is_constant()
    assert not term.is_axial_line()


@pytest.mark.parametrize("coeff", (0, 1, 2))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("other_var", ("x", "y"))
@pytest.mark.parametrize("pow", (0, None))
@pytest.mark.parametrize("other_pow", (0, None))
def test_constants_with_equal_coeffs_are_equal(coeff, var, other_var, pow, other_pow):
    term = Term(coeff=coeff, var=var, pow=pow)
    other_term = Term(coeff=coeff, var=other_var, pow=other_pow)

    assert term == other_term


@pytest.mark.parametrize("coeff", (0, 1, 2))
@pytest.mark.parametrize("other_coeff", (3, 4, 5))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("other_var", ("x", "y"))
@pytest.mark.parametrize("pow", (0, None))
@pytest.mark.parametrize("other_pow", (0, None))
def test_constants_with_unequal_coeffs_are_not_equal(
    coeff, other_coeff, var, other_var, pow, other_pow
):
    term = Term(coeff=coeff, var=var, pow=pow)
    another_term = Term(coeff=other_coeff, var=other_var, pow=other_pow)

    assert term != another_term


@pytest.mark.parametrize("coeff", (0, 1, 2))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (0, None))
def test_differentiate_constant(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.differentiate() == Term(coeff=0, var=var, pow=None)


@pytest.mark.parametrize("coeff", (0, 1, 2))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (1,))
def test_term_is_axial_line_when_pow_is_one(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.is_axial_line()
    assert not term.is_constant()


@pytest.mark.parametrize("coeff", (1, 2, 3))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (1, 2, 3))
def test_differentiate(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.differentiate() == Term(coeff=coeff * pow, var=var, pow=pow - 1)


@pytest.mark.parametrize("coeff", (0, 1, 2))
@pytest.mark.parametrize("var", ("x", "y"))
@pytest.mark.parametrize("pow", (1,))
def test_axial_lines_differentiate_into_constants(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.differentiate().is_constant()
