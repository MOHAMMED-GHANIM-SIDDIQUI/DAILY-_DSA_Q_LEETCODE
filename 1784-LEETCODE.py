class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # 11110001000 ----> valid 
        # 0000011111--->not valid
        flag = True
        for i in s:
            if i != '1' and flag:
                flag=False # zero is here
                continue
            if i =='1' and flag==False: # getting 1 after zero 
                return flag 
        return True        
