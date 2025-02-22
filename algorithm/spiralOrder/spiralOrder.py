
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n -1
        top = 0
        bottom = m -1
        result = []

        while True:
            if left > right:
                break
            for j in range (left ,right + 1):
                result.append(matrix[top][j])
            top += 1 

            if top > bottom:
                break
            for i in range (top,bottom + 1):
                result .append(matrix[i][right]) 
            right-=1
            if right < left:
                break
            for j in range(right,left):
                result.append(matrix[bottom][j])
            bottom-=1
            if bottom < top:
                break
            for i in range(bottom,top):
                result.append(matrix[i][left]) 
            left+=1

