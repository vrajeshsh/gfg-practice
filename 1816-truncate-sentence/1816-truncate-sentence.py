class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        count, word, new_str = 0, "", ""
        for ch in s+" ":
            if ch.isalpha():
                word+=ch
            elif word!="":
                new_str+=word
                count+=1
                if count==k:
                    return new_str
                new_str+=" "
                word=""
        