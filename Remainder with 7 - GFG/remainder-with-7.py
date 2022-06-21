class Solution:
    #your task is to complete this function
    #Function should return the required answer
    #You are not allowed to convert string to integer
    def remainderWith7(self, num):
        #Code here
        series = [1, 3, 2, -1, -3, -2];
     
    # Index of next element
    # in series
        series_index = 0;
         
        # Initialize result
        result = 0;
         
        # Traverse num from end
        for i in range((len(num) - 1), -1, -1):
             
            # Find current digit of num
            digit = ord(num[i]) - 48;
             
            # Add next term to result
            result += digit * series[series_index];
             
            # Move to next term in series
            series_index = (series_index + 1) % 6;
             
            # Make sure that result
            # never goes beyond 7.
            result %= 7;
         
        # Make sure that remainder
        # is positive
         
        if (result < 0):
            result = (result + 7) % 7;
        return result;

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        ob=Solution()
        print(ob.remainderWith7(str))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends