from math import log

from .common import colSum_iter, rowSum_iter, item_iter


def pX(A):
    r"""Evaluate the probability distribution of the columns of an agreement matrix

    Compute the probability distribution of the columns of an agreement matrix, i.e., 
    
    .. math::
    
       pX(i) = 

    :param A: An agreement matrix 
    :type A:  numpy.ndarray	
    :returns: The probability distribution of the columns of A
    :rtype: float 
    """

    SA = A.sum()
    
    for s_col in colSum_iter(A):
        yield s_col/SA


def pY(A):
    SA = A.sum()
    
    for s_row in rowSum_iter(A):
        yield s_row/SA


def pXY(A):
    SA = A.sum()
    
    for y in range(A.shape[0]):
        for x in range(A.shape[1]):
            yield (A[y,x]/SA)


def entropy(values):
    return -sum(v*log(v,2) for v in values)

