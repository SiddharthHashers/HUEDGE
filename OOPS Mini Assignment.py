from itertools import combinations
from collections import Counter

class StringClassa:
    def __init__(self,f):
        self.String=f
    def lenmethod(self):
        return len(self.String)
    def strtolist(self):
        listblock=[]
        for i in self.String:
            listblock.append(i)
        return listblock

class PairPossible(StringClassa):
    def __init__(self,a):
        self.pairstring=a
    def allpair(self):
        com=combinations(self.pairstring,2)
        output=[]
        for i in com:
            output.append("".join(i))
        return list(set(output))
class SearchCommonelement():
    def __init__(self,a,b):
        self.commonele=a
        self.commonelee=b
    def pairStringclass(self):
        str1=self.commonele
        str2=self.commonelee
        d1=Counter(str1)
        d2=Counter(str2)
        cdict=d1&d2
        cchar=list(cdict.elements())
        outputs=[]
        for i in cchar:

            outputs.append("".join(i))
        return list(set(outputs))
class uniqueopair(PairPossible):
    def __init__(self,b):
        self.o=b
    def sumofpair(self):
        d={}
        ss=self.o
        for i in ss:
            cal=int(i[0])+int(i[1])
            if cal not in d:
                d[cal]=[i]
            else:
                d[cal].append(i)
            count=0
            for i in d:
                if len(d[i])==1:
                    count=count+1
        return count




s1="Siddharth"
s2="Kalidas"
s3="12314532"
obj_a=StringClassa(s1)
print(obj_a.lenmethod())
print(obj_a.strtolist())
obj_c=PairPossible(s3)
print(obj_c.allpair())
obj_p=SearchCommonelement(s1,s2)
print(obj_p.pairStringclass())
obj_pairunique=uniqueopair(obj_c.allpair())
print(obj_pairunique.sumofpair())


