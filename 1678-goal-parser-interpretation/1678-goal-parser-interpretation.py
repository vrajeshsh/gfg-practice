class Solution:
    def interpret(self, command: str) -> str:
        new_str = ""
        for ch in range(len(command)):
            if command[ch]=="G":
                new_str+="G"
            elif command[ch:ch+2]=="()":
                new_str+="o"
            elif command[ch:ch+4]=="(al)":
                new_str+="al"
        return new_str