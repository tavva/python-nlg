'''
Created on Sep 11, 2011

@author: Nich
'''
import xml.etree.ElementTree
import os.path
from collections import namedtuple
from collections import defaultdict

import pynlg.morphology as morph

DEFAULT_PATH = os.path.abspath("/projects/Python-nlg/trunk/res/default-lexicon.xml")


class Word(object):
    def __init__(self, base, category, w_id = "E000000", features = None, inflections= None):
        self.base = base
        self.category = category
        self.id = w_id
        self.features = {} if features is None else features
        self.inflections = {} if inflections is None else inflections
    def hasFeature(self, key):
        return key in self.features    

class Lexicon(object):
    def __init__(self):
        self.words_by_id = {}
        self.words_by_base = defaultdict(list)
        self.words_by_category = defaultdict(list)
        self.words_by_variants = defaultdict(list)
        
         
    def hasWord(self, word, word_cat = None):
        if word in self.words_by_base.keys():
            if word_cat == None:
                return True
            else:
                for value in self.words_by_base[word]:
                    if value.category == word_cat:
                        return True
                return False
        
        
    
    
    def getWordByID(self, id):
        return self.words_by_id[id]
    
    def getWords(self, word, word_cat = None):
        words = self.words_by_base[word]
        if not word_cat is None:
            return [w for w in words if w.category == word_cat]
        else:
            return words
        
    def getWord(self, word, word_cat = None):
        return self._getWordFromDict(self.words_by_base, word, word_cat)
        
    def getWordFromVariant(self, variant, word_cat = None):
        return self._getWordFromDict(self.words_by_variants, variant, word_cat)
    def _getWordFromDict(self, w_dict, word, word_cat = None):
        words = w_dict[word]
        if word_cat is None:
            if len(words) == 0:
                return None
            if len(words) == 1:
                return words[0]
            else:
                return words
        else:
            for w in words:
                if w.category == word_cat:
                    return w
        return None
    
    def makeVariants(self, word_elem):
        for variant in morph.makeVariants(word_elem):
            self.words_by_variants[variant].append(word_elem)
    
    def makeInflections(self, word_elem):
        inflections = morph.makeInflections(word_elem)
        for key, value in inflections.items():
            #add to variants list so we can search by it
            self.words_by_variants[value].append(word_elem)
            word_elem.inflections[key] = value
            setattr(word_elem, "to_"+key, lambda: word_elem.inflections[key])

class XMLLexicon(Lexicon):
    
    def __init__(self, filename=None):
        Lexicon.__init__(self)
        if filename is None:
            lex_tree = xml.etree.ElementTree.parse(DEFAULT_PATH)
        else:
            lex_tree = xml.etree.ElementTree.parse(filename)
        
        self.buildDicts(lex_tree)
        
    def buildDicts(self, lex_tree):
        lex = lex_tree.getroot()
        for word in lex.findall("word"):
            word_elem = self.makeWordElem(word)
            self.words_by_base[word_elem.base].append(word_elem)
            self.words_by_category[word_elem.category].append(word_elem)
            self.words_by_id[word_elem.id] = word_elem
            self.words_by_variants[word_elem.base].append(word_elem)
            self.makeInflections(word_elem)
        
    def makeWordElem(self, word):
        features = {}
        base = None
        w_id = None
        category = None
        for prop in list(word):
            if prop.tag == "base":
                base = prop.text.lower()
            elif prop.tag == "id":
                w_id = prop.text.upper()
            elif prop.tag == "category":
                category = prop.text.upper()
            else:
                if len(prop) == 0:
                    features[prop.tag.lower()] = True
                else:
                    features[prop.tag.lower()] = prop.text
        return Word(base, category, w_id, features)
    
    

        
    
            
        
        
    