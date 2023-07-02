# tokens = ["import", "math", "NEW_LINE", "def", "sumOfTwoCubes", "(", "n", ")", ":", "NEW_LINE", "INDENT", "lo", "=", "1", "NEW_LINE", "hi", "=", "round", "(", "math", ".", "pow", "(", "n", ",", "1", "/", "3", ")", ")", "NEW_LINE", "while", "(", "lo", "<=", "hi", ")", ":", "NEW_LINE", "INDENT", "curr", "=", "(", "lo", "*", "lo", "*", "lo", "+", "hi", "*", "hi", "*", "hi", ")", "NEW_LINE", "if", "(", "curr", "==", "n", ")", ":", "NEW_LINE", "INDENT", "return", "True", "NEW_LINE", "DEDENT", "if", "(", "curr", "<", "n", ")", ":", "NEW_LINE", "INDENT", "lo", "+=", "1", "NEW_LINE", "DEDENT", "else", ":", "NEW_LINE", "INDENT", "hi", "-=", "1", "NEW_LINE", "DEDENT", "DEDENT", "return", "False", "NEW_LINE", "DEDENT", "N", "=", "28", "NEW_LINE", "if", "(", "sumOfTwoCubes", "(", "N", ")", ")", ":", "NEW_LINE", "INDENT", "print", "(", "\" True \"", ")", "NEW_LINE", "DEDENT", "else", ":", "NEW_LINE", "INDENT", "print", "(", "\" False \"", ")", "NEW_LINE", "DEDENT"]
# codeStr = codeToken2codeStr.codeToken2codeStr(tokens)
def codeStr2codeToken(code_string):

    import io
    import tokenize
    import ast
    import codeToken2codeStr

    code_bytes = code_string.encode('utf-8')
    tokens = []

    for token in tokenize.tokenize(io.BytesIO(code_bytes).readline):
        if token.type == tokenize.NEWLINE:
            tokens.append('NEW_LINE')
        elif token.type == tokenize.INDENT:
            tokens.append('INDENT')
        elif token.type == tokenize.DEDENT:
            tokens.append('DEDENT')
        else:
            tokens.append(token.string)
     
        if 'utf-8' in tokens:# 'utf-8' 토큰 삭제
            tokens = [x for x in tokens if x != 'utf-8']
        if '\n' in tokens:# '\n' 토큰 삭제
            tokens = [x for x in tokens if x != '\n']
        if '' in tokens:# '' 토큰 삭제
            tokens = [x for x in tokens if x != '']

    return tokens
    #print(tokens)

