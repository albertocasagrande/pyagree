from math import log

from .common import test_agreement_matrix, countNNRows, countNNCols
from .IT import pX, pY, pXY, entropy
from numpy import matrix


def refine(values):
    for v in values:
        if v!=0:
            yield v


def IAeps(A):
    r"""Evaluate *extension-by-continuity of Information Agreement* (:math:`\text{IA}_{\epsilon}`)

    Compute the :ref:`IAe_theory` (:math:`\text{IA}_{\epsilon}`) of 
    an agreement matrix C.


    :param A: An agreement matrix 
    :type A: :class:`numpy.ndarray`	
    :returns: The extension-by-continuity of Information Agreement of A
    :rtype: :class:`float`
    :raises: :class:`ValueError`
    """
    if isinstance(A,list):
    	A = matrix(A)

    test_agreement_matrix(A)
	
    if A.shape[0]<2:
        raise ValueError("The matrix has less than 2 rows and columns")

    H_Xf = entropy(refine(pX(A)))
    H_Yf = entropy(refine(pY(A)))
 
    if H_Xf==0:
        return (A.shape[0]-countNNRows(A))/A.shape[0]
 		
    if H_Yf==0:
        return (A.shape[0]-countNNCols(A))/A.shape[0]
    
    H_XYf = entropy(refine(pXY(A)))
    if H_Xf < H_Yf:
        return 1+(H_Yf-H_XYf)/H_Xf
    
    return 1+(H_Xf-H_XYf)/H_Yf

