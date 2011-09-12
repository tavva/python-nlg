'''
Created on Sep 12, 2011

@author: Nich
'''
import unittest
import pynlg.morphology
from pynlg.lexicon import Word

class Test(unittest.TestCase):
    def setUp(self):
        #make some words
        self.story = Word("story", "NOUN", "E0000", {})
        self.hero = Word("hero", "NOUN", "E0000", {})
        self.case = Word("case", "NOUN", "E0000", {})
        
        #Irreg
        self.goose = Word("goose", "NOUN", "E0000", {"plural":"geese"})
        
        #Proper
        self.Harry = Word("Harry", "NOUN", "E0000", {"proper":True})
        
    def tearDown(self):
        pass

    def testNounPlural(self):
        morph = pynlg.morphology
        self.assertEqual("stories", morph.noun_plural(self.story))
        self.assertEqual("heroes", morph.noun_plural(self.hero))
        self.assertEqual("cases", morph.noun_plural(self.case))
        self.assertEqual("geese", morph.noun_plural(self.goose))
        self.assertEqual("Harrys", morph.noun_plural(self.Harry))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNounPlural']
    unittest.main()