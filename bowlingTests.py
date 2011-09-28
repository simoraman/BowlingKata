import unittest
import itertools
from bowlingGame import *


class BowlingTests(unittest.TestCase):
    def roll_many(self,  n,  pins):
        for _ in itertools.repeat(None,  n):
            self.game.roll(pins)
        
    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        
    def setUp(self):
        self.game=Game()
    
    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())
        
    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.game.score())
        
    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(16, self.game.score())
        
if __name__ == '__main__':
    unittest.main()
