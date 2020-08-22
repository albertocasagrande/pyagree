from pyagree import *
from numpy import array

import unittest

class TestFleissKappa(unittest.TestCase):
    def setUp(self):
        self.Cs = [(array([[0, 0, 0, 0,14],
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

    def test_FleissKappa(self):
    	for C, res in self.Cs:
            self.assertAlmostEqual(FleissKappa(C), 
                                   res, places=7)


class TestScottPi(unittest.TestCase):
    def setUp(self):
        self.Cs = [(array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]),
                    0.0),
                   (array([[3600,2595],
                           [  65,3740]]),
                    0.468),
                   (array([[9901,  64],
                           [   2,  33]]),
                    0.9868),
                   (array([[9900,  86],
                           [   1,  13]]),
                    0.9826),
                   (array([[21, 5],
                           [ 3,21]]),
                    0.68),
                   (array([[40, 5],
                           [ 3, 2]]),
                    0.68),
                   (array([[40, 2],
                           [ 3, 5]]),
                    0.8),
                   (array([[51, 4, 0, 1, 1],
                           [ 3,78, 1, 0, 0],
                           [ 0, 0,13, 4, 0],
                           [ 0, 1, 1,16, 7],
                           [ 0, 0, 0, 0, 5]]),
                    0.8454301075268817),
                   (array([[136,  3],
                           [  1, 46]]),
                    0.956989247311828),
                   ]

    def test_ScottPi(self):
    	for C, res in self.Cs:
            self.assertAlmostEqual(ScottPi(C), 
        	                   res, places=7)


class TestBangdiwalaB(unittest.TestCase):
    def setUp(self):
        self.Cs = [(array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]),
                    0.1467764060356653),
                   (array([[3600,2595],
                           [  65,3740]]),
                    0.575688404132935),
                   (array([[9901,  64],
                           [   2,  33]]),
                    0.9933537203915539),
                   (array([[9900,  86],
                           [   1,  13]]),
                    0.9912756264181609),
                   (array([[21, 5],
                           [ 3,21]]),
                    0.7067307692307693),
                   (array([[40, 5],
                           [ 3, 2]]),
                    0.8142131979695432),
                   (array([[40, 2],
                           [ 3, 5]]),
                    0.8727175080558539),
                   (array([[51, 4, 0, 1, 1],
                           [ 3,78, 1, 0, 0],
                           [ 0, 0,13, 4, 0],
                           [ 0, 1, 1,16, 7],
                           [ 0, 0, 0, 0, 5]]),
                    0.851430701836145),
                   (array([[136,  3],
                           [  1, 46]]),
                    0.965614166588588),
                   ]

    def test_BangdiwalaB(self):
    	for C, res in self.Cs:
            self.assertAlmostEqual(BangdiwalaB(C), 
        	                   	   res, places=7)


class TestBennettS(unittest.TestCase):
    def setUp(self):
        self.Cs = [(array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]),
                    0.0),
                   (array([[3600,2595],
                           [  65,3740]]),
                    0.468),
                   (array([[9901,  64],
                           [   2,  33]]),
                    0.9868),
                   (array([[9900,  86],
                           [   1,  13]]),
                    0.9826),
                   (array([[21, 5],
                           [ 3,21]]),
                    0.68),
                   (array([[40, 5],
                           [ 3, 2]]),
                    0.68),
                   (array([[40, 2],
                           [ 3, 5]]),
                    0.8),
                   (array([[51, 4, 0, 1, 1],
                           [ 3,78, 1, 0, 0],
                           [ 0, 0,13, 4, 0],
                           [ 0, 1, 1,16, 7],
                           [ 0, 0, 0, 0, 5]]),
                    0.8454301075268817),
                   (array([[136,  3],
                           [  1, 46]]),
                    0.956989247311828),
                   ]

    def test_BennettS(self):
    	for C, res in self.Cs:
            self.assertAlmostEqual(BennettS(C), 
        	                   res, places=7)


class TestScottPi(unittest.TestCase):
    def setUp(self):
        self.Cs = [(array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]),
                    -0.05633802816901419),
                   (array([[3600,2595],
                           [  65,3740]]),
                    0.46789570755868143),
                   (array([[9901,  64],
                           [   2,  33]]),
                    0.49667807529695585),
                   (array([[9900,  86],
                           [   1,  13]]),
                    0.22571377842332252),
                   (array([[21, 5],
                           [ 3,21]]),
                    0.6799999999999999),
                   (array([[40, 5],
                           [ 3, 2]]),
                    0.24242424242424246),
                   (array([[40, 2],
                           [ 3, 5]]),
                    0.6078431372549022),
                   (array([[51, 4, 0, 1, 1],
                           [ 3,78, 1, 0, 0],
                           [ 0, 0,13, 4, 0],
                           [ 0, 1, 1,16, 7],
                           [ 0, 0, 0, 0, 5]]),
                    0.8205800322939165),
                   (array([[136,  3],
                           [  1, 46]]),
                    0.943840579710145),
                   ]

    def test_ScottPi(self):
    	for C, res in self.Cs:
            self.assertAlmostEqual(ScottPi(C), 
        	                   res, places=7)

class TestCohenKappa(unittest.TestCase):
    def setUp(self):
        self.Cs = [(array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]),
                    -0.0416666666666666),
                   (array([[3600,2595],
                           [  65,3740]]),
                    0.49991210861307384),
                   (array([[9901,  64],
                           [   2,  33]]),
                    0.4974147318402951),
                   (array([[9900,  86],
                           [   1,  13]]),
                    0.22819518322823573),
                   (array([[21, 5],
                           [ 3,21]]),
                    0.6805111821086262),
                   (array([[40, 5],
                           [ 3, 2]]),
                    0.24528301886792425),
                   (array([[40, 2],
                           [ 3, 5]]),
                    0.6081504702194358),
                   (array([[51, 4, 0, 1, 1],
                           [ 3,78, 1, 0, 0],
                           [ 0, 0,13, 4, 0],
                           [ 0, 1, 1,16, 7],
                           [ 0, 0, 0, 0, 5]]),
                    0.8207566933422716),
                   (array([[136,  3],
                           [  1, 46]]),
                    0.9438490566037736),
                   ]

    def test_CohenKappa(self):
    	for C, res in self.Cs:
            self.assertAlmostEqual(CohenKappa(C), 
        	                   res, places=7)


class TestIAeps(unittest.TestCase):
    def setUp(self):
        self.Cs = [(array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]),
                    0.005631983988003131),
                   (array([[3600,2595],
                           [  65,3740]]),
                    0.30887720803994045),
                   (array([[9901,  64],
                           [   2,  33]]),
                    0.6512617074161697),
                   (array([[9900,  86],
                           [   1,  13]]),
                    0.5405241728004455),
                   (array([[21, 5],
                           [ 3,21]]),
                    0.3711004990501593),
                   (array([[40, 5],
                           [ 3, 2]]),
                    0.07294578321618128),
                   (array([[40, 2],
                           [ 3, 5]]),
                    0.34151310726779016),
                   (array([[51, 4, 0, 1, 1],
                           [ 3,78, 1, 0, 0],
                           [ 0, 0,13, 4, 0],
                           [ 0, 1, 1,16, 7],
                           [ 0, 0, 0, 0, 5]]),
                    0.7291088595271555),
                   (array([[136,  3],
                           [  1, 46]]),
                    0.8363880077413772),
                   ]

    def test_IAeps(self):
    	for C, res in self.Cs:
            self.assertAlmostEqual(IAeps(C), 
        	                   res, places=7)


if __name__=='__main__':
    unittest.main()

