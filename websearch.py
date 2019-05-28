'''
Created on May 23, 2019

@author: ashto
'''

class searchEngine:
    
    def __init__(self, invDic):
        self.invertedIndex = invDic
        
    def simpleSearch(self, query, num):
        '''Search based upon single words'''
        pass
    
    def phraseSearch(self, query, num):
        '''Search based on phrases'''
        pass
        
    def search(self, query, num = 10):
        if len(query) > 1:
            return self.phraseSearch(query, num)
        return self.simpleSearch(query, num)
            