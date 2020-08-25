r"""This file contains the tests for the `pyagree` package.

.. moduleauthor:: Alberto Casagrande <acasagrande@units.it>

"""

import unittest

from numpy import array

from pyagree import fleiss_kappa, yule_y, bangdiwala_b, bennett_s
from pyagree import cohen_kappa, scott_pi, ia_eps


class TestFleissKappa(unittest.TestCase):
    r"""This class implements the tests for Fleiss's Kappa
    """

    def setUp(self):
        """Setup the tests
        """
        self.tests = [(array([[0, 0, 0, 0, 14],
                              [0, 2, 6, 4, 2],
                              [0, 0, 3, 5, 6],
                              [0, 3, 9, 2, 0],
                              [2, 2, 8, 1, 1],
                              [7, 7, 0, 0, 0],
                              [3, 2, 6, 3, 0],
                              [2, 5, 3, 2, 2],
                              [6, 5, 2, 1, 0],
                              [0, 2, 2, 3, 7]]),
                       0.20993070442195522)]
        self.errors = []

    def test_fleiss_kappa(self):
        """Measure evaluations
        """
        for matrix, res in self.tests:
            self.assertAlmostEqual(fleiss_kappa(matrix),
                                   res, places=7)

    def test_fleiss_kappa_domain(self):
        """Test out-of-domain matrices
        """
        for matrix, err_type in self.errors:
            with self.assertRaises(err_type):
                fleiss_kappa(matrix)


class TestYuleY(unittest.TestCase):
    r"""This class implements the tests for Yule's Y
    """

    def setUp(self):
        """Setup the tests
        """
        self.tests = [(array([[3600, 2595],
                              [65, 3740]]),
                       0.7986777938427015),
                      (array([[9901, 64],
                              [2, 33]]),
                       0.961182593583485),
                      (array([[9900, 86],
                              [1, 13]]),
                       0.9496028357716024),
                      (array([[21, 5],
                              [3, 21]]),
                       0.6885791067119448),
                      (array([[40, 5],
                              [3, 2]]),
                       0.3956610414960755),
                      (array([[40, 2],
                              [3, 5]]),
                       0.7047317922538398),
                      (array([[136, 3],
                              [1, 46]]),
                       0.9571417398636336),
                      ]
        self.errors = [(array([[51, 4, 0, 1, 1],
                               [3, 78, 1, 0, 0],
                               [0, 0, 13, 4, 0],
                               [0, 1, 1, 16, 7],
                               [0, 0, 0, 0, 5]]),
                        ValueError),
                       (array([[1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]),
                        ValueError),
                       (array([[1, 2],
                               [4, 5],
                               [7, 8]]),
                        ValueError),
                       (array([[1]]),
                        ValueError),
                       (array([[1, 2],
                               [3, -4]]),
                        ValueError),
                       (array([[0, 0],
                               [0, 0]]),
                        ValueError)
                       ]

    def test_yule_y(self):
        """Measure evaluations
        """
        for matrix, res in self.tests:
            self.assertAlmostEqual(yule_y(matrix),
                                   res, places=7)

    def test_yule_y_domain(self):
        """Test out-of-domain matrices
        """
        for matrix, err_type in self.errors:
            with self.assertRaises(err_type):
                yule_y(matrix)


class TestBangdiwalaB(unittest.TestCase):
    r"""This class implements the tests for Bangdiwala's B
    """

    def setUp(self):
        """Setup the tests
        """
        self.tests = [(array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]),
                       0.1467764060356653),
                      (array([[3600, 2595],
                              [65, 3740]]),
                       0.575688404132935),
                      (array([[9901, 64],
                              [2, 33]]),
                       0.9933537203915539),
                      (array([[9900, 86],
                              [1, 13]]),
                       0.9912756264181609),
                      (array([[21, 5],
                              [3, 21]]),
                       0.7067307692307693),
                      (array([[40, 5],
                              [3, 2]]),
                       0.8142131979695432),
                      (array([[40, 2],
                              [3, 5]]),
                       0.8727175080558539),
                      (array([[51, 4, 0, 1, 1],
                              [3, 78, 1, 0, 0],
                              [0, 0, 13, 4, 0],
                              [0, 1, 1, 16, 7],
                              [0, 0, 0, 0, 5]]),
                       0.851430701836145),
                      (array([[136, 3],
                              [1, 46]]),
                       0.965614166588588),
                      ]
        self.errors = [(array([[1, 2],
                               [4, 5],
                               [7, 8]]),
                        ValueError),
                       (array([[1, 2],
                               [3, -4]]),
                        ValueError),
                       (array([[0, 0],
                               [0, 0]]),
                        ValueError)
                       ]

    def test_bangdiwala_b(self):
        """Measure evaluations
        """
        for matrix, res in self.tests:
            self.assertAlmostEqual(bangdiwala_b(matrix),
                                   res, places=7)

    def test_bangdiwala_b_domain(self):
        """Test out-of-domain matrices
        """
        for matrix, err_type in self.errors:
            with self.assertRaises(err_type):
                bangdiwala_b(matrix)


