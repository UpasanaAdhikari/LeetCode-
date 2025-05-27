class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        div=1
        while x >= 10 * div:
            div *= 10
        while x:
            end=x%10
            front=x/div  
            if end !=front:  #check value are same or not
                return False
            x=(x%div)//10 #removes first and last number
            div =div /100 # upades from2 fewer digits
        return True
    


        """
        :type x: int
        :rtype: bool
        """
        