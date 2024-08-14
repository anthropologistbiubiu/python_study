



def generateParenthesis(n):
    result = []
    def generator(n,close,open,cur):
        if len(cur) == 2*n:
            result.append(cur)
        if close < n:
            generator(n,close+1,open,cur+"(")
        if open < close:
            generator(n,close,open+1,cur+")")
    generator(n,0,0,"")
    return result


print(generateParenthesis(1))