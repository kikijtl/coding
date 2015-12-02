# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
# 
# a) it                      --> it    (no abbreviation)
# 
#      1
# b) d|o|g                   --> d1g
# 
#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n
# 
#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
# 
# Example: 
# Given dictionary = [ "deer", "door", "cake", "card" ]
# 
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbr_dict = {}
        for word in dictionary:
            abbr = self._getAbbreviation(word)
            if abbr not in self.abbr_dict:
                self.abbr_dict[abbr] = word
            elif self.abbr_dict[abbr] != word:
                self.abbr_dict[abbr] = False

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self._getAbbreviation(word)
        if abbr not in self.abbr_dict or self.abbr_dict[abbr] == word:
            return True
        return False
    
    def _getAbbreviation(self, word):
        num = len(word) - 2
        if num > 0:
            abbr = word[0] + str(num) + word[-1]
        else:
            abbr = word
        return abbr

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")