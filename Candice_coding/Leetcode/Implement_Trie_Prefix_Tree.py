'''
Implement a trie with insert, search, and startsWith methods.
Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.leaves = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for char in word:
            if char not in current.leaves:
                current.leaves[char] = TrieNode()
            current = current.leaves[char]
        current.leaves[''] = TrieNode()  # Mark the end of a word


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        leaf = self._leavesForPrefix(word)
        if not leaf or '' not in leaf:
            return False
        return True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if self._leavesForPrefix(prefix):
            return True
        return False
        
        
    def _leavesForPrefix(self, prefix):
        """
        Returns all the leaves that start with the given prefix
        """
        current = self.root
        for char in prefix:
            if char not in current.leaves:
                return None
            current = current.leaves[char]
        return current.leaves


if __name__ == '__main__':
    mytrie = Trie()
    mytrie.insert("app")
    mytrie.insert("apple")
    mytrie.insert("beer")
    mytrie.insert("add")
    mytrie.insert("jam")
    mytrie.insert("rental")
    print mytrie.search("apps")
    print mytrie.search("app")
    print mytrie.search("ad")
    print mytrie.search("applepie")
    print mytrie.search("rest")
    print mytrie.search("jan")
    print mytrie.search("rent")
    print mytrie.search("beer")
    print mytrie.search("jam")
    print mytrie.startsWith("apps")
    print mytrie.startsWith("app")
    print mytrie.startsWith("ad")
    print mytrie.startsWith("applepie")
    print mytrie.startsWith("rest")
    print mytrie.startsWith("jan")
    print mytrie.startsWith("rent")
    print mytrie.startsWith("beer")
    print mytrie.startsWith("jam")