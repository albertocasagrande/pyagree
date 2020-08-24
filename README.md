# pyagree
A simple Python package to compute some inter-rater agreement measures. Among the other measures this package provides an implementation for both the _Information Agreement_ and the _extension-by-continuity of Information Agreement_ coefficients (see [[1]](#information_agreement)).



## Documentation

[Here](https://pyagree.readthedocs.io/) you can find the *pyagree* documentation. It contains:

- the instruction to install the package
- the user manual and some examples
- the API manual



## Examples

In order to use `pyagree`, it is sufficient to import it, for instance, 
by using the statement

```python
import pyagree
```

After that, all the functions reported can be invoked as follows:

```python
pyagree.<function name>(<parameter1>, ...)
```

Alternatively, the desired functions can be individually imported 
and avoiding the package name prefix as in:

```python
from pyagree import <function name>

<function name>(<parameter1>, ...)
```

For instance, the Python program:

```python
from pyagree import yule_y, cohen_kappa
	
A = [[10,  1],
     [ 5, 10]]
	
Y = yule_y(A)
K = cohen_kappa(A)
	
print("Yule's Y = {}".format(Y))
print("Cohen's Kappa = {}".format(K))
```

evaluates both Yule's Y and Cohen's kappa of  the agreement matrix A and print them in output.



## References 

<a id="information_agreement">[1]</a>  Casagrande, A. and Fabris, F. and Girometti R. (2020).  Beyond Kappa: An Informational Index for
Diagnostic Agreement in Dichotomous and Multivalue Ordered-Categorical Ratings, _Submitted for the publication_.



## Copyright and license

*pyagree* Copyright (C) 2020 Alberto Casagrande [acasagrande@units.it](mailto:acasagrande@units.it)

Copyright (c) 2020 Alberto Casagrande

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
