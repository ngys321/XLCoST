def codeToken2codeStr(tokens):

    code = ""
    indentation_level = 0

    for token in tokens:
        if token == "NEW_LINE":
            code += "\n"
            code += "    " * indentation_level
        elif token == "INDENT":
            indentation_level += 1
            code += "    "
        elif token == "DEDENT":
            indentation_level -= 1
            code = code[:-4]
        else:
            code += token + " "

    codeStr = code.strip()

    return codeStr
    #print(codeStr)

# tokens = ["def", "maxPresum", "(", "a", ",", "b", ")", ":", "NEW_LINE", "INDENT", "X", "=", "max", "(", "a", "[", "0", "]", ",", "0", ")", "NEW_LINE", "for", "i", "in", "range", "(", "1", ",", "len", "(", "a", ")", ")", ":", "NEW_LINE", "INDENT", "a", "[", "i", "]", "+=", "a", "[", "i", "-", "1", "]", "NEW_LINE", "X", "=", "max", "(", "X", ",", "a", "[", "i", "]", ")", "NEW_LINE", "DEDENT", "Y", "=", "max", "(", "b", "[", "0", "]", ",", "0", ")", "NEW_LINE", "for", "i", "in", "range", "(", "1", ",", "len", "(", "b", ")", ")", ":", "NEW_LINE", "INDENT", "b", "[", "i", "]", "+=", "b", "[", "i", "-", "1", "]", "NEW_LINE", "Y", "=", "max", "(", "Y", ",", "b", "[", "i", "]", ")", "NEW_LINE", "DEDENT", "return", "X", "+", "Y", "NEW_LINE", "DEDENT", "A", "=", "[", "2", ",", "-", "1", ",", "4", ",", "-", "5", "]", "NEW_LINE", "B", "=", "[", "4", ",", "-", "3", ",", "12", ",", "4", ",", "-", "3", "]", "NEW_LINE", "print", "(", "maxPresum", "(", "A", ",", "B", ")", ")", "NEW_LINE"]
# tokens = ["mod", "=", "1000000007", "NEW_LINE", "def", "ValOfTheExpression", "(", "n", ")", ":", "NEW_LINE", "INDENT", "global", "mod", "NEW_LINE", "factorial", "=", "[", "0", "for", "i", "in", "range", "(", "n", "+", "1", ")", "]", "NEW_LINE", "factorial", "[", "0", "]", "=", "1", "NEW_LINE", "factorial", "[", "1", "]", "=", "1", "NEW_LINE", "for", "i", "in", "range", "(", "2", ",", "n", "+", "1", ",", "1", ")", ":", "NEW_LINE", "INDENT", "factorial", "[", "i", "]", "=", "(", "(", "factorial", "[", "i", "-", "1", "]", "%", "mod", ")", "*", "(", "i", "%", "mod", ")", ")", "%", "mod", "NEW_LINE", "DEDENT", "dp", "=", "[", "0", "for", "i", "in", "range", "(", "n", "+", "1", ")", "]", "NEW_LINE", "dp", "[", "1", "]", "=", "1", "NEW_LINE", "for", "i", "in", "range", "(", "2", ",", "n", "+", "1", ",", "1", ")", ":", "NEW_LINE", "INDENT", "dp", "[", "i", "]", "=", "(", "(", "dp", "[", "i", "-", "1", "]", "%", "mod", ")", "*", "(", "factorial", "[", "i", "]", "%", "mod", ")", ")", "%", "mod", "NEW_LINE", "DEDENT", "return", "dp", "[", "n", "]", "NEW_LINE", "DEDENT", "if", "__name__", "==", "' _ _ main _ _ '", ":", "NEW_LINE", "INDENT", "n", "=", "4", "NEW_LINE", "print", "(", "ValOfTheExpression", "(", "n", ")", ")", "NEW_LINE", "DEDENT"]
# codeStr = codeToken2codeStr(tokens)
# print(codeStr)



# tokens = ["import", "math", "NEW_LINE", "def", "sumOfTwoCubes", "(", "n", ")", ":", "NEW_LINE", "INDENT", "lo", "=", "1", "NEW_LINE", "hi", "=", "round", "(", "math", ".", "pow", "(", "n", ",", "1", "/", "3", ")", ")", "NEW_LINE", "while", "(", "lo", "<=", "hi", ")", ":", "NEW_LINE", "INDENT", "curr", "=", "(", "lo", "*", "lo", "*", "lo", "+", "hi", "*", "hi", "*", "hi", ")", "NEW_LINE", "if", "(", "curr", "==", "n", ")", ":", "NEW_LINE", "INDENT", "return", "True", "NEW_LINE", "DEDENT", "if", "(", "curr", "<", "n", ")", ":", "NEW_LINE", "INDENT", "lo", "+=", "1", "NEW_LINE", "DEDENT", "else", ":", "NEW_LINE", "INDENT", "hi", "-=", "1", "NEW_LINE", "DEDENT", "DEDENT", "return", "False", "NEW_LINE", "DEDENT", "N", "=", "28", "NEW_LINE", "if", "(", "sumOfTwoCubes", "(", "N", ")", ")", ":", "NEW_LINE", "INDENT", "print", "(", "\" True \"", ")", "NEW_LINE", "DEDENT", "else", ":", "NEW_LINE", "INDENT", "print", "(", "\" False \"", ")", "NEW_LINE", "DEDENT"]
# codeStr = codeToken2codeStr(tokens)
#print(codeStr)
#
# tmp = {}
# tmp['codeStr'] = codeStr
# print(tmp)
#
# 
# exec(codeStr) : codeStr 을 직접 실행시켜볼 수 있음.