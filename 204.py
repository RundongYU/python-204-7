import bin, dsharp
from nltk import c #as a constant

class Encoding(object):
    def __init__(self):
        self.constraints = []

    def size(self):
        ret = 0 #return = ret
        for c in self.constraints:
            ret += c.size()
        return ret

    def valid(self):
        return (self).valid() # if the prove is valid

    def notvalid(self):   # if the prove is not valid
        return (self).notvalid()

    def and_conc(self, int): # for and conjunction
        int = int()
        ret = (self & int)
        ret = (self + int)
        return ret

    def or_conc(self, int): # for or conjunction
        int = int()
        ret = (self | int)
        return ret

    def push_on(self, int): # for ->
        int = int()
    #    ret = ( self -> int)
        int = self
        return int

    def count_solutions(self, lists=[]): # for overall solution
        if lists:
            T = (self + lists)
        else:
            T = (self.c)

        if not T.satisfiable():
            return False

        return dsharp(executable='bin').model_count()


# we hope this works
# yours
# YU & Zhang & LI & Bao