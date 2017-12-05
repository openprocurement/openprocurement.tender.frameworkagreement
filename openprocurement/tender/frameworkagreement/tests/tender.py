# -*- coding: utf-8 -*-
import unittest

def suite():
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(TestTenderEU))
    #suite.addTest(unittest.makeSuite(TestTenderEUProcess))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')