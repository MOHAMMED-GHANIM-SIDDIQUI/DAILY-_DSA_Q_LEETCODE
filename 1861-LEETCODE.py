class Solution:
    def rotateTheBox(self, box):
        m, n = len(box), len(box[0])
        
        # Step 1: apply gravity
        for i in range(m):
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    empty = j - 1
                elif box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][empty] = '#'
                    empty -= 1
        
        # Step 2: rotate
        res = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = box[i][j]
        
        return res


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        r, c = len(box), len(box[0])
        rotate = [['.'] * r for _ in range(c)]
        
        for i in range(r):
            bottom = c - 1
            for j in range(c - 1, -1, -1):
                if box[i][j] == '*':
                    rotate[j][r - 1 - i] = '*'
                    bottom = j - 1
                elif box[i][j] == '#':
                    rotate[bottom][r - 1 - i] = '#'
                    bottom -= 1
        
        return rotate



class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        for i in range(m):
            k = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] != '.':
                    if box[i][j] == '*':
                        k = j - 1
                    else:
                        box[i][k], box[i][j] = box[i][j], box[i][k]
                        k -= 1
        
        rotated = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - i - 1] = box[i][j]
        
        for j in range(m):
            q = deque()
            for i in range(n - 1, -1, -1):
                if rotated[i][j] == '*':
                    q.clear()
                elif rotated[i][j] == '.':
                    q.append(i)
                elif q:
                    rotated[q.popleft()][j] = '#'
                    rotated[i][j] = '.'
                    q.append(i)
        
        return rotated
