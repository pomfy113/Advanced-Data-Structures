import sys, re, time, pickle, os

# Python program for insert and search
# operation in a Trie

class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None]*27
        self.end = False

class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self,ch):
        if(ch == '-'):
            return 26
        return ord(ch) - 97


    def insert(self,key):
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not node.children[index]:
                node.children[index] = self.getNode()
            node = node.children[index]

        # mark last node as leaf
        node.end = True

    def search(self, key):
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not node.children[index]:
                return False

            node = node.children[index]

        return self.traverse(node, key)

    def traverse(self, node, word, wordlist=[]):
        if any(node.children):
            for index, child in enumerate(node.children):
                if child:
                    newword = word + chr(index + 97)
                    if child.end:
                        wordlist.append(newword)
                    self.traverse(child, newword, wordlist)
            return wordlist
        else:
            if node.end:
                return wordlist
        # return True

def get_words(filename):
    list = []
    inputfile = open(filename).read()
    for word in inputfile.split('\n')[:-1]:
        list.append(word.replace(' ', ''))

    return inputfile.split('\n')[:-1]

def autocomplete(prefix):
    if os.path.exists('auto.p'):
        trie = pickle.load( open( "auto.p", "rb" ) )
    else:
        words = get_words('/usr/share/dict/words')
        # words = get_words('./dictionarytest.txt')
        trie = Trie()

        for word in words:
            trie.insert(word.lower())

        pickle.dump(trie, open( "auto.p", "wb" ))

    all_words = get_words('/usr/share/dict/words')
    all_prefixes = set([word[:len(word)//2] for word in all_words])
    time = benchmark(trie, all_prefixes)
    print('Took {} seconds to benchmark {} prefixes on {} words'.format(time, len(all_prefixes), len(all_words)))



def benchmark(trie, prefixes):
    start_time = time.time()
    print("Starting timer")
    for prefix in prefixes:
        trie.search(prefix.lower())
    return (time.time() - start_time)


def main():
    """Perform main function."""
    start_time = time.time()
    autocomplete(sys.argv[1])

    return


if __name__ == "__main__":
    main()
