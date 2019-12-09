#!/usr/bin/python3

import unittest
from tree import show_tree
from math import *

class TestUM(unittest.TestClass):
    def setUp(self):
        pass

    def test_tree1(self)
        self.assertEqual(show_tree(1), """x
                                           x """)
    
    def test_tree2(self):
        self.assertEqual(show_tree(2), """x
                                          xxx
                                           x """)
    
    def test_tree5(self):
        self.assertEqual(show_tree(5), """x
                                          xxx
                                         xxxxx
                                          xxx
                                          xxx """)
    
    def test_tree30(self):
        self.assertEqual(show_tree(30), """x
                                           xxx
                                          xxxxx
                                         xxxxxxx
                                        xxxxxxxxx
                                       xxxxxxxxxxx
                                      xxxxxxxxxxxxx
                                     xxxxxxxxxxxxxxx
                                    xxxxxxxxxxxxxxxxx
                                   xxxxxxxxxxxxxxxxxxx
                                  xxxxxxxxxxxxxxxxxxxxx
                                 xxxxxxxxxxxxxxxxxxxxxxx
                                xxxxxxxxxxxxxxxxxxxxxxxxx
                               xxxxxxxxxxxxxxxxxxxxxxxxxxx
                              xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                             xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                           xxx
                                           xxx
                                           xxx
                                           xxx
                                           xxx
                                           xxx
                                           xxx """)

if __name__ == '__main__':
    unittest.main()