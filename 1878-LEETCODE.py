class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        st = set()

        def addToSet(val):
            st.add(val)
            if len(st) > 3:
                st.remove(min(st))

        for r in range(m):
            for c in range(n):

                # every cell itself (side = 0 rhombus)
                addToSet(grid[r][c])

                side = 1
                while r - side >= 0 and r + side < m and c - side >= 0 and c + side < n:
                    s = 0

                    for k in range(side):
                        s += grid[r - side + k][c + k]     # top → right
                        s += grid[r + k][c + side - k]     # right → bottom
                        s += grid[r + side - k][c - k]     # bottom → left
                        s += grid[r - k][c - side + k]     # left → top

                    addToSet(s)
                    side += 1

        return sorted(st, reverse=True) 
