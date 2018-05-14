import sys, re, time, pickle, os

class TrieNode(object):
    def __init__(self, item=None, freq=None):
        self.links = [None] * 26
        self.freq = freq

    def __repr__(self):
        return '[NODE - {}]'.format(self.data)

class ProtoTrie(object):
    def __init__(self, items=None):
        self.root = self.getNode()

    def __repr__(self):
        return "Trie (WIP) - {}".format(self.root)

    def _findIndex(self, item):
        return ord(item) - 97

    def getNode():
        return TrieNode()

    def add(self, item, node=None):
        if node == None:
            node = self.root
        if not item.isalpha():
            return

        index = self._findIndex(item[0])

        # If first char not in array
        if node.links[index] == None:
            # if not last character
            if len(item) != 1:
                newNode = TrieNode(item[0])
                node.links[index] = newNode
                self.add(item[1:], newNode)
            # Else, end of the line
            else:
                newNode = TrieNode(item[0], 1)
                node.links[index] = newNode
                return
        else:
            if len(item) != 1:
                newNode = node.links[index]
                self.add(item[1:], newNode)
            else:
                node.links[index].freq = 1
                return

    def find(self, item, node=None, word=''):
        if node == None:
            node = self.root
        if item == '':
            return self.traverse(node, word)

        index = self._findIndex(item[0])

        if node.links[index] != None:
            newNode = node.links[index]
            word += newNode.data
            return self.find(item[1:], newNode, word)

    def traverse(self, node, word, wordlist=[]):
        if any(node.links):
            for link in node.links:
                if link != None:
                    if link.freq:
                        word += link.data
                        wordlist.append(word)
                        if any(node.links[self._findIndex(word[-1])].links):
                            self.traverse(link, word, wordlist)
                        return
                    else:
                        self.traverse(link, word + link.data)
        return wordlist



def get_words(filename):
    inputfile = open(filename).read()
    return inputfile.split('\n')

def autocomplete(prefix):
    # if os.path.exists('auto.p'):
        # Trie = pickle.load( open( "auto.p", "rb" ) )
    # else:
    test = []
    words = get_words('/usr/share/dict/words')
    #
    # Trie = ProtoTrie()
    #
    # for word in words:
    #     Trie.add(word.lower())
    # for word in words:
    #     if re.match(prefix, word):
    #         test.append(word)
    # print(re.match(prefix, words))
    # for word in words:
    #     if word.startswith(prefix):
    #         test.append(word)

    print(test)



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
