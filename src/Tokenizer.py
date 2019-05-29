'''
Created on May 29, 2019

@author: omarvalenzuela
'''

from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import RegexpTokenizer
from _collections import defaultdict
import os

class Tokenizer:
    
    def generateFilePath(self, folderNum, fileNum):
        cur_path = os.path.dirname(__file__)
        new_path = os.path.relpath(f'..\\WEBPAGES_RAW\\{folderNum}\\{fileNum}', cur_path)
        return new_path
    
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
    
    
    def generateTFScore(self, tokenDict, tokenCount):
        for token in tokenDict.items():
            tokenDict[token[0]] = token[1] / tokenCount
            
        return tokenDict

    def generateTokenDict(self, folderNum, fileNum):
        filePath = self.generateFilePath(folderNum, fileNum)
        rawFile = self.readFile(filePath)
        if rawFile != None:
            tokens = self.tokenizeFile(rawFile)
            tokenFreq = self.populateTokenDictFrequencies(tokens)
            return self.generateTFScore(tokenFreq, len(tokens))
        return "File Not Readable"
        
            
    
    
    
    
        