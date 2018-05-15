import sys, re, time, pickle, os

class TrieNode(object):
    def __init__(self):
        self.children = [];
        self.counter = 0;

class ProtoTrie(object):
    def __init__(self, items=None):
        self.root = self.getNode()

    def __repr__(self):
        return "Trie (WIP) - {}".format(self.root)

    def _findIndex(self, item):
        return ord(item) - ord('a')

    def getNode(self):
        return TrieNode()

    def add(self, item):
        if item.isalpha() == False:
            return None
        node = self.root
        length = len(item)
        for level in range(length):
            index = self._findIndex(item[level])
            # if current character is not present
            if not node.children[index]:
                node.children[index] = self.getNode()
            node = node.children[index]

        # mark last node as leaf
        node.counter += 1

    def find(self, item):
        node = self.root
        length = len(item)
        for level in range(length):
            index = self._findIndex(item[level])
            if not node.children[index]:
                return False
            node = node.children[index]

        return node != None and node.counter

def get_words(filename):
    inputfile = open(filename).read()
    return inputfile.split('\n')

def autocomplete(prefix):
    # if os.path.exists('auto.p'):
        # Trie = pickle.load( open( "auto.p", "rb" ) )
    # else:
    test = []
    # words = get_words('/usr/share/dict/words')
    words = get_words('./dictionarytest.txt')

    #
    Trie = ProtoTrie()
    #

    for word in words:
        Trie.add(word.lower())

    print(Trie.find(prefix))
    # for word in words:
    #     if re.match(prefix, word):
    #         test.append(word)
    # print(re.match(prefix, words))
    # for word in words:
    #     if word.startswith(prefix):
    #         test.append(word)




    # pickle.dump(Trie, open( "auto.p", "wb" ))

    # print(Trie.find(prefix))



def benchmark(num_words):
    autocomplete
    pass

def main():
    """Perform main function."""
    start_time = time.time()
    autocomplete(sys.argv[1])
    print("--- %s seconds ---" % (time.time() - start_time))

    return


if __name__ == "__main__":
    main()
