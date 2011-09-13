'''
Created on Sep 11, 2011

@author: Nich
'''
import unittest
import pynlg.lexicon as lex

class TestWords(unittest.TestCase):
    def setUp(self):
        self.lexicon = lex.XMLLexicon()
        self.abandon = self.lexicon.getWord("abandon", "VERB")
        self.battle = self.lexicon.getWord("battle", "VERB")
        self.bear = self.lexicon.getWord("bear", "VERB")
        self.heal = self.lexicon.getWord("heal", "VERB")
        self.linger = self.lexicon.getWord("linger", "VERB")
        
    def tearDown(self):
        del self.lexicon
    
    def testVerbPastConversion(self):
        self.assertEqual("abandoned", self.abandon.to_past())
        self.assertEqual("battled", self.battle.to_past())
        self.assertEqual("bore", self.bear.to_past())
        self.assertEqual("healed", self.heal.to_past())
        self.assertEqual("lingered", self.linger.to_past())

class TestLexicon(unittest.TestCase):

    def setUp(self):
        self.lexicon = lex.XMLLexicon()
        
    def tearDown(self):
        del self.lexicon
    
    def testGetWord(self):
        abandon = self.lexicon.getWord("abandon")
        self.assertEqual("abandon", abandon.base)
        self.assertEqual("VERB", abandon.category)
        self.assertEqual("E0006429", abandon.id)
        
    def testGetWords(self):
        #"Can" has 3 possible values, a verb, a noun, and a modal
        self.assertEqual(3, len(self.lexicon.getWords("can")))
        self.assertEqual(1, len(self.lexicon.getWords("can", "NOUN")))
        self.assertEqual(0, len(self.lexicon.getWords("can", "ADJECTIVE")))
    
    def testGetWord_good(self):
        good = self.lexicon.getWord("good", "ADJECTIVE")
        self.assertEqual("better", good.to_comparative())
        self.assertEqual("best", good.to_superlative())
        self.assertTrue(good.hasFeature("QUALITATIVE"))
        self.assertTrue(good.hasFeature("PREDICATIVE"))
        self.assertFalse(good.hasFeature("COLOUR"))
        self.assertFalse(good.hasFeature("CLASSIFYING"))
    
    def testGetWord_woman(self):
        woman = self.lexicon.getWord("woman")
        self.assertEqual("women", woman.plural())
        self.assertEqual(None, woman.acronymOf())
        self.assertFalse(woman.hasFeature("PROPER"))
        self.assertFalse(woman.hasInfVariant("UNCOUNT"))
    
    def testGetWord_sand(self):
        sand = self.lexicon.getWord("sand", "NOUN")
        self.assertTrue(sand.hasFeature("noncount"))
        
    def testHasWord_tree(self):
        self.assertTrue(self.lexicon.hasWord("tree"))
        self.assertFalse(self.lexicon.hasWord("tree", "ADJECTIVE"))
        
    def testGetWordByID_quickly(self):
        quickly = self.lexicon.getWordByID("E0051632")
        self.assertEqual("quickly", quickly.base)
        self.assertEqual("ADVERB", quickly.category)
        self.assertTrue(quickly.hasFeature("verb_modifier"))
        self.assertFalse(quickly.hasFeature("sentence_modifier"))
        self.assertFalse(quickly.hasFeature("intensifier"))
    
    def testGetWordFromVariant_eating_eat(self):
        eat = self.lexicon.getWordFromVariant("eating")
        self.assertEqual("eat", eat.base)
        self.assertTrue(eat.hasFeature("TRANSITIVE"))
        self.assertTrue(eat.hasFeature("INTRANSITIVE"))
        self.assertFalse(eat.hasFeature("DITRANSITIVE"))
        
    def test_BE(self):
        be = self.lexicon.getWordFromVariant("is", "VERB")
        self.assertEqual("been", be.toPastParticiple())
        
    def testModal(self):
        can = self.lexicon.getWord('can', 'MODAL')
        self.assertEqual("could", can.toPast())
    
    def testNonExistantWord(self):
        self.assertFalse(self.lexicon.hasWord("Quijubie"))
        self.assertEquals(0, len(self.lexicon.getWords("Quijubie")))
        
    def testLookup(self):
        self.assertEqual("say", lexicon.lookup("say", "VERB").base)
        self.assertEqual("say", lexicon.lookup("said", "VERB").base)
        self.assertEqual("say", lexicon.lookup("E0054448").base)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()