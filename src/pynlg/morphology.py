'''
Created on Sep 12, 2011

@author: Nich
'''

def makeVariants(word):
    variants = []
    if word.category == "NOUN":
        #do plural
        variants.append(noun_plural(word))
    return variants
    
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
