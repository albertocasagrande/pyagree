.. _using_pyagree:

Importing `pyagree` Functions
-----------------------------

.. toctree::

In order to use `pyagree`, it is sufficient to import it, for instance, 
by using the statement::
    
    import pyagree

After that, all the functions reported in the :ref:`API <pyagree_API>` 
can be invoked as follows::

    pyagree.<function name>(<parameter1>, ...)

Alternatively, the desired functions can be individually imported 
and avoiding the package name prefix as in::
	
    from pyagree import <function name>

    <function name>(<parameter1>, ...)

.. _usage_examples:

Working Examples
----------------

For instance::

    >>> from pyagree import BangdiwalaB, CohenKappa

    >>> A = [[10,  1],
    ...      [ 5, 10]]

    >>> BangdiwalaB(A)

    0.6060606060606061

    >>> CohenKappa(A)

    0.5491329479768786

evaluates both Bangdiwala's :math:`B` and Cohen's :math:`\kappa` of 
the agreement matrix 

.. math::
   A = \left(\begin{array}{cc}
   10 & 1\\
   5 & 10\\
   \end{array}\right)
   
and print them in output. 

-------------
NumPy Support
-------------

.. _numpy_support:

All the `pyagree` functions natively support both standard "list-of-list"  
representation of matrices and `NumPy <https://numpy.org/>`_ matrices.

.. code:: python

    >>> import numpy
    >>> from pyagree import ScottPi

    >>> A = [[0,1,2],
    ...      [3,4,5],
    ...      [6,7,8]]

    >>> B = numpy.matrix(A)

    >>> ScottPi(A)

	-0.09090909090909094

    >>> ScottPi(B)

    -0.09090909090909094


.. _value_errors:

---------------------------
Matrix Sizes and Exceptions
---------------------------

Whenever, the matrix size is not supported either by the agreement measure 
or by the corresponding `pyagree` function, an opportune `ValueError` is 
raised.

.. code:: python

    >>> from pyagree import CohenKappa, YuleY
    
    >>> A = [[0,1],
    ...      [2,3],
    ...      [4,5]]
    
    >>> B = [[0,1,2],
    ...      [3,4,5],
    ...      [6,7,8]]
    
    >>> C = [[0,1],
    ...      [2,3]]
    
    >>> CohenKappa(A)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/lib/python3.8/site-packages/pyagree/standard.py", line 81, in CohenKappa
        test_agreement_matrix(A)
      File "/usr/lib/python3.8/site-packages/pyagree/common.py", line 29, in test_agreement_matrix
        raise ValueError("Non-squared matrix")
    ValueError: Non-squared matrix

    >>> CohenKappa(B)
	
    -0.0666666666666667
	
    >>> YuleY(B)
	
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/lib/python3.8/site-packages/pyagree/standard.py", line 149, in YuleY
        raise ValueError("The agreement matrix must be a 2x2-matrix")
    ValueError: The agreement matrix must be a 2x2-matrix

    >>> YuleY(C)
	
    -1.0

