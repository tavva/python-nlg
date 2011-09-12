'''
Created on Sep 11, 2011

@author: Nich
'''
import unittest
import pynlg.lexicon as lex

class Test(unittest.TestCase):


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
        self.assertEqual("better", good.toComparative())
        self.assertEqual("best", good.toSuperlative())
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
        self.assertTrue(sand.hasInfVariant("UNCOUNT"))
        
    def testHasWord_tree(self):
        self.assertTrue(self.lexicon.hasWord("tree"))
        self.assertFalse(self.lexicon.hasWord("tree", "ADJECTIVE"))
        
    def testGetWordByID_quickly(self):
        quickly = self.lexicon.getWordByID("E0051632")
        self.assertEqual("quickly", quickly.baseForm())
        self.assertEqual("ADVERB", quickly.getCategory())
        self.assertTrue(quickly.hasFeature("VERB_MODIFIER"))
        self.assertFalse(quickly.hasFeature("SENTENCE_MODIFIER"))
        self.assertFalse(quickly.hasFeature("INTENSIFIER"))
    
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