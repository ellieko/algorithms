'''
271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

'''

class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """
        
        encoded = ""
        
        for s in strs:
            encoded += str(len(s)) + '#' + s
            
        return encoded
        

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0
        
        while i < len(s):
            j = i
            
            while s[j] != '#':
                j += 1
                
            length = int(s[i:j])
            
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))