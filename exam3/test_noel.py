#!/usr/bin/python3

import unittest
from noel import show_noel

class TestUM(unittest.TestClass):
    def setUp(self):
        pass
    
    def test_noel_2018_8_18(self):
        self.assertEqual(show_noel(2018_8_18), """129 days before christmas
    August 20(18)
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
   September 2018
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
    October 2018
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
   November 2018
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
   December 2018
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 [25] 26 27 28 29 30
31""")
    
    def test_noel_2020_11_1(self):
        self.assertEqual(show_noel(2020-11-1)), """"54 days before christmas
   November 2020
Mo Tu We Th Fr Sa Su
                   (1)
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
   December 2020
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 [25] 26 27
28 29 30 31""")


if __name__ == '__main__':
    unittest.main()