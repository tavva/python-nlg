'''
Created on Sep 12, 2011

@author: Nich
'''
vowels = ('a', 'e', 'i','o', 'u') #fuck y
double_vowels = ('ea', 'ee', 'oo', 'ou')


def makeVariants(word):
    variants = []
    return variants

def makeInflections(word):
    inflections = {}
    if word.category == "NOUN":
        #do plural
        inflections["plural"] = noun_plural(word)
    if word.category == "VERB":
        inflections["infinitive"] = verb_inf(word)
        inflections["past"] = verb_past(word)
    if word.category == "ADJECTIVE":
        inflections["superlative"] = adj_superlative(word)
        inflections["comparative"] = adj_comparative(word)
    return inflections
    
def noun_plural(word):
    base = word.base
    feat = word.features
    if "plural" in feat:
        return feat["plural"]
    
    if base[-2:] == "ss" or base[-2:] == "sh" or base[-2:] == "ch" or base[-1:] == "o":
        return base + "es"
    elif base[-1:] == "y" and not "proper" in feat:
        return base[:-1] + "ies"
    else:
        return base + "s"

def verb_inf(word):
    if "infinitive" in word.features:
        return word.features["infinitive"]
    else:
        return 'to '+word.base

def verb_past(word):
    if "past" in word.features:
        return word.features["past"]
    else:
        base = word.base
        if base[-1] == "e":
            return base+"d"
        if base[-1] in ('b', 'd', 'f', 'g', 'l', 'm', 'n', 'p', 's', 't', 'z'):
            return base+base[-1]+"ed"
        if base[-1] == 'y':
            return base[:-1]+"ied"
        else:
            return base+"ed"

def verb_present_participal(word):
    if "present_participal" in word.features:
        return word.features["present_participal"]
    else:
        base = word.base
        if base[-1] == "e":
            return base[:-1]+"ing"
        if base[-1] in ('b', 'd', 'f', 'g', 'l', 'm', 'n', 'p', 's', 't', 'z') and not base[-3:-1] in double_vowels:
            return base+base[-1]+"ing"
        if base[-1] == 'y':
            return base+"ing"
        else:
            return base+"ing"
        
        
def adj_comparative(word):
    if "comparative" in word.features:
        return word.features["comparative"]
    else:
        base = word.base
        if base[-1] == 'e':
            return base[:-1]+"er"
        if base[-3:] == "ful":
            return "more "+base
        if base[-1] in ('b', 'd', 'f', 'g', 'l', 'm', 'n', 'p', 's', 't', 'z') and base[-2:] != "ll":
            return base+base[-1]+"er"
        if base[-1] == 'y':
            return base[:-1] + "ier"
        return word.base+"er"
    
def adj_superlative(word):
    if "superlative" in word.features:
        return word.features["superlative"]
    else:
        base = word.base
        if base[-1] == 'e':
            return base[:-1]+"est"
        if base[-3:] == "ful":
            return "most "+base
        if base[-1] in ('b', 'd', 'f', 'g', 'l', 'm', 'n', 'p', 's', 't', 'z') and base[-2:] != "ll":
            return base+base[-1]+"est"
        if base[-1] == 'y':
            return base[:-1] + "iest"
        return word.base+"est"
    

    
    