"""A simple Python package to compute some inter-rater agreement measures.

.. moduleauthor:: Alberto Casagrande <acasagrande@units.it>

"""

__author__ = "Alberto Casagrande"
__copyright__ = "Copyright 2020"
__credits__ = ["Alberto Casagrande"]
__license__ = "MIT"
__release__ = "0.0"
__subrelease__ = "3"
__version__ = __release__+"."+__subrelease__
__maintainer__ = "Alberto Casagrande"
__email__ = "acasagrande@units.it"
__status__ = "Development"

from .inf_agreement import *
from .standard import *

NAME = "pyagree"
