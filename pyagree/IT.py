from math import log

from .common import colSum_iter, rowSum_iter, item_iter


def pX(A):
    r"""Evaluate the probability distribution of the columns of an agreement matrix

    Iterate over the probabilities of the columns of an agreement matrix , i.e., the 
    sequence :math:`(pX_0, \ldots, pX_n)` where:
    
    .. math::
    
       pX_{k} \stackrel{\tiny\text{def}}{=} \frac{\sum_{i} A[i][k]}{\sum_{i} \sum_{j} A[i][j]}

    :param A: An agreement matrix 
    :type A:  numpy.ndarray	
    :returns: An iterator over the probabilities of the columns of A
    :rtype: Iterator[:class:`float`]
    """

    SA = A.sum()
    
    for s_col in colSum_iter(A):
        yield s_col/SA


def pY(A):
    r"""Evaluate the probability distribution of the rows of an agreement matrix

    Iterate over the probabilities of the rows of an agreement matrix , i.e., the 
    sequence :math:`(pY_0, \ldots, pY_n)` where:
    
    .. math::
    
       pY_{k} \stackrel{\tiny\text{def}}{=} \frac{\sum_{j} A[k][j]}{\sum_{i} \sum_{j} A[i][j]}

    :param A: An agreement matrix 
    :type A:  numpy.ndarray	
    :returns: An iterator over the probabilities of the rows of A
    :rtype: Iterator[:class:`float`]
    """

    SA = A.sum()
    
    for s_row in rowSum_iter(A):
        yield s_row/SA


def pXY(A):
    r"""Evaluate the probability distribution of the elements of an agreement matrix

    Iterate over the probabilities of the elements of an agreement matrix , i.e., the 
    sequence :math:`(pXY_{0,0}, \ldots, pXY_{0,n}, pXY_{1,0},\ldots, pXY_{1,n},\ldots, pXY_{n,n})` where:
    
    .. math::
    
       pXY_{k,h} \stackrel{\tiny\text{def}}{=} \frac{A[k][h]}{\sum_{i} \sum_{j} A[i][j]}

    :param A: An agreement matrix 
    :type A:  numpy.ndarray	
    :returns: An iterator over the probabilities of the elements of A
    :rtype: Iterator[:class:`float`]
    """

    SA = A.sum()
    
    for y in range(A.shape[0]):
        for x in range(A.shape[1]):
            yield (A[y,x]/SA)


def entropy(I):
    r"""Evaluate the entropy of an iterable

    Compute the `entropy <https://en.wikipedia.org/wiki/Entropy_(information_theory)>`_  
    of an iterable I of floating point numbers, i.e., 
    
    .. math::
    
       H(\text{I}) \stackrel{\tiny\text{def}}{=} -\sum_{v \in \text{I}} v*\log_2{v}

    :param I: An iterable object of floating point numbers
    :type I:  Iterable object of :class:`float`
    :returns: Compute the entropy of I
    :rtype: :class:`float`
    """

    return -sum(v*log(v,2) for v in I)

