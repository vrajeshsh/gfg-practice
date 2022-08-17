class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        word, final = "", []
        thisdict =  {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.",
                     "g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.",
                     "o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-",
                     "w":".--","x":"-..-","y":"-.--","z":"--.."}
        for i in words:
            for j in i:
                word+=thisdict[j]
            print(word)
            if word not in final:
                final.append(word)
            word=""
        return len(final)