class Solution:
    def toLowerCase(self, s: str) -> str:
        new = ""
        for ch in s:
            if ch.isupper():
                new+=chr(ord(ch)+32)
            else:
                new+=ch
        return new
                