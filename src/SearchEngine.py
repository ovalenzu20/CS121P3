'''
Created on May 30, 2019

@author: omarvalenzuela
'''
import json

class SearchEngine:
    
    def getJSON(self, path):
        try:
            oJSON = open(path, 'r')
            return json.load(oJSON)
        
        finally:
            oJSON.close()
            
    
if __name__ == "__main__":
    s = SearchEngine()
    jsonFile = s.getJSON("/WEBPAGES_RAW/bookkeeping.json")
    print(jsonFile)