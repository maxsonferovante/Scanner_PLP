import re

from extracting_lexemas import Extractor


def tokens_ident(lexeme):
    if tokens_reserved.has_key(lexeme):
        return  False
    elif re.findall(re.compile(ex.TYPE_STRING),lexeme):
        return True

    return  False

def tokens_numeral_int(lexeme):
    if re.findall(re.compile(ex.TYPE_INT_NUMERAL),lexeme):
        return  True
    return  False

myCode = open("myCode.txt").readlines()

tokens_reserved = {'main':'RESERVED',
                   'return':'RESERVED',
                   'include':'RESERVED',
                   'stdio':'RESERVED'
                   }
tokens_assing = {'=': 'ASSIGN_OP'}
tokens_type_numeral = {'int': 'TYPE','float':'TYPE'}
tokens_end_line = {';': 'END_LINE'}

ex = Extractor()

for line in range(0,len(myCode)):
    lexemes = ex.extracting_lexames(myCode[line])
    if lexemes:
        ## int var = 10;
        ind = 0
        while  ind<len(lexemes):
            ##if tokens_type_numeral.has_key(lexemes[ind]) and ind + 1 < len(lexemes) and tokens_ident(lexemes[ind +1]):
            ##    print "O token ",lexemes[ind]," esta associado a ", lexemes[ind+1]
            if tokens_ident(lexemes[ind]) and ind + 2 < len(lexemes) and tokens_numeral_int(lexemes[ind+2]):
                print "O token ", lexemes[ind], " esta associado a ", lexemes[ind + 2]
            ind +=1
