from mylib.AVLTree import AVLTree, Node


def test_avl_functions():
    # Test AVL Build
    avl = AVLTree()

    data = [41, 20, 65, 50, 29, 26, 11]
    avl.build_tree(data)

    assert str(avl.root) == '41'
    assert str(avl.root.left_child) == '41->26'
    assert str(avl.root.left_child.right_child) == '41->26->29'

    # Insert 23
    test_node = Node(23, None)
    avl.insert(test_node)

    assert str(avl.root.left_child.left_child.right_child) == '41->26->20->23'

    # Test AVL find
    avl.find(12)
    assert avl.find(12) is None
    assert str(avl.find(26)) == '41->26'

    # Test find min and find max
    assert str(avl.find_min()) == '41->26->20->11'
    assert str(avl.find_max()) == '41->65'

    # Test find larger
    # checking by finding next parent
    node = avl.find(29)
    assert str(node) == '41->26->29'
    assert str(avl.next_larger(node)) == '41'

    # checking right subtree
    node = avl.find(20)
    assert str(node) == '41->26->20'
    assert str(avl.next_larger(node)) == '41->26->20->23'


def test_avl_inorder():
    # Test in-order traversal
    avl = AVLTree()
    c = [5, 3, 7, 0, -1, 2, 4, 10, 23]
    avl.build_tree(c)

    answer = [-1, 0, 2, 3, 4, 5, 7, 10, 23]

    ans = avl.in_order_traversal(avl.root)
    assert ans == answer
