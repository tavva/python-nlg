'''
Created on Sep 12, 2011

@author: Nich
'''
import unittest
import pynlg.morphology
from pynlg.lexicon import Word

class NounTest(unittest.TestCase):
    def setUp(self):
        #make some words
        self.story = Word("story", "NOUN")
        self.hero = Word("hero", "NOUN")
        self.case = Word("case", "NOUN")
        
        #Irreg
        self.goose = Word("goose", "NOUN", features = {"plural":"geese"})
        
        #Proper
        self.Harry = Word("Harry", "NOUN", features = {"proper":True})
        
    def tearDown(self):
        pass

    def testNounPlural(self):
        morph = pynlg.morphology
        self.assertEqual("stories", morph.noun_plural(self.story))
        self.assertEqual("heroes", morph.noun_plural(self.hero))
        self.assertEqual("cases", morph.noun_plural(self.case))
        self.assertEqual("geese", morph.noun_plural(self.goose))
        self.assertEqual("Harrys", morph.noun_plural(self.Harry))

class VerbTensesTest(unittest.TestCase):
    def setUp(self):
        self.walk = Word("walk", "VERB")
        self.be = Word("is", "VERB", features = {"infinitive":"to be", "past":"was"})
        self.welcome = Word("welcome", "VERB")
        self.program = Word("program", "VERB")
        self.worry = Word("worry", "VERB")
        
    def tearDown(self):
        pass
    
    def testInfinitive(self):
        morph = pynlg.morphology
        self.assertEqual("to walk", morph.verb_inf(self.walk))
        self.assertEqual("to welcome", morph.verb_inf(self.welcome))
        self.assertEqual("to program", morph.verb_inf(self.program))
        self.assertEqual("to be", morph.verb_inf(self.be))
        self.assertEqual("to worry", morph.verb_inf(self.worry))
        
    def testPast(self):
        morph = pynlg.morphology
        self.assertEqual("walked", morph.verb_past(self.walk))
        self.assertEqual("welcomed", morph.verb_past(self.welcome))
        self.assertEqual("programmed", morph.verb_past(self.program))
        self.assertEqual("was", morph.verb_past(self.be))
        self.assertEqual("worried", morph.verb_past(self.worry))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNounPlural']
    unittest.main()