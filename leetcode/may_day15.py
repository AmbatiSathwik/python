class Solution:
    def is_integer(self,s):
        try:
            k = int(s)
            return True
        except:
            return False
    def is_decimal(self,s):
        if 'inf' in s or 'Infinity' in s:
            return False
        try:
            k = float(s)
            return True
        except:
            return False
    def isNumber(self, s: str) -> bool:
        if 'e' in s or 'E' in s:
            
            try:
                k = s.index('e')
                if 'e' in s[k+1:] or 'E' in s[k+1:]:
                    return False
                if k != 0 and k != int(len(s))-1:
                    k1 = self.is_decimal(s[:k])
                    k2 = self.is_integer(s[k+1:])
                    return k1 and k2
                else:
                    return False
            except:
                k = s.index('E')
                if 'e' in s[k+1:] or 'E' in s[k+1:]:
                    return False
                if k != 0 and k != int(len(s))-1:
                    k1 = self.is_decimal(s[:k])
                    k2 = self.is_integer(s[k+1:])
                    return k1 and k2
                else:
                    return False
        else:
            return self.is_integer(s) or self.is_decimal(s)
        
