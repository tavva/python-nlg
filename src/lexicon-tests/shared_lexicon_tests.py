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
        self.assertEqual("abandoned", self.abandon.past)
        self.assertEqual("battled", self.battle.past)
        self.assertEqual("bore", self.bear.past)
        self.assertEqual("healed", self.heal.past)
        self.assertEqual("lingered", self.linger.past)

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
        self.assertTrue(isinstance(abandon, lex.Verb))
        
        
    def testGetWords(self):
        #"Can" has 3 possible values, a verb, a noun, and a modal
        self.assertEqual(3, len(self.lexicon.getWords("can")))
        self.assertEqual(set(["NOUN", "VERB", "MODAL"]), set([w.category for w in self.lexicon.getWords("can")]))
        self.assertEqual(set([lex.Noun, lex.Verb, lex.Modal]), set([type(w) for w in self.lexicon.getWords("can")]))
        self.assertEqual(1, len(self.lexicon.getWords("can", "NOUN")))
        self.assertEqual(0, len(self.lexicon.getWords("can", "ADJECTIVE")))
    
    def testGetWord_good(self):
        good = self.lexicon.getWord("good", "ADJECTIVE")
        self.assertEqual("better", good.comparative)
        self.assertEqual("best", good.superlative)
        self.assertTrue(good.hasFeature("qualitative"))
        self.assertTrue(good.hasFeature("predicative"))
        self.assertFalse(good.hasFeature("colour"))
        self.assertFalse(good.hasFeature("classifying"))
    
    def testGetWord_woman(self):
        woman = self.lexicon.getWord("woman")
        self.assertEqual("women", woman.plural)
        self.assertFalse(woman.hasFeature("PROPER"))
        self.assertFalse(woman.hasInflection("UNCOUNT"))
    
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
        self.assertTrue(eat.hasFeature("transitive"))
        self.assertTrue(eat.hasFeature("intransitive"))
        self.assertFalse(eat.hasFeature("ditransitive"))
        
    def test_BE(self):
        be = self.lexicon.getWordFromVariant("is", "VERB")
        self.assertEqual("be", be.base)
        self.assertEqual("is", be.present)
        self.assertEqual("been", be.past_participle)
        
    def testModal(self):
        can = self.lexicon.getWord('can', 'MODAL')
        self.assertEqual("could", can.past)
    
    def testNonExistantWord(self):
        self.assertFalse(self.lexicon.hasWord("Quijubie"))
        self.assertEquals(0, len(self.lexicon.getWords("Quijubie")))
        self.assertRaises(Exception, self.lexicon.getWord, ("Quijubie"))
        
    def testLookup(self):
        self.assertEqual("say", self.lexicon.lookup("say", "VERB").base)
        self.assertEqual("say", self.lexicon.lookup("said", "VERB").base)
        self.assertEqual("say", self.lexicon.lookup("E0054448").base)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()