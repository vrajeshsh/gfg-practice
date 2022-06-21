# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
CHARS = 26
def remAnagram(str1,str2):
    #add code here
    count1 = [0]*CHARS
    count2 = [0]*CHARS
 
    # count frequency of each character
    # in first string
    i = 0
    while i < len(str1):
        count1[ord(str1[i])-ord('a')] += 1
        i += 1
 
    # count frequency of each character
    # in second string
    i =0
    while i < len(str2):
        count2[ord(str2[i])-ord('a')] += 1
        i += 1
 
    # traverse count arrays to find
    # number of characters
    # to be removed
    result = 0
    for i in range(26):
        result += abs(count1[i] - count2[i])
    return result
            
    
    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends