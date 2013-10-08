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
        self.be = Word("be", "VERB", features = {"present":"is", "presentparticiple":"being", "to-infinitive":"to be", "infinitive":"be", "past":"was"})
        self.welcome = Word("welcome", "VERB")
        self.program = Word("program", "VERB")
        self.worry = Word("worry", "VERB")
        self.kiss = Word("kiss", "VERB")
        
    def tearDown(self):
        pass
    
    def testInfinitive(self):
        morph = pynlg.morphology
        self.assertEqual("walk", morph.verb_inf(self.walk))
        self.assertEqual("welcome", morph.verb_inf(self.welcome))
        self.assertEqual("program", morph.verb_inf(self.program))
        self.assertEqual("be", morph.verb_inf(self.be))
        self.assertEqual("worry", morph.verb_inf(self.worry))
        self.assertEqual("kiss", morph.verb_inf(self.kiss))
    
    def testToInfinitive(self):
        morph = pynlg.morphology
        self.assertEqual("to walk", morph.verb_to_inf(self.walk))
        self.assertEqual("to welcome", morph.verb_to_inf(self.welcome))
        self.assertEqual("to program", morph.verb_to_inf(self.program))
        self.assertEqual("to be", morph.verb_to_inf(self.be))
        self.assertEqual("to worry", morph.verb_to_inf(self.worry))
        self.assertEqual("to kiss", morph.verb_to_inf(self.kiss))
        
    def testPresent(self):
        morph = pynlg.morphology
        self.assertEqual("walks", morph.verb_present(self.walk))
        self.assertEqual("welcomes", morph.verb_present(self.welcome))
        self.assertEqual("programs", morph.verb_present(self.program))
        self.assertEqual("is", morph.verb_present(self.be))
        self.assertEqual("worries", morph.verb_present(self.worry))
        self.assertEqual("kisses", morph.verb_present(self.kiss))
        
    def testPast(self):
        morph = pynlg.morphology
        self.assertEqual("walked", morph.verb_past(self.walk))
        self.assertEqual("welcomed", morph.verb_past(self.welcome))
        self.assertEqual("programmed", morph.verb_past(self.program))
        self.assertEqual("was", morph.verb_past(self.be))
        self.assertEqual("worried", morph.verb_past(self.worry))
        self.assertEqual("kissed", morph.verb_past(self.kiss))
    
    def testPresentParticiple(self):
        morph = pynlg.morphology
        self.assertEqual("walking", morph.verb_present_participle(self.walk))
        self.assertEqual("welcoming", morph.verb_present_participle(self.welcome))
        self.assertEqual("programming", morph.verb_present_participle(self.program))
        self.assertEqual("being", morph.verb_present_participle(self.be))
        self.assertEqual("worrying", morph.verb_present_participle(self.worry))
        self.assertEqual("kissing", morph.verb_present_participle(self.kiss))
        eat = Word("eat", "VERB")
        self.assertEqual("eating", morph.verb_present_participle(eat))
        
    def testPresentProgressive(self):
        morph = pynlg.morphology
        self.assertEqual("is walking", morph.verb_present_progressive(self.walk))
        self.assertEqual("is welcoming", morph.verb_present_progressive(self.welcome))
        self.assertEqual("is programming", morph.verb_present_progressive(self.program))
        self.assertEqual("is being", morph.verb_present_progressive(self.be))
        self.assertEqual("is worrying", morph.verb_present_progressive(self.worry))
        
        
    def testPastProgressive(self):
        morph = pynlg.morphology
        self.assertEqual("was walking", morph.verb_past_progressive(self.walk))
        self.assertEqual("was welcoming", morph.verb_past_progressive(self.welcome))
        self.assertEqual("was programming", morph.verb_past_progressive(self.program))
        self.assertEqual("was being", morph.verb_past_progressive(self.be))
        self.assertEqual("was worrying", morph.verb_past_progressive(self.worry))
        
        
        
class AdjectivesTests(unittest.TestCase):
    
    def setUp(self):
        self.good = Word("good", "ADJECTIVE", features = {"superlative":"best", "comparative":"better"})
        self.tall = Word("tall", "ADJECTIVE")
        self.large = Word("large", "ADJECTIVE")
        self.big = Word("big", "ADJECTIVE")
        self.happy = Word("happy", "ADJECTIVE")
        self.beautiful = Word("beautiful", "ADJECTIVE")
        
    def tearDown(self):
        pass
        
    def testSuperlative(self):
        morph = pynlg.morphology
        self.assertEqual("best", morph.adj_superlative(self.good))
        self.assertEqual("tallest", morph.adj_superlative(self.tall))
        self.assertEqual("largest", morph.adj_superlative(self.large))
        self.assertEqual("biggest", morph.adj_superlative(self.big))
        self.assertEqual("happiest", morph.adj_superlative(self.happy))
        self.assertEqual("most beautiful", morph.adj_superlative(self.beautiful))
        
    def testComparative(self):
        morph = pynlg.morphology
        self.assertEqual("better", morph.adj_comparative(self.good))
        self.assertEqual("taller", morph.adj_comparative(self.tall))
        self.assertEqual("larger", morph.adj_comparative(self.large))
        self.assertEqual("bigger", morph.adj_comparative(self.big))
        self.assertEqual("happier", morph.adj_comparative(self.happy))
        self.assertEqual("more beautiful", morph.adj_comparative(self.beautiful))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNounPlural']
    unittest.main()