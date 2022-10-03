class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #finding the length of matrix row
        m=len(matrix)
        #finding the length of columns
        n=len(matrix[0])
        #calculating the low value as index is zero at first
        l=0
        #calculating the hight value
        h=(m*n)-1
        
        #base condition for binary search
        while l<=h:
            #calculating the mid element without integer overflow
            mid=l+(h-l)//2
            #accessing the element in a two dimensional matrix as follows:
            num= matrix[mid//n][mid%n]
            
            #if find the target return True
            if num==target:
                return True
            #if the target value is less then the num value
            elif target<num:
                h=mid-1
            #if target value is greater than num value    
            else:
                l=mid+1
                
        return False        
                
            