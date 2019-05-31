'''
Created on May 30, 2019

@author: omarvalenzuela
'''
import json
from Tokenizer import Tokenizer
from InvertedIndex import InvertedIndex
from _collections import defaultdict

class SearchEngine:
    

    def run(self):
        II = InvertedIndex()
        T = Tokenizer()
        invertedIndex = II.loadPickle(II.pickleName)
        urls = self.getJSON("../WEBPAGES_RAW/bookkeeping.json")
        
        userInput = input("Please enter a query")
        print("To end the Search Engine, please enter the letter 'q'.")
        
        while userInput != "q":
            tokens = T.tokenizeText(userInput)
            documentScores = self.getRelevantDocScores(tokens, invertedIndex)
            self.displayTopKSearchResults(documentScores, urls, 20)
            
            userInput = input("Please enter a query: ")
            print("To end the Search Engine, please enter the letter 'q'.")
            
    
    def getRelevantDocScores(self, tokens, invertedIndex):
        documentScores = defaultdict(float)
        for token in tokens:
            for filePath in invertedIndex[token]:
                TFIDF = invertedIndex[token][filePath][2]
                documentScores[filePath] += TFIDF
        return documentScores
                
    
    #set counter to exit after K iterations -- while loop
    def displayTopKSearchResults(self, documentScores, urls, K):
        decreasingOrder = sorted(documentScores, key = lambda K: documentScores[K], reverse = True)
        if len(decreasingOrder) > K:
            ranking = 1
            print(f"Displaying top {K} results:")
            for filePath in decreasingOrder:
                refinedPath = self.refineFilePath(filePath)
                print(f"\t{ranking}. {urls[refinedPath]}")
                ranking += 1
        
            
            
    def getJSON(self, path):
        try:
            oJSON = open(path, 'r')
            return json.load(oJSON)
        
        finally:
            oJSON.close()
            
    def refineFilePath(self, path):
        splitPath = path.split('/')
        return splitPath[2] + '/' + splitPath[3]
 
if __name__ == "__main__":
    s = SearchEngine()
    s.run()
    