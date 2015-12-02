# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.
# 
# Write a function to determine if the starting player can guarantee a win.
# 
# For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".
# 
# Follow up:
# Derive your algorithm's runtime complexity.


class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2: return False
        self.table = {}
        return self.canWinHelper(s)
        
    def canWinHelper(self, s):
        if s not in self.table:
            i = 1
            self.table[s] = False
            while i < len(s):
                if s[i] == s[i-1] == '+' and not self.canWinHelper(s[:i-1]+'--'+s[i+1:]):
                    self.table[s] = True
                i += 1
        return self.table[s]
    