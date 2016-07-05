import re

class Extractor():
    def __init__(self):

        self.TYPE_INT_NUMERAL = "[0-9][0-9]*"
        self.TYPE_STRING = "[a-zA-Z][_a-zA-Z0-9]*"
        self.TYPE_SYMBOL_ASSINGNMENT = "="
        self.TYPE_SYMBOL_ENDLINE = ";"

    def extracting_lexames(self,text):
        aux = []
        aux = re.findall(re.compile(self.TYPE_STRING), text)
        aux += re.findall(re.compile(self.TYPE_SYMBOL_ASSINGNMENT), text)
        aux += re.findall(re.compile(self.TYPE_INT_NUMERAL), text)
        aux += re.findall(re.compile(self.TYPE_SYMBOL_ENDLINE), text)

        return  aux








