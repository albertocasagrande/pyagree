.. _basic_notions:

General Notions
---------------

**Inter-rater agreement** (also known as **inter-rater 
reliability**) is a measure of consensus among :math:`n`  
raters in the classification of :math:`N` objects in 
a :math:`k` different categories. 

In the general case, the rater evalutations can be 
represented by the **reliability data matrix**: 
a :math:`n \times N`-matrix :math:`R` 
such that :math:`R[i,j]` stores the category 
selected by the :math:`i`-th rater for the 
:math:`j`-th object.


A more succint representation is provided by 
a :math:`N \times k`-matrix :math:`C` 
whose elements :math:`C[i,j]` account how many raters 
evaluated the :math:`i`-th object as belonging 
to the :math:`j`-th category. This matrix is the 
**classification matrix**.


Whenever the numer of raters is :math:`2`, i.e., 
:math:`n=2`, the rater evaluations can be 
represented by the **agreement matrix**: 
a :math:`k \times k`-matrix :math:`A` 
such that :math:`A[i,j]` stores the number 
of objects that are classified at the same 
time as belonging to the :math:`i`-th category 
by the first rater and to the 
:math:`j`-th category by the second rater.


.. _BennettS_theory:

Bennett, Alpert and Goldstein's S
---------------------------------

Bennett, Alpert and Goldstein's :math:`S` is an inter-rater agreement 
measure on nominal scale (see :cite:`bennettS` and :cite:`bennettS2`). 
It is defined as:
    
.. math::
   S \stackrel{\tiny\text{def}}{=} \frac { k * P_0 - 1 } { k - 1 }

where :math:`P_0` is the probability of agreement among the raters 
and :math:`k` is the number of different categories in the classification.


.. _BangdiwalaB_theory:

Bangdiwala's B
--------------

Bangdiwala's :math:`B` is an inter-rater agreement measure on nominal 
scale (see :cite:`BangdiwalaB`). It is defined as:
    
.. math::

   B \stackrel{\tiny\text{def}}{=} \frac{\sum_{i} A[i,i]}{\sum_{i} A_{i\cdot}*A_{\cdot{}i}}

where :math:`A_{i\cdot}` and :math:`A_{\cdot{}i}` are the sums of the elements in 
the :math:`i`-th row and :math:`i`-th column of the matrix :math:`A`, respectively.


.. _CohenKappa_theory:

Cohen's Kappa
-------------

Cohen's :math:`\kappa` is an inter-rater agreement measure on nominal 
scale (see :cite:`CohenK`). It is defined as:
    
.. math::

   \kappa \stackrel{\tiny\text{def}}{=} \frac{P_0-P_e}{1-P_e}

where :math:`P_0` is the probability of agreement among the raters 
and :math:`P_e` is the agreement probability by chance.


.. _ScottPi_theory:

Scott's Pi
----------

Scott's :math:`\pi` is an inter-rater agreement measure on nominal scale 
(see :cite:`ScottPi`). Similarly to Cohen's :math:`\kappa`, it is defined 
as:
    
.. math::

   \pi \stackrel{\tiny\text{def}}{=} \frac{P_0-P_e}{1-P_e}

where :math:`P_0` is the probability of agreement among the raters (as 
in Cohen's :math:`\kappa`) and :math:`P_e` is the sum of the squared joint 
proportions (whereas it is the sum of the squared geometric means of 
marginal proportions in Cohen's :math:`\kappa`). 
In particular, the *joint proportions* are the arithmetic means of the 
marginal proportions.


.. _YuleY_theory:

Yule's Y
--------

Yule's :math:`Y` (see :cite:`YuleY`), sometime called 
*coefficient of colligation*, measures the relation between two binary 
random variables (i.e., it can be computed exclusively on 
:math:`2 \times 2` agreement matrices). 
It is defined as:
    
.. math::

   Y \stackrel{\tiny\text{def}}{=} \frac{\sqrt{\text{OR}}-1}{\sqrt{\text{OR}}+1}

where :math:`\text{OR}` is the *odds ratio* (e.g., see `here <https://en.wikipedia.org/wiki/Odds_ratio>`_):
    
.. math::

   \text{OR} \stackrel{\tiny\text{def}}{=} \frac{A[0,0]*A[1,1]}{A[1,0]*A[0,1]}.


.. _FleissKappa_theory:

Fleiss's Kappa
--------------

Fleiss's :math:`\kappa` (see :cite:`fleissK`) is a multi-rater 
generalization of :ref:`ScottPi_theory`. 

If the classifications are represented in a classification matrix 
(see :ref:`basic_notions`), 
the ratio of classifications assigned to class :math:`j` is:

.. math::

   p_j \stackrel{\tiny\text{def}}{=} \frac{1}{N*n}\sum_{i=1}^{N} C[i,j]

and their square sum is:

.. math::

   \bar{P_e} \stackrel{\tiny\text{def}}{=}  \sum_{j=1}^k p_j.

Instead, the ratio between the pairs of raters which agree on the 
:math:`i`-th subject and the overall pairs of raters is:

.. math::

   P_i \stackrel{\tiny\text{def}}{=} \frac{1}{n*(n-1)}\left(\left(\sum_{j=1}^k C[i,j]^2\right) - n\right)
    
and its mean is:

.. math::
        
   \bar{P} \stackrel{\tiny\text{def}}{=} \frac{1}{N}\sum_{i=1}^{N}P_i.

Fleiss's :math:`\kappa` is defined as:

.. math::

   \kappa \stackrel{\tiny\text{def}}{=} \frac{\bar{P}-\bar{P_e}}{1-\bar{P_e}}.


.. _IA_theory:

Information Agreement
---------------------

The *Information Agreement*, (:math:`\text{IA}`), is an inter-rater 
agreement measure on nominal scale (see :cite:`IA2020`) which gauges the 
dependence between the classifications of two raters. 

The probability distributions for the evaluations of the rater 
:math:`\mathfrak{X}`, those of the rater :math:`\mathfrak{Y}`, and the 
joint evalutions :math:`\mathfrak{X}\mathfrak{Y}` on the 
agreement matrix :math:`A` are:

.. math::
   p_{X_{A}}(j_0) \stackrel{\tiny\text{def}}{=} 
   \frac{\sum_{i} A[i,j_0]}{\sum_{i}\sum_{j} A[i,j]}, 
   \quad\quad\quad
   p_{Y_{A}}(i_0) \stackrel{\tiny\text{def}}{=} 
   \frac{\sum_{j} A[i_0,j]}{\sum_{i}\sum_{j} A[i,j]}, 
   
and

.. math::
   p_{X_{A}Y_{A}}(i_0,j_0) = 
   \frac{A[i_0,j_0]}{\sum_{i}\sum_{i} A[i,j]}, 

respectively. The 
`entropy functions <https://en.wikipedia.org/wiki/Entropy_(information_theory)>`_ 
for the random variables 
:math:`X_{A}`, :math:`Y_{A}`, and 
:math:`X_{A}Y_{A}` are:

.. math::
   H(X_{A}) \stackrel{\tiny\text{def}}{=} 
   - \sum_{i} p_{X_{A}}(i) \log_2 p_{X_{A}}(i), 
   \quad\quad\quad
   H(Y_{A}) \stackrel{\tiny\text{def}}{=} 
   - \sum_{j} p_{Y_{A}}(j) \log_2 p_{Y_{A}}(j),
   
and

.. math::
   H(X_{A}Y_{A}) \stackrel{\tiny\text{def}}{=} 
   - \sum_{i}\sum_{j} p_{X_{A}Y_{A}}(i,j) 
   \log_2 p_{X_{A}Y_{A}}(i,j).


The `mutual information <https://en.wikipedia.org/wiki/Mutual_information>`_  
between the classification of 
:math:`\mathfrak{X}` and :math:`\mathfrak{Y}` is:

.. math::
   I(X_{A},Y_{A}) \stackrel{\tiny\text{def}}{=} 
   H(X_{A})+H(Y_{A})-H(X_{A}Y_{A}).
    
The *Information Agreement* of :math:`A` is the ratio between 
:math:`I(X_{A},Y_{A})` and 
the minimum among :math:`H(X_{A})` and :math:`H(Y_{A})`
as :math:`\epsilon` tends to :math:`0` from the right, i.e., 

.. math::
   \text{IA} \stackrel{\tiny\text{def}}{=} \frac{I(X_{A},Y_{A})} 
   { \min(H(X_{A}), H(Y_{A})) }.


.. _IAc_theory:

-----------------------------
Extension-by-Continuity of IA
-----------------------------

:math:`\text{IA}` was proven to be effetive in gauging agreement 
and solves some of the pitfalls of Cohen's :math:`\kappa`. 
However, it is not defined over all the agreement matrices and,  
in particular, it cannot be directly computed on agreement 
matrices containing some zeros (see :cite:`IAc2020`). 

The *extension-by-continuity of Information Agreement*, 
(:math:`\text{IA}_{C}`), extends :math:`\text{IA}`'s 
domain so that it can deal with matrices containing some zeros 
(see :cite:`IAc2020`). In order to achieve this goal, 
the considered agreement matrix :math:`A` is replaced by 
the symbolic matrix :math:`A_{\epsilon}` is defined as:

.. math::
   A_{\epsilon}[i,j] \stackrel{\tiny\text{def}}{=} \begin{cases}
   A[i,j] & \textrm{if $A[i,j]\neq 0$}\\
   \epsilon &   \textrm{if $A[i,j]=0$}
   \end{cases}

where :math:`\epsilon` is a real variable with values in 
the open interval :math:`(0, +\infty)`. On this matrix, 
mutual information of the variables :math:`X_{A_{\epsilon}}` 
and :math:`Y_{A_{\epsilon}}` and their entropy functions 
are defined. 
The *extension-by-continuity of Information Agreement* 
of :math:`A` is the limit of the ratio 
between :math:`I(X_{A_{\epsilon}},Y_{A_{\epsilon}})` and 
the minimum among :math:`H(X_{A_{\epsilon}})` 
and :math:`H(Y_{A_{\epsilon}})` as :math:`\epsilon` tends 
to :math:`0` from the right, i.e., 

.. math::
   \text{IA}_{C}(A) \stackrel{\tiny\text{def}}{=}  
   \lim_{\epsilon \rightarrow 0^+} 
   \frac{I(X_{A_{\epsilon}},Y_{A_{\epsilon}})} 
   { \min(H(X_{A_{\epsilon}}), H(Y_{A_{\epsilon}})) }.


:math:`\text{IA}_{C}(A)` was proven to be defined 
over any non-null agreement matrix having more than one 
row/column and, if :math:`l` and :math:`m` are numbers of 
non-null columns and non-null rows in :math:`A`, 
respectively, then:

.. math::
   \text{IA}_{C}(A) = \begin{cases}
   1-\frac{m}{k} & \text{if $H(\overline{X_{A}})=0$}\\
   1-\frac{l}{k} & \text{if $H(\overline{Y_{A}})=0$}\\
   \frac{I(\overline{X_{A}},\overline{Y_{A}})} 
   { \min\left(H\left(\overline{X_{A}}\right), 
   H\left(\overline{Y_{A}}\right)\right) }&\text{otherwise}
   \end{cases}

where :math:`\overline{X_{A}}`, :math:`\overline{Y_{A}}`, 
and :math:`\overline{X_{A}Y_{A}}` are three random 
variables having the same probability distributions of 
:math:`{X_{A}}`, :math:`{Y_{A}}`, and :math:`{X_{A}Y_{A}}` 
except for :math:`0`-probability events which are removed 
from their domains (see :cite:`IAc2020`).

References
----------

.. bibliography:: refs.bib


