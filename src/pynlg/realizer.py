'''
Created on 2013-03-06

@author: Nich
'''
from pynlg.lexicon import Noun, Determiner, Word


class NounPhrase():
    
    def __init__(self, word, determiner = None, adjectives = None, owners = None):
        self.base_word = word
        self.determiner = determiner
        self.owners = [] if owners == None else owners
        self.adjectives = [] if adjectives == None else adjectives
        
    def add_determiner(self, determiner):
        if isinstance(determiner, Determiner) or isinstance(determiner, Word):
            self.determiner = determiner
        else:
            raise Exception("A determiner must be an instance of Determiner or Word. Type of determiner given: " +str(type(determiner)))
    
    @staticmethod
    def wrap_noun_in_np(subject):
        #If the subject isn't a noun or a nounphrase, there's a problem
        if not isinstance(subject, Noun) and not isinstance(subject, NounPhrase):
            raise Exception("The subject of the Clause must either be a Noun or a NounPhrase. Type of " + str(subject) + ": " + str(type(subject)))
        np_subject = subject
        # If the subject is of type word, wrap it in a NounPhrase
        if isinstance(subject, Noun):
            np_subject = NounPhrase(subject)
        return np_subject
    
    def add_owner(self, object):
        np_object = NounPhrase.wrap_noun_in_np(object)
        self.owners.append(np_object)
        return np_object

    def realize_possessive(self):
        np = []
        if self.determiner:
            np.append(str(self.determiner))
            
        np.append(str(self.base_word))
        
        base = " ".join(np)
        if base[-1] == 's':
            return base+"'"
        
        return base +"'s"
        
        
    def realize(self):
        np = []
        if self.determiner:
            np.append(str(self.determiner))
        if len(self.owners) >= 1:
            np.append(self.owners[0].realize_possessive())
            
        np.append(str(self.base_word))
        
        return " ".join(np)
    
class VerbPhrase():
    def __init__(self, verb, adverbs=None, direct_object=None, indirect_object=None, tense = None):
        self.verb = verb
        self.adverbs = [] if adverbs == None else adverbs
        self.direct_object = direct_object
        self.indirect_object = indirect_object
        self.tense = tense
    
    def set_tense(self, tense):
        self.tense = tense
        
    def add_object(self, object, position=None):
        np_object = NounPhrase.wrap_noun_in_np(object)
        
        self.direct_object = np_object
        return np_object
    
    def add_indirect_object(self, object):
        np_object = NounPhrase.wrap_noun_in_np(object)
        
        self.indirect_object = np_object
        return np_object
    
    
    @staticmethod
    def wrap_verb_in_vp(verb):
        return VerbPhrase(verb)
    
    def realize(self):
        vp = []
        vp.append(self.verb.tense(self.tense))
        if not self.indirect_object is None:
            vp.append(self.indirect_object.realize())
        
        if not self.direct_object is None:
            vp.append(self.direct_object.realize())
        
        return " ".join(vp)
    
    
class Clause():
    
    def __init__(self, subject = None, verb = None, object = None, verbtense = "present"):
        self.subject = [] if subject is None else subject
        self.verb = [] if verb is None else verb
        self.object = [] if object is None else object
        self.verbtense = verbtense
        

    def add_subject(self, subject, position=None):
        np_subject = NounPhrase.wrap_noun_in_np(subject)
        
        #TODO: Currently ignores position
        self.subject.append(np_subject)
        
        return np_subject
        
    def add_verb(self, verb, position=None):
        vp_verb = VerbPhrase.wrap_verb_in_vp(verb)
        self.verb.append(vp_verb)
        return vp_verb
        
   
    def set_verb_tense(self, tense):
        for vp in self.verb:
            vp.set_tense(tense)
        
    def realize(self):
        return " ".join([self.subject[0].realize(), self.verb[0].realize()]) 

