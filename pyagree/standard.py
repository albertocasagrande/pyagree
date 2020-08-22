from .common import colSum_iter, rowSum_iter, item_iter
from numpy import multiply, matrix
from math import sqrt


def BennettS(A):
    r"""Evaluate Bennett, Alpert and Goldstein's :math:`S` 

    Compute the :ref:`BennettS_theory` of an agreement matrix A.

    :param A: An :math:`n \times n`-agreement matrix 
    :type A:  numpy.ndarray
    
    :returns: The Bennett, Alpert and Goldstein's :math:`S` of A
    :rtype: float 
    """
    
    if isinstance(A,list):
    	A = matrix(A)

    if A.shape[0]!=A.shape[1]:
        raise ValueError("This method exclusively supports nxn-matrices")

    k = A.shape[0]

    Pa = sum(A[i,i] for i in range(k))/A.sum()

    return (k*Pa-1)/(k-1) 


def BangdiwalaB(A):
    r"""Evaluate Bangdiwala's :math:`B` 

    Compute the :ref:`BangdiwalaB_theory` of an agreement matrix A.

    :param A: An :math:`n \times n`-agreement matrix 
    :type A:  numpy.ndarray
    
    :returns: The Bangdiwala's :math:`B` of A
    :rtype: float
    """

    if isinstance(A,list):
    	A = matrix(A)

    if A.shape[0]!=A.shape[1]:
        raise ValueError("This method exclusively supports nxn-matrices")

    k = A.shape[0]
  
    Pa = sum(A[i,i]**2 for i in range(k))
    
    Pe = sum(A[i,:].sum()*A[:,i].sum() for i in range(k))

    return Pa/Pe


def CohenKappa(A):
    r"""Evaluate Cohen's :math:`\kappa` 

    Compute :ref:`CohenKappa_theory` of an agreement matrix A.

    :param A: An :math:`n \times n`-agreement matrix 
    :type A:  numpy.ndarray
    
    :returns: The Cohen's :math:`\kappa` of A
    :rtype: float 
    """

    if isinstance(A,list):
    	A = matrix(A)

    if A.shape[0]!=A.shape[1]:
        raise ValueError("This method exclusively supports nxn-matrices")

    k = A.shape[0]

    S_A = A.sum()

    Pa = sum(A[i,i] for i in range(k))/S_A
    
    Pe = sum(A[i,:].sum()*A[:,i].sum() for i in range(k))/(S_A**2)

    return (Pa-Pe)/(1-Pe)


def ScottPi(A):
    r"""Evaluate Scott's :math:`\pi` 

    Compute the :ref:`ScottPi_theory` of an agreement matrix A.

    :param A: An :math:`n \times n`-agreement matrix 
    :type A:  numpy.ndarray
    
    :returns: The Scott's :math:`\pi` of A
    :rtype: float
    """
    
    if isinstance(A,list):
    	A = matrix(A)
    	
    if A.shape[0]!=A.shape[1]:
        raise ValueError("This method exclusively supports nxn-matrices")

    S_A2 = 2*A.sum()
    
    Pe = sum(((A[i,:].sum()+A[:,i].sum())/S_A2)**2
             for i in range(A.shape[0]))
    Pa = 2*sum(A[i,i] for i in range(A.shape[0]))/S_A2

    return (Pa-Pe)/(1-Pe)


def YuleY(A):
    r"""Evaluate Yule's :math:`Y` 

    Compute the :ref:`YuleY_theory` of a :math:`2 \times 2`-agreement 
    matrix A.

    :param A: A :math:`2 \times 2`-agreement matrix 
    :type A:  numpy.ndarray
    
    :returns: The Yule :math:`Y` of A
    :rtype: float
    """
    
    if isinstance(A,list):
    	A = matrix(A)
    	
    if A.shape[0]!=A.shape[1] or A.shape[0]!=2:
        raise ValueError("This method exclusively supports 2x2-matrices")

    odd_r = 1
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i==j:
                odd_r *= A[i,j]
            else:
                odd_r /= A[i,j]

    sqrt_odd_r = sqrt(odd_r)
    
    return (sqrt_odd_r-1)/(sqrt_odd_r+1)
    

def FleissKappa(C):
    r"""Evaluate Fleiss's :math:`\kappa` 

    Compute the :ref:`FleissKappa_theory` of 
    a classification matrix C.

    :param C: An :math:`N \times k`-classification matrix
    :type C:  numpy.ndarray
    
    :returns: The Fleiss's :math:`\kappa` of C
    :rtype: float
    """
    
    if isinstance(C,list):
    	A = matrix(C)
    	
    N = C.shape[0]
    k = C.shape[1]
    n = C[0,:].sum()

    Nn = N*n
    
    P0 = (multiply(C,C).sum()-Nn)/(Nn*(n-1))

    p = [C[:,j].sum()/Nn for j in range(k)]

    Pe = sum(p[j]**2 for j in range(k))

    return (P0-Pe)/(1-Pe)
    
 