class TestBennettS(unittest.TestCase):
    r"""This class implements the tests for Bennett's S
    """

    def setUp(self):
        """Setup the tests
        """
        self.tests = [(array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]),
                       0.0),
                      (array([[3600, 2595],
                              [65, 3740]]),
                       0.468),
                      (array([[9901, 64],
                              [2, 33]]),
                       0.9868),
                      (array([[9900, 86],
                              [1, 13]]),
                       0.9826),
                      (array([[21, 5],
                              [3, 21]]),
                       0.68),
                      (array([[40, 5],
                              [3, 2]]),
                       0.68),
                      (array([[40, 2],
                              [3, 5]]),
                       0.8),
                      (array([[51, 4, 0, 1, 1],
                              [3, 78, 1, 0, 0],
                              [0, 0, 13, 4, 0],
                              [0, 1, 1, 16, 7],
                              [0, 0, 0, 0, 5]]),
                       0.8454301075268817),
                      (array([[136, 3],
                              [1, 46]]),
                       0.956989247311828),
                      ]
        self.errors = [(array([[1, 2],
                               [4, 5],
                               [7, 8]]),
                        ValueError),
                       (array([[1, 2],
                               [3, -4]]),
                        ValueError),
                       (array([[0, 0],
                               [0, 0]]),
                        ValueError)
                       ]

    def test_bennett_s(self):
        """Measure evaluations
        """
        for matrix, res in self.tests:
            self.assertAlmostEqual(bennett_s(matrix),
                                   res, places=7)

    def test_bennett_s_domain(self):
        """Test out-of-domain matrices
        """
        for matrix, err_type in self.errors:
            with self.assertRaises(err_type):
                bennett_s(matrix)


class TestScottPi(unittest.TestCase):
    r"""This class implements the tests for Scott's Pi
    """

    def setUp(self):
        """Setup the tests
        """
        self.tests = [(array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]),
                       -0.05633802816901419),
                      (array([[3600, 2595],
                              [65, 3740]]),
                       0.46789570755868143),
                      (array([[9901, 64],
                              [2, 33]]),
                       0.49667807529695585),
                      (array([[9900, 86],
                              [1, 13]]),
                       0.22571377842332252),
                      (array([[21, 5],
                              [3, 21]]),
                       0.6799999999999999),
                      (array([[40, 5],
                              [3, 2]]),
                       0.24242424242424246),
                      (array([[40, 2],
                              [3, 5]]),
                       0.6078431372549022),
                      (array([[51, 4, 0, 1, 1],
                              [3, 78, 1, 0, 0],
                              [0, 0, 13, 4, 0],
                              [0, 1, 1, 16, 7],
                              [0, 0, 0, 0, 5]]),
                       0.8205800322939165),
                      (array([[136, 3],
                              [1, 46]]),
                       0.943840579710145),
                      ]
        self.errors = [(array([[1, 2],
                               [4, 5],
                               [7, 8]]),
                        ValueError),
                       (array([[1]]),
                        ValueError),
                       (array([[1, 2],
                               [3, -4]]),
                        ValueError),
                       (array([[0, 0],
                               [0, 0]]),
                        ValueError)
                       ]

    def test_scott_pi(self):
        """Measure evaluations
        """
        for matrix, res in self.tests:
            self.assertAlmostEqual(scott_pi(matrix),
                                   res, places=7)

    def test_scott_pi_domain(self):
        """Test out-of-domain matrices
        """
        for matrix, err_type in self.errors:
            with self.assertRaises(err_type):
                scott_pi(matrix)


