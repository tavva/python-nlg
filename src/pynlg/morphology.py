'''
Created on Sep 12, 2011

@author: Nich
'''



def makeVariants(word):
    variants = []
    return variants

def makeInflections(word):
    inflections = {}
    if word.category == "NOUN":
        #do plural
        inflections.append(noun_plural(word))
    if word.category == "VERB":
        inflections.append(verb_inf(word))
        inflections.append(verb_past(word))
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