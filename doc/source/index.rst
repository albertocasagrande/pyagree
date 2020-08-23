Welcome to `pyagree`'s documentation!
#####################################

*pyagree* is a simple Python module containing some of the main 
inter-rater agreement measures.


.. _installing_pyagree:

Installing `pyagree`
====================

.. toctree::

There are two main ways to install `pyagree`. The first one requires to clone 
`pyagree's repository from GitHub <https://github.com/albertocasagrande/pyagree>`_ by using the following command::

    git clone https://github.com/albertocasagrande/pyagree.git

Once the command has been completed, the repository directory must be entered 
and the package can be installed by issuing as administrator (root) the 
following commands::

    cd pyagree
    python setup.py install

The second method to install `pyagree` is easier, but requires the tool `pip` 
(see `pypi <https://pypi.org/project/pip/>`_) and it may install a 
non-bleeding edge version of the package. As administrator, issue the 
command::

    pip install pyagree


.. _using_pyagree:

Using `pyagree`
===============

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
		
For instance, the Python program::

    #!/usr/bin/env python

    from pyagree import YuleY, CohenKappa
	
    A = [[10,  1],
	 [ 5, 10]]

    Y = YuleY(A)
    K = CohenKappa(A)
	
    print('Yule = {}'.format(Y))
    print('Kappa = {}'.format(K))

evaluates both Yule's :math:`Y` and Cohen's :math:`\kappa` of 
the agreement matrix 

.. math::
   A = \left(\begin{array}{cc}
   10 & 1\\
   5 & 10\\
   \end{array}\right)
   
and print them in output.

.. _agreement_measures:

Agreement Measures
==================

.. toctree::

   measures

.. _API:

API
===

.. toctree::

   API

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
