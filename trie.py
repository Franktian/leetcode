class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root

        for w in word:
            if not w in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.word = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root

        for w in word:
            if not w in node.children:
                return False
            node = node.children[w]
        return node.word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        node = self.root

        for w in prefix:
            if not w in node.children:
                return False
            node = node.children[w]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)