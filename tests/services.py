'''
Created on May 10, 2016

@author: rkushchak
'''

import unittest
from test_addressbook import AddressbookTestCase 
#from test_addressbook import PageNaviTestCase 


tests1 = unittest.TestLoader().loadTestsFromTestCase(AddressbookTestCase)
#tests2 = unittest.TestLoader().loadTestsFromTestCase(PageNaviTestCase)


all_tests = unittest.TestSuite([tests1])

unittest.TextTestRunner(verbosity=2).run(all_tests)