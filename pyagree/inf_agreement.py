"""This file contains the implementation of the extension-by-continuity of
   Information Agreement.

.. moduleauthor:: Alberto Casagrande <acasagrande@units.it>

"""

from numpy import matrix

from .common import test_agreement_matrix, count_nonnull_rows
from .common import count_nonnull_cols
from .inf_theory import p_x, p_y, p_xy, entropy


def refine(values):
    r"""Remove 0 from a sequence of values

    Give an interable set of values, this function yields all
    the values in the sequence, but those that equal 0.

    :param values: An interable set of values
    :type values: An interable set of values
    :returns: An iterator over values without the instances of 0
    :rtype: Iterator
    """

    for value in values:
        if value != 0:
            yield value


def ia_eps(agreement_matrix):
    r"""Evaluate *extension-by-continuity of Information Agreement*

    Compute the :ref:`IAe_theory` (:math:`\text{IA}_{\epsilon}`) of
    agreement_matrix.

    :param agreement_matrix: An agreement matrix
    :type agreement_matrix: :class:`numpy.ndarray`
    :returns: The extension-by-continuity of Information Agreement of
              agreement_matrix
    :rtype: :class:`float`
    :raises: :class:`ValueError`
    """
    if isinstance(agreement_matrix, list):
        agreement_matrix = matrix(agreement_matrix)

    test_agreement_matrix(agreement_matrix)

    if agreement_matrix.shape[0] < 2:
        raise ValueError("The matrix has less than 2 rows and columns")

    h_xf = entropy(refine(p_x(agreement_matrix)))
    h_yf = entropy(refine(p_y(agreement_matrix)))

    if h_xf == 0:
        return (agreement_matrix.shape[0] -
                count_nonnull_rows(agreement_matrix))/agreement_matrix.shape[0]

    if h_yf == 0:
        return (agreement_matrix.shape[0] -
                count_nonnull_cols(agreement_matrix))/agreement_matrix.shape[0]

    h_xyf = entropy(refine(p_xy(agreement_matrix)))
    if h_xf < h_yf:
        return 1+(h_yf-h_xyf)/h_xf

    return 1+(h_xf-h_xyf)/h_yf
