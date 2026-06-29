class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_parts = []
        for s in strs:
            encoded_parts.append(str(len(s)) + "#" + s)
        return "".join(encoded_parts)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        n = len(s)
        while i < n:
            # find the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1                     
            decoded.append(s[i:i+length])
            i += length                  
        return decoded
