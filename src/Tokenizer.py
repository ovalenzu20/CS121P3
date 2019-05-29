'''
Created on May 29, 2019

@author: omarvalenzuela
'''

from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import RegexpTokenizer
from _collections import defaultdict

class Tokenizer:
    
    def generateFilePath(self, folderNum, fileNum):
        return f"WEBPAGES_RAW/{folderNum}/{fileNum}"
    
    def readFile(self, fileName):
        try:
            oFile = open(fileName, 'r')
            text = oFile.read()
            return text.encode()
        
        finally:
            oFile.close()
            
            
    def tokenizeFile(self, rawFile):
        #return a list of tokens
        soup = BeautifulSoup(rawFile, 'lxml')
        return nltk.word_tokenize(soup.get_text().lower())
    
    
    def populateTokenDictFrequencies(self, tokens):
        tokenDict = defaultdict(int)
        for token in tokens:
            tokenDict[token] += 1
            
        return tokenDict
    
    
    def generateTFScore(self, tokenDict, tokenCount):
        for token in tokenDict.items():
            tokenDict[token[0]] = token[1] / tokenCount
            
        return tokenDict
    
    def generateIDFScore(self):
        pass

    def generateTokenDict(self, folderNum, fileNum):
        filePath = self.generateFilePath(folderNum, fileNum)
        rawFile = self.readFile(filePath)
        tokens = self.tokenizeFile(rawFile)
        tokenFreq = self.populateTokenDictFrequencies(tokens)
        
        return self.generateTFScore(tokenFreq, len(tokens))
        
        
        
        
    
    
            
    
    
    
    
        