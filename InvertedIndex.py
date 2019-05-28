'''
Created on May 23, 2019

@author: ashto
'''
import corpus
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from _collections import defaultdict
class InvertedIndex:
    def __init__(self, corp, urlList):
        self.outFile = "index.txt"
        self.corpus = corp
        self.url_list = urlList
    def wordFrequency(self, doc):
        tokenizer = RegexpTokenizer("\b[^\d\W]+\b")
        tokens = tokenizer.tokenize(doc)
        result = defaultdict(int)
        
        for word in tokens:
            result[word.lower()] += 1
        for i in result.items():
            result[i[0]] = j[1] / len(tokens)
        return result
    def createIndex(self):
        for i in self.url_list:
            fileAddr = self.corpus.get_file_name(i)
            if fileAddr != None:
                f = open(fileAddr)
                docStr = f.read()
                doc = BeautifulSoup(docStr.encode('utf-8'), "html-parser").get_text()
                

            