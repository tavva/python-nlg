'''
Created on Sep 11, 2011

@author: Nich
'''
import copy

class Simple(object):
    pass


def make_method(obj, name, method):
    
    setattr(obj, name, method)


sim = Simple()
li = []    
for i in range(5):
    li.append(i)
    def newmethod():return li[copy.deepcopy(i)]
    make_method(sim, "method"+str(i), newmethod)

print(sim.method0())
print(sim.method1())
print(sim.method2())
print(sim.method3())
print(sim.method4())
    
    

