'''
Created on May 29, 2019

@author: omarvalenzuela
'''

from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import RegexpTokenizer
from _collections import defaultdict
from _contextvars import Token
from lxml.html.diff import token

class Tokenizer:
    
    def generateFilePath(self, folderNum, fileNum):
        return f"../WEBPAGES_RAW/{folderNum}/{fileNum}"
    
        
    
    def readFile(self, fileName):
        try:
            oFile = open(fileName, 'r')
            text = oFile.read()
            return text.encode('utf-8')
        except:
            return None
        
        finally:
            oFile.close()
            
            
    def tokenizeFile(self, rawFile):
        #return a list of tokens
        soup = BeautifulSoup(rawFile, 'lxml')
        tokens = nltk.word_tokenize(soup.get_text().lower())
        return [w.lower() for w in tokens if w.isalnum() and not any(char.isdigit() for char in w)]
    
    
    def populateTokenDictFrequencies(self, tokens):
        tokenDict = defaultdict(int)
        for token in tokens:
            tokenDict[token] += 1
            
        return tokenDict

    def generateTokenDict(self, folderNum, fileNum):
        filePath = self.generateFilePath(folderNum, fileNum)
        rawFile = self.readFile(filePath)
        if rawFile != None:
            tokens = self.tokenizeFile(rawFile)
            tokenFreq = self.populateTokenDictFrequencies(tokens)
            return tokenFreq
        
        
        
# t = Tokenizer()
# print(t.generateTokenDict(0, 4))
    
    
        