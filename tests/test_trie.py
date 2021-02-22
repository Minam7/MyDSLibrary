from mylib.trie import Trie


def test_trie_functins():
    # Test insert
    t = Trie()
    t.insert('ab')

    answer = None
    assert t.root.children['a'] != answer
    assert t.root.children['a'].children['b'] != answer

    # Test find
    answer = False
    assert t.find('a') == answer

    answer = True
    assert t.find('ab') == answer

    answer = False
    assert t.find('aba') == answer

    answer = False
    assert t.find('aaa') == answer

    # insert and existing item
    t.insert('a')
    answer = True
    assert t.root.children['a'].isEnd == answer

    # Test find
    answer = True
    assert t.find('a') == answer

    answer = True
    assert t.find('ab') == answer

    answer = False
    assert t.find('aba') == answer

    answer = False
    assert t.find('aaa') == answer

    # insert already existing string
    t.insert('a')
    answer = None
    assert t.root.children['a'].children.get('a') == answer

    answer = True
    assert t.find('a') == answer
