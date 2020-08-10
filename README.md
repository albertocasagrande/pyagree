# pyagree
A simple Python module to compute some inter-rater agreement measures. Among the other measures this package provides an implementation for both the _Information Agreement_ and the _Information Agreement*_ coefficients (see [[1]](#information_agreement)).

## Installation
In order to install the `pyagree` module, execute the following command as administrator (root):

```bash
python setup.py install 
```

Alternatively, this module can be installed by using PyPi as follows:
```bash
pip install pyagree
```

## Usage
```python
import numpy
import pyagree


A = numpy.matrix([[12, 1],
                  [0, 37]])
                  
                  
pyagree.IAstar(A)

```


## References 

<a id="information_agreement">[1]</a> 
Casagrande, A. and Fabris, F. and 
Girometti R. (2020). 
Beyond Kappa: An Informational Index for
Diagnostic Agreement in Dichotomous and
Multivalue Ordered-Categorical Ratings, _Submitted for the publication_.