class TestCohenKappa(unittest.TestCase):
    r"""This class implements the tests for Cohen's Kappa
    """

    def setUp(self):
        """Setup the tests
        """
        self.tests = [(array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]),
                       -0.0416666666666666),
                      (array([[3600, 2595],
                              [65, 3740]]),
                       0.49991210861307384),
                      (array([[9901, 64],
                              [2, 33]]),
                       0.4974147318402951),
                      (array([[9900, 86],
                              [1, 13]]),
                       0.22819518322823573),
                      (array([[21, 5],
                              [3, 21]]),
                       0.6805111821086262),
                      (array([[40, 5],
                              [3, 2]]),
                       0.24528301886792425),
                      (array([[40, 2],
                              [3, 5]]),
                       0.6081504702194358),
                      (array([[51, 4, 0, 1, 1],
                              [3, 78, 1, 0, 0],
                              [0, 0, 13, 4, 0],
                              [0, 1, 1, 16, 7],
                              [0, 0, 0, 0, 5]]),
                       0.8207566933422716),
                      (array([[136, 3],
                              [1, 46]]),
                       0.9438490566037736),
                      ]
        self.errors = [(array([[1, 2],
                               [4, 5],
                               [7, 8]]),
                        ValueError),
                       (array([[1]]),
                        ValueError),
                       (array([[1, 2],
                               [3, -4]]),
                        ValueError),
                       (array([[1]]),
                        ValueError),
                       (array([[0, 0],
                               [0, 0]]),
                        ValueError)
                       ]

    def test_cohen_kappa(self):
        """Measure evaluations
        """
        for matrix, res in self.tests:
            self.assertAlmostEqual(cohen_kappa(matrix),
                                   res, places=7)

    def test_cohen_kappa_domain(self):
        """Test out-of-domain matrices
        """
        for matrix, err_type in self.errors:
            with self.assertRaises(err_type):
                cohen_kappa(matrix)


class TestIAeps(unittest.TestCase):
    r"""This class implements the tests for IAeps
    """

    def setUp(self):
        """Setup the tests
        """
        self.tests = [(array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]),
                       0.005631983988003131),
                      (array([[3600, 2595],
                              [65, 3740]]),
                       0.30887720803994045),
                      (array([[9901, 64],
                              [2, 33]]),
                       0.6512617074161697),
                      (array([[9900, 86],
                              [1, 13]]),
                       0.5405241728004455),
                      (array([[21, 5],
                              [3, 21]]),
                       0.3711004990501593),
                      (array([[40, 5],
                              [3, 2]]),
                       0.07294578321618128),
                      (array([[40, 2],
                              [3, 5]]),
                       0.34151310726779016),
                      (array([[51, 4, 0, 1, 1],
                              [3, 78, 1, 0, 0],
                              [0, 0, 13, 4, 0],
                              [0, 1, 1, 16, 7],
                              [0, 0, 0, 0, 5]]),
                       0.7291088595271555),
                      (array([[136, 3],
                              [1, 46]]),
                       0.8363880077413772),
                      ]
        self.errors = [(array([[1, 2],
                               [4, 5],
                               [7, 8]]),
                        ValueError),
                       (array([[1, 2],
                               [3, -4]]),
                        ValueError),
                       (array([[1]]),
                        ValueError),
                       (array([[0, 0],
                               [0, 0]]),
                        ValueError)
                       ]

    def test_ia_eps(self):
        """Measure evaluations
        """
        for matrix, res in self.tests:
            self.assertAlmostEqual(ia_eps(matrix),
                                   res, places=7)

    def test_ia_eps_domain(self):
        """Test out-of-domain matrices
        """
        for matrix, err_type in self.errors:
            with self.assertRaises(err_type):
                ia_eps(matrix)


if __name__ == '__main__':
    unittest.main()
