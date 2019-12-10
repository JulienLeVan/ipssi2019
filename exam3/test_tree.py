#!/usr/bin/python3

import unittest
from tree import show_tree


class TestUM(unittest.TestClass):
    def setUp(self):
        pass

    def test_tree1(self)
        self.assertEqual(show_tree(1),
                   """ X
                      XXX      
                       X """)

    def test_tree2(self):
        self.assertEqual(show_tree(2),
                   """ X
                      XXX      
                       X """)
                       
    def test_tree5(self):
        self.assertEqual(show_tree(5), 
                   """ X
                      XXX
                     XXXXX      
                      XXX
                      XXX """)
    
    def test_tree30(self):
        self.assertEqual(show_tree(30), 
                   """ X
                      XXX
                     XXXXX
                    XXXXXXX
                   XXXXXXXXX
                  XXXXXXXXXXX
                 XXXXXXXXXXXXX
                XXXXXXXXXXXXXXX
               XXXXXXXXXXXXXXXXX
              XXXXXXXXXXXXXXXXXXX
             XXXXXXXXXXXXXXXXXXXXX
            XXXXXXXXXXXXXXXXXXXXXXX
           XXXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXXXX
         XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXX
                      XXX
                      XXX
                      XXX
                      XXX
                      XXX
                      XXX """)

if __name__ == '__main__':
    unittest.main()