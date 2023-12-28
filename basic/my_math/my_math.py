


class mathTool:
    def __init__(self):
        pass
    def sub(self,num1,num2):
        return num1 - num2
    def sum(self,*args):
        result = 0
        for num in args:
            result += num
        return result
