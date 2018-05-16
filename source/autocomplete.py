import sys, re, time, pickle, os

# Python program for insert and search
# operation in a Trie

class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.getNode()
            node = node.children[char]

        node.end = True

    def search(self, prefix):
        node = self.root
        wordlist = []

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.end:
            wordlist.append(prefix)

        return self.traverse(node, prefix, wordlist)

    def traverse(self, node, word, wordlist):
        # If it has children, keeep going
        if any(node.children):
            # For every item in the children
            for key in node.children:
                child = node.children[key]
                newword = word + key
                # If it's a proper word
                if child.end:
                    wordlist.append(newword)
                # Keep going!
                self.traverse(child, newword, wordlist)
            return wordlist
        # Else, just return the word list
        else:
            return wordlist

def get_words(filename):
    list = []
    inputfile = open(filename).read()
    for word in inputfile.split('\n')[:-1]:
        list.append(word.replace(' ', ''))

    return inputfile.split('\n')[:-1]

def autocomplete(prefix):
    start_time = time.time()

    # if os.path.exists('auto.p'):
    #     trie = pickle.load( open( "auto.p", "rb" ) )
    #     all_words = pickle.load( open("word.p", "rb") )
    # else:
    all_words = get_words('/usr/share/dict/words')
    # all_words = get_words('./dictionarytest.txt')
    trie = Trie()

    for word in all_words:
        trie.insert(word.lower())

    # print(trie.search(prefix))
        # pickle.dump(trie, open( "auto.p", "wb" ))
        # pickle.dump(all_words, open( "word.p", "wb") )

    all_prefixes = set([word[:len(word)//2] for word in all_words])
 #
    print("Dictionary build time: {} seconds".format(time.time() - start_time))

    bench_time = benchmark(trie, all_prefixes)
    print('Took {} seconds to benchmark {} prefixes on {} words'.format(bench_time, len(all_prefixes), len(all_words)))



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
    print("Total time, counting dict build: {} seconds".format(time.time() - start_time))

    return


if __name__ == "__main__":
    main()
