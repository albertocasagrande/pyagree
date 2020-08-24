"""This file contains all the functions which are commonly required by
   agreement measures.

.. moduleauthor:: Alberto Casagrande <acasagrande@units.it>

"""

from numpy import any as np_any
from numpy import all as np_all


def count_nonnull_rows(matrix):
    r"""Evaluate the number of non-null rows in a matrix.

    Compute the number of non-null rows in matrix.

    :param matrix: A matrix
    :type matrix: :class:`numpy.ndarray`
    :returns: The number of non-null rows in matrix
    :rtype: :class:`int`
    """
    return sum(1 for row in matrix if not np_any(row))


def count_nonnull_cols(matrix):
    r"""Evaluate the number of non-null columns in a matrix.

    Compute the number of non-null columns in matrix.

    :param matrix: A matrix
    :type matrix: :class:`numpy.ndarray`
    :returns: The number of non-null columns in matrix
    :rtype: :class:`int`
    """
    return sum(1 for col in matrix.T if not np_any(col))


def col_sums_iter(matrix):
    r"""Evaluate the sums of values in each column of a matrix

    Iterate over the sums of values in each column of a matrix, i.e.,
    the sequence :math:`(s_0, \ldots, s_m)` where:

    .. math::

       s_{k} \stackrel{\tiny\text{def}}{=} \sum_{i} A[i][k]

    :param matrix: A matrix
    :type matrix: :class:`numpy.ndarray`
    :returns: An iterator over sums of values in each column of matrix
    :rtype: Iterator
    """
    for col in matrix.T:
        yield col.sum()


def row_sums_iter(matrix):
    r"""Evaluate the sums of values in each row of a matrix

    Iterate over the sums of values in each row of a matrix, i.e.,
    the sequence :math:`(s_0, \ldots, s_n)` where:

    .. math::

       s_{k} \stackrel{\tiny\text{def}}{=} \sum_{j} A[k][j]

    :param matrix: A matrix
    :type matrix: :class:`numpy.ndarray`
    :returns: An iterator over sums of values in each row of matrix
    :rtype: Iterator
    """
    for row in matrix:
        yield row.sum()


def item_iter(matrix):
    r"""Iterate over values of a matrix

    Iterate row-wise over values of a matrix, i.e., the sequence
    :math:`(\text{matrix}[0][0],\ldots,\text{matrix}[0][n],
    \text{matrix}[1][0],\ldots,\text{matrix}[1][n],\ldots,
    \text{matrix}[m][n])`.

    :param matrix: A matrix
    :type matrix: :class:`numpy.ndarray`
    :returns: An iterator over values of matrix row-wise
    :rtype: Iterator
    """
    for row in matrix:
        for elem in row:
            yield elem


def test_agreement_matrix(matrix):
    r"""Test whether a matrix is an agreement matrix

    Test whether a matrix is a square-matrix, contains some negative
    values, or all its elements equal 0, i.e., if matrix is not
    an agreement matrix. In such cases, raise an opportune
    :class:`ValueError`.

    :param matrix: A matrix
    :type matrix: :class:`numpy.ndarray`
    :raises: :class:`ValueError`
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Non-squared matrix")

    if np_any(matrix < 0):
        raise ValueError("The matrix contains some negative values")

    if np_all(matrix == 0):
        raise ValueError("The matrix is null")
