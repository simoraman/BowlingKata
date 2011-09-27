import unittest
import itertools
from bowlingGame import *

class BowlingTests(unittest.TestCase):
    def setUp(self):
        self.game=Game()
    
    def test_gutter_game(self):
        for _ in itertools.repeat(None,  20):
            self.game.roll(0)
        self.assertEqual(0, self.game.score)
        
    def test_all_ones(self):
        for _ in itertools.repeat(None,  20):
            self.game.roll(1)
        self.assertEqual(20, self.game.score)
        
        
if __name__ == '__main__':
    unittest.main()
