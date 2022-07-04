class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_str, word = "", ""
        for ch in address+" ":
            if ch.isdigit():
                word+=ch
            elif word!="":
                if ch==".":
                    word+="[.]"
                new_str+=word
                word=""
        return new_str