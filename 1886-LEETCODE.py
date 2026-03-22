class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rot90(org_mat):
            for  i in range(len(org_mat)):
                for j in range(i,len(org_mat[0])):
                    org_mat[i][j] , org_mat[j][i] = org_mat[j][i] , org_mat[i][j]
            row_num = 0 
            for row in org_mat:
                org_mat[row_num] = row[::-1]
                row_num+=1
            return org_mat


        for i in range(4):
            if rot90(mat) == target:
                return True
        return False
        
