#User function template for Python 3

class Solution:
    def convertRoman(self, n):
        #Code here
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[n // 1000] + C[(n % 1000) // 100] + X[(n % 100) // 10] + I[n % 10]

#{ 
#  Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        print(ob.convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends