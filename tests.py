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
    assert not term.is_axis()


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
def test_term_is_axis_when_pow_is_one(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.is_axis()
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
def test_axiss_differentiate_into_constants(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.differentiate().is_constant()


@pytest.mark.parametrize("coeff", (0,))
@pytest.mark.parametrize("var", ("x", "y", "z"))
@pytest.mark.parametrize("pow", (1, 2, 3))
def test_string_representation_of_term_with_coeff_zero(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert str(term) == "0"


@pytest.mark.parametrize("coeff", (1, 2, 3, 4))
@pytest.mark.parametrize("var", ("x", "y", "z"))
@pytest.mark.parametrize("pow", (0, None))
def test_string_representation_of_constant(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.is_constant()
    assert str(term) == str(coeff)


@pytest.mark.parametrize("coeff", (1,))
@pytest.mark.parametrize("var", ("x", "y", "z"))
@pytest.mark.parametrize("pow", (1,))
def test_string_representation_of_unscaled_axis(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.is_axis()
    assert str(term) == var


@pytest.mark.parametrize("coeff", (2, 3, 4))
@pytest.mark.parametrize("var", ("x", "y", "z"))
@pytest.mark.parametrize("pow", (1,))
def test_string_representation_of_scaled_axis(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert term.is_axis()
    assert str(term) == str(coeff) + var


@pytest.mark.parametrize("coeff", (1,))
@pytest.mark.parametrize("var", ("x", "y", "z"))
@pytest.mark.parametrize("pow", (2, 3, 4))
def test_string_representation_x_pow_n(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert str(term) == var + "^" + str(pow)


@pytest.mark.parametrize("coeff", (2, 3, 4))
@pytest.mark.parametrize("var", ("x", "y", "z"))
@pytest.mark.parametrize("pow", (2, 3, 4))
def test_string_representation(coeff, var, pow):
    term = Term(coeff=coeff, var=var, pow=pow)

    assert str(term) == str(coeff) + var + "^" + str(pow)
