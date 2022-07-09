class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        if len(sentence)<26:
            return False
        else:
            for i in range(97, 123):
                isFound = False
                for j in sentence:
                    if i==ord(j):
                        isFound=True
                if not isFound:
                    return False
            return True
                
        