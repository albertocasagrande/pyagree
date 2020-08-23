from math import log

from .common import countNNRows, countNNCols
from .IT import pX, pY, pXY, entropy


def refine(values):
    for v in values:
        if v!=0:
            yield v


def IAeps(A):
    r"""Evaluate *extension-by-continuity of Information Agreement* (:math:`\text{IA}_{\epsilon}`)

    Compute the :ref:`IAe_theory` (:math:`\text{IA}_{\epsilon}`) of 
    an agreement matrix C.


    :param A: An agreement matrix 
    :type A:  numpy.ndarray	
    :returns: The extension-by-continuity of Information Agreement of A
    :rtype: float 
    """
    if isinstance(A,list):
    	A = matrix(A)
    	
    if A.shape[0]!=A.shape[1] or A.shape[0]<2:
        raise ValueError("This method exclusively supports nxn-matrices where n>1")
        
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
