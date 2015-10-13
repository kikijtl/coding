'''
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string 
containing only letters a-z or .. A . means it can represent any one letter.

For example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

You should be familiar with how a Trie works. If not, please work on this problem: 
Implement Trie (Prefix Tree) first.
'''


class TrieNode(object):
    def __init__(self):
        self.leaves = {}
        

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for char in word:
            if char not in current.leaves:
                current.leaves[char] = TrieNode()
            current = current.leaves[char]
        current.leaves[''] = TrieNode()  # Mark the end of the word
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        current = self.root
        return self._searchHelper(word, 0, current)
        
        
        
    def _searchHelper(self, word, start, current):
        if not current.leaves:
            return False
        if start == len(word):
            return '' in current.leaves
        if word[start] in current.leaves:
            current = current.leaves[word[start]]
            return self._searchHelper(word, start+1, current)
        elif word[start] == '.':
            for leaf in current.leaves:
                if self._searchHelper(word, start+1, current.leaves[leaf]):
                    return True
        return False
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")


if __name__ == '__main__':
    test = WordDictionary()
#     test.addWord("a")
#     test.addWord("a")
#     print test.search(".")
#     print test.search("a")
#     print test.search("aa")
#     print test.search("a")
#     print test.search(".a")
#     print test.search("a.")
    test.addWord("a")
    test.addWord("ab")
    print test.search("a")
    print test.search("a.")
    print test.search("ab")
    print test.search(".a")
    print test.search(".b")
    print test.search("ab.")
    print test.search(".")
    print test.search("..")