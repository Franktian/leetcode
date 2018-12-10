class TrieNode(object):

    def __init__(self, val):
        self.children = {}
        self.word = False
        self.val = val


class Trie(object):
    def __init__(self):
        self.root = TrieNode('#')

    def insert(self, word):
        root = self.root

        for c in word:
            if not c in root.children:
                root.children[c] = TrieNode(c)
            root = root.children[c]

        root.word = True


def autoComplete(words, word):
    trie = Trie()

    for w in words:
        trie.insert(w)

    res = []
    # Find the last prefix of word
    root = trie.root
    for c in word:
        if not c in root.children:
            return []
        root = root.children[c]

    print "After rooting {}".format(root.val)

    # N-ary tree DFS traversal
    def dfs(node, path):
        if node:
            path += node.val
            if node.word == True:
                res.append(word[:-1] + path)

            for _, trie in node.children.iteritems():
                dfs(trie, path)
    
    dfs(root, '')

    return res

if __name__ == '__main__':
    print autoComplete(['graph', 'grape','apple', 'banana', 'typing', 'gra'], 'grap')
