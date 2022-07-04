class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for sent in sentences:
            count = 0
            for ch in sent:
                if ch==" ":
                    count+=1
            if count>maxi:
                maxi = count
        return maxi+1