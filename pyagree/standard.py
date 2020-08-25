"""This file contains the implementation of the standard agreement measures.

.. moduleauthor:: Alberto Casagrande <acasagrande@units.it>

"""

from math import sqrt

from numpy import multiply, matrix
from numpy import any as np_any

from .common import test_agreement_matrix


def bennett_s(agreement_matrix):
    r"""Evaluate Bennett, Alpert and Goldstein's :math:`S`

    Compute the :ref:`BennettS_theory` of agreement_matrix.

    :param agreement_matrix: An :math:`n \times n`-agreement matrix
    :type agreement_matrix: :class:`numpy.ndarray`
    :returns: The Bennett, Alpert and Goldstein's :math:`S` of agreement_matrix
    :rtype: :class:`float`
    :raises: :class:`ValueError`
    """

    if isinstance(agreement_matrix, list):
        agreement_matrix = matrix(agreement_matrix)

    test_agreement_matrix(agreement_matrix)

    if agreement_matrix.shape[0] < 2:
        raise ValueError("The matrix has less than 2 rows and columns")

    k = agreement_matrix.shape[0]

    p_a = sum(agreement_matrix[i, i] for i in range(k))/agreement_matrix.sum()

    return (k*p_a-1)/(k-1)


def bangdiwala_b(agreement_matrix):
    r"""Evaluate Bangdiwala's :math:`B`

    Compute the :ref:`BangdiwalaB_theory` of agreement_matrix.

    :param agreement_matrix: An :math:`n \times n`-agreement matrix
    :type agreement_matrix: :class:`numpy.ndarray`
    :returns: The Bangdiwala's :math:`B` of agreement_matrix
    :rtype: :class:`float`
    :raises: :class:`ValueError`
    """

    if isinstance(agreement_matrix, list):
        agreement_matrix = matrix(agreement_matrix)

    test_agreement_matrix(agreement_matrix)

    k = agreement_matrix.shape[0]

    p_a = sum(agreement_matrix[i, i]**2 for i in range(k))

    p_e = sum(agreement_matrix[i, :].sum()*agreement_matrix[:, i].sum()
              for i in range(k))

    if p_e == 0:
        raise ValueError("This matrix is out of the domain of Bangdiwala's B")

    return p_a/p_e


def cohen_kappa(agreement_matrix):
    r"""Evaluate Cohen's :math:`\kappa`

    Compute :ref:`CohenKappa_theory` of agreement_matrix.

    :param agreement_matrix: An :math:`n \times n`-agreement matrix
    :type agreement_matrix: :class:`numpy.ndarray`
    :returns: The Cohen's :math:`\kappa` of agreement_matrix
    :rtype: :class:`float`
    :raises: :class:`ValueError`
    """

    if isinstance(agreement_matrix, list):
        agreement_matrix = matrix(agreement_matrix)

    test_agreement_matrix(agreement_matrix)

    k = agreement_matrix.shape[0]

    sum_am = agreement_matrix.sum()

    p_a = sum(agreement_matrix[i, i] for i in range(k))/sum_am

    p_e = sum(agreement_matrix[i, :].sum()*agreement_matrix[:, i].sum()
              for i in range(k))/(sum_am**2)

    if p_e == 1:
        raise ValueError("The agreement probability by chance of the " +
                         "matrix is 1")

    return (p_a-p_e)/(1-p_e)


def scott_pi(agreement_matrix):
    r"""Evaluate Scott's :math:`\pi`

    Compute the :ref:`ScottPi_theory` of agreement_matrix.

    :param agreement_matrix: An :math:`n \times n`-agreement matrix
    :type agreement_matrix: :class:`numpy.ndarray`

    :returns: The Scott's :math:`\pi` of agreement_matrix
    :rtype: :class:`float`
    :raises: :class:`ValueError`
    """

    if isinstance(agreement_matrix, list):
        agreement_matrix = matrix(agreement_matrix)

    test_agreement_matrix(agreement_matrix)

    sum_am2 = 2*agreement_matrix.sum()
    p_e = sum(((agreement_matrix[i, :].sum() +
                agreement_matrix[:, i].sum()) / sum_am2)**2
              for i in range(agreement_matrix.shape[0]))
    p_a = 2*sum(agreement_matrix[i, i]
                for i in range(agreement_matrix.shape[0]))/sum_am2

    if p_e == 1:
        raise ValueError("The sum of the squared joint proportions of " +
                         "the matrix is 1")

    return (p_a-p_e)/(1-p_e)


def yule_y(agreement_matrix):
    r"""Evaluate Yule's :math:`Y`

    Compute the :ref:`YuleY_theory` of a :math:`2 \times 2`-agreement
    matrix agreement_matrix.

    :param agreement_matrix: A :math:`2 \times 2`-agreement matrix
    :type agreement_matrix: :class:`numpy.ndarray`

    :returns: The Yule :math:`Y` of agreement_matrix
    :rtype: :class:`float`
    :raises: :class:`ValueError`
    """

    if isinstance(agreement_matrix, list):
        agreement_matrix = matrix(agreement_matrix)

    test_agreement_matrix(agreement_matrix)

    if agreement_matrix.shape[0] != 2:
        raise ValueError("The agreement matrix must be a 2x2-matrix")

    odd_r = 1
    for i in range(agreement_matrix.shape[0]):
        for j in range(agreement_matrix.shape[1]):
            if i == j:
                odd_r *= agreement_matrix[i, j]
            else:
                if agreement_matrix[i, j] == 0:
                    raise ValueError("Some elements outside the main " +
                                     "diagonal are 0")
                odd_r /= agreement_matrix[i, j]

    sqrt_odd_r = sqrt(odd_r)

    return (sqrt_odd_r-1)/(sqrt_odd_r+1)


def fleiss_kappa(classification_matrix):
    r"""Evaluate Fleiss's :math:`\kappa`

    Compute the :ref:`FleissKappa_theory` of a classification
    matrix classification_matrix.

    :param classification_matrix: An :math:`N \times k`-classification matrix
    :type classification_matrix: class:`numpy.ndarray`

    :returns: The Fleiss's :math:`\kappa` of classification_matrix
    :rtype: :class:`float`
    :raises: :class:`ValueError`
    """

    if isinstance(classification_matrix, list):
        classification_matrix = matrix(classification_matrix)

    if np_any(classification_matrix < 0):
        raise ValueError("The matrix contains some negative values")

    dataset_size = classification_matrix.shape[0]
    num_of_classes = classification_matrix.shape[1]
    num_of_raters = classification_matrix[0, :].sum()

    d_n = dataset_size*num_of_raters

    p_0 = (multiply(classification_matrix,
                    classification_matrix).sum()-d_n)/(d_n*(num_of_raters-1))

    p_e = sum((classification_matrix[:, j].sum()/d_n)**2
              for j in range(num_of_classes))

    return (p_0-p_e)/(1-p_e)
