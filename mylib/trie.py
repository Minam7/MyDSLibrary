def create_empty_alphabet_dictionary():
    dict_out = {}
    for i in range(ord('a'), ord('z') + 1):
        dict_out[chr(i)] = None
    return dict_out


class Node:
    def __init__(self, key_in):
        self.key = key_in
        self.children = create_empty_alphabet_dictionary()
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, string_in):
        walker = self.root

        for i in range(len(string_in)):
            node_char = walker.children[string_in[i]]
            if node_char is None:
                # the character is not in this node so create a new node
                new_node = Node(string_in[i])
                if i == len(string_in) - 1:
                    # this is the last character so make end true!
                    new_node.isEnd = True

                walker.children[string_in[i]] = new_node
                walker = new_node
            else:
                # the character is already in the tree
                if i == len(string_in) - 1:
                    # this is the last character so make end true!
                    node_char.isEnd = True
                walker = node_char
        return

    def find(self, string_in):
        walker = self.root
        for i in range(len(string_in)):
            node_char = walker.children[string_in[i]]
            if node_char is None:
                # item is not found
                return False
            if i == len(string_in) - 1 and node_char.isEnd is True:
                return True

            walker = node_char

        return False
