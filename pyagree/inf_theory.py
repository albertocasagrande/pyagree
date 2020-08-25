"""This file contains the implementation of some information-theoretic
   functions.

.. moduleauthor:: Alberto Casagrande <acasagrande@units.it>

"""

from math import log

from .common import col_sums_iter, row_sums_iter


def p_x(matrix):
    r"""Evaluate the probability distribution of the columns of a matrix

    Iterate over the probabilities of the columns of a matrix, i.e., the
    sequence :math:`(pX_0, \ldots, pX_n)` where:

    .. math::

       pX_{k} \stackrel{\tiny\text{def}}{=} \frac{\sum_{i} A[i][k]}{
           \sum_{i} \sum_{j} A[i][j]}

    :param matrix: A matrix
    :type matrix: :class:`numpy.ndarray`
    :returns: An iterator over the probabilities of the columns of matrix
    :rtype: Iterator[:class:`float`]
    """

    sum_m = matrix.sum()

    for s_col in col_sums_iter(matrix):
        yield s_col/sum_m


def p_y(matrix):
    r"""Evaluate the probability distribution of the rows of a matrix

    Iterate over the probabilities of the rows of a matrix, i.e., the
    sequence :math:`(pY_0, \ldots, pY_n)` where:

    .. math::

       pY_{k} \stackrel{\tiny\text{def}}{=} \frac{\sum_{j} A[k][j]}{
           \sum_{i} \sum_{j} A[i][j]}

    :param matrix: A matrix
    :type matrix: :class:`numpy.ndarray`
    :returns: An iterator over the probabilities of the rows of matrix
    :rtype: Iterator[:class:`float`]
    """

    sum_m = matrix.sum()

    for s_row in row_sums_iter(matrix):
        yield s_row/sum_m


def p_xy(matrix):
    r"""Evaluate the probability distribution of the elements of a matrix

    Iterate over the probabilities of the elements of a matrix, i.e., the
    sequence
    :math:`(pXY_{0,0},\ldots,pXY_{0,n},pXY_{1,0},\ldots,pXY_{1,n},\ldots,
    pXY_{n,n})` where:

    .. math::

       pXY_{k,h} \stackrel{\tiny\text{def}}{=} \frac{A[k][h]}{
           \sum_{i} \sum_{j} A[i][j]}

    :param matrix: A matrix
    :type matrix: :class:`numpy.ndarray`
    :returns: An iterator over the probabilities of the elements of matrix
    :rtype: Iterator[:class:`float`]
    """

    sum_m = matrix.sum()

    for row_idx in range(matrix.shape[0]):
        for col_idx in range(matrix.shape[1]):
            yield matrix[row_idx, col_idx]/sum_m


def entropy(values):
    r"""Evaluate the entropy of an iterable

    Compute the
    `entropy <https://en.wikipedia.org/wiki/Entropy_(information_theory)>`_
    of an iterable I of floating point numbers, i.e.,

    .. math::

       H(\text{I}) \stackrel{\tiny\text{def}}{=}
       -\sum_{v \in \text{I}} v*\log_2{v}

    :param values: An iterable object of floating point numbers
    :type values:  Iterable object of :class:`float`
    :returns: Compute the entropy of values
    :rtype: :class:`float`
    """

    return -sum(value*log(value, 2) for value in values)
