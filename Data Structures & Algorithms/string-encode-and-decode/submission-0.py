class Solution:
    def encode(self, strs: List[str]) -> str:
        encode = []
        #We use the lenght of each string to encode
        for element in strs:
            encode.append(str(len(element)))#We append always first the lenght of the string
            encode.append(',')#We append the , to know the exactly number
            encode.append(element)
        return "".join(encode) #If it exist a "", this will be eliminated by join and only we have 0 denote this element
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        size = 0
        while(i < len(s)):
            if(s[i] != ','):
                size *= 10
                size += int(s[i])
                i += 1
            else:
                i += 1
                if size == 0:
                    result.append("")
                else:
                    result.append(s[i:i+size])
                i += size
                size = 0
        return result