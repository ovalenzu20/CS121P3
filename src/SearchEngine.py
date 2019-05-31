'''
Created on May 30, 2019

@author: omarvalenzuela
'''
import json
from Tokenizer import Tokenizer
from InvertedIndex import InvertedIndex
from _collections import defaultdict


class SearchEngine:
    
    def __init__(self):
        self.query = None
        self.urls = self.getJSON("../WEBPAGES_RAW/bookkeeping.json")
        self.II = InvertedIndex()
        self.T = Tokenizer()
        
    def run(self):
        invertedIndex = InvertedIndex.loadPickle(InvertedIndex.pickleName)
        userInput = input("Please enter a query: ")
        self.query = userInput
        print("To end the Search Engine, please enter the letter 'q'. \n")
        
        while userInput != "q":
            self.search(self.query, invertedIndex)
            
            userInput = input("Please enter a query: ")
            self.query = userInput
            print("To end the Search Engine, please enter the letter 'q'. \n")

            
            
    def search(self, query, invertedIndex):
        tokens = self.T.tokenizeText(query)
        documentScores = self.getRelevantDocScores(tokens, invertedIndex)
        self.displayTopKSearchResults(documentScores, self.urls, 20)
            
    
    def getRelevantDocScores(self, tokens, invertedIndex):
        documentScores = defaultdict(float)
        for token in tokens:
            for filePath in invertedIndex[token]:
                TFIDF = invertedIndex[token][filePath][2]
                documentScores[filePath] += TFIDF
        return documentScores
                
    
    def displayTopKSearchResults(self, documentScores, urls, K):
        decreasingOrder = sorted(documentScores, key = lambda val: documentScores[val], reverse = True)[:K]
        ranking = 1
        print(f"Total results found: {len(documentScores)}")
        print(f'Displaying top {len(decreasingOrder)} results for the query "{self.query}":')
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
 
 
    def outputStats(self):
        invertedIndex = self.II.loadPickle(self.II.pickleName)
        queries = ["Informatics", "Mondego", "Irvine", "artificial intelligence", "computer science"]
        milestone2 = open("Milestone2.txt", 'w+')

        for query in queries:
            self.query = query
            tokens = self.T.tokenizeText(query)
            documentScores = self.getRelevantDocScores(tokens, invertedIndex)
            self.writeResults(milestone2, documentScores, self.urls, 20)
            
        milestone2.close()
    
    def writeResults(self, fileToWrite, documentScores, urls, K):
        decreasingOrder = sorted(documentScores, key = lambda val: documentScores[val], reverse = True)[:K]
        ranking = 1
        
        fileToWrite.write(f"Total results found: {len(documentScores)} \n")
        fileToWrite.write(f'Displaying top {len(decreasingOrder)} results for the query "{self.query}":\n')
        for filePath in decreasingOrder:
            refinedPath = self.refineFilePath(filePath)
            fileToWrite.write(f"\t{ranking}. {urls[refinedPath]}\n")
            ranking += 1
            
        fileToWrite.write("\n")
            
 
if __name__ == "__main__":
    s = SearchEngine()
#     s.run()
    s.outputStats()
    