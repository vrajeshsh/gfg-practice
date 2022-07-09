class Solution:
    def sortSentence(self, s: str) -> str:
        sent = ""
        new = s.split(" ")
        for i in range(100):
            for j in new:
                if j[-1]==str(i):
                    sent+=j[0:-1]+" "
        return sent.strip()