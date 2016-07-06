import re

tokens_reserved = {"return":"RESERVED_RETURN",
                   "int":"TYPE_NUMERAL",
                   "{":"STARTING_BLOCK",
                   "}":"END_BLOCK",
                   ";":"END_LINE",
                   "=":"ASSIGNMENT",
                   "main()":"RESERVED_FUNCTION_MAIN"}

def munber_integer(text):
    if re.findall(re.compile("[1-9][0-9]*"),text):
        return True
    return False

def identifying_variables(text):
    if re.findall(re.compile("[a-zA-Z][_a-zA-Z0-9]*"),text):
        return True
    return False

def reserved_include(text):
    if re.findall(re.compile("[#][i][n][c][l][u][d][e][<][a-zA-z]*[.][a-zA-z]*[>]"),text):
        return True
    return False

def main():
    myCode = open("myCode.txt").read().split()

    for i in range(0,len( myCode)):
        if ";" in myCode[i] and myCode[i]!=";":
            myCode[i]= myCode[i][:-1]
            myCode.insert(i+1,";")

    resultado = []
    for i in range(0,len(myCode)):
        if tokens_reserved.has_key(myCode[i]):
            resultado.append((tokens_reserved[myCode[i]],myCode[i]))

        elif munber_integer(myCode[i]):
            resultado.append(("NUMBER_INTEGER",myCode[i]))

        elif identifying_variables(myCode[i]):
            resultado.append(("IDENTIFYINF_VARIABLES",myCode[i]))

        elif reserved_include(myCode[i]):
            resultado.append(("RESERVED_INCLUDE",myCode[i]))
        else:
            resultado.append(("LEXEME_UNKNOWN", myCode[i]))

    for token, lexeme in resultado:
        print token," : ",lexeme

main()


