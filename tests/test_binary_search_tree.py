from mylib.binarySearchTree import BinarySearchTree, AugmentedBinarySearchTree


def test_bst_insert():
    # Test BST insert
    bst = BinarySearchTree()

    data = [14, 7, 18, 5, 8, 9]
    bst.build_tree(data)

    assert str(bst.root) == '14'
    assert str(bst.root.left_child) == '14->7'
    assert str(bst.root.left_child.right_child) == '14->7->8'


def test_bst_find():
    # Test BST find
    bst = BinarySearchTree()

    data = [14, 7, 18, 5, 8, 9]
    bst.build_tree(data)

    assert bst.find(12) is None
    assert str(bst.find(8)) == '14->7->8'
    assert str(bst.find(14) == '14')


def test_bst_min_max():
    # Test find min and find max
    bst = BinarySearchTree()

    data = [14, 7, 18, 5, 8, 9]
    bst.build_tree(data)
    assert str(bst.find_min()) == '14->7->5'
    assert str(bst.find_max()) == '14->18'


def test_bst_find_larger():
    # Test find larger
    bst = BinarySearchTree()

    data = [14, 7, 18, 5, 8, 9]
    bst.build_tree(data)

    # checking by finding next parent
    node = bst.find(9)
    assert str(bst.next_larger(node)) == '14'
    # checking right subtree
    node = bst.find(14)
    assert str(bst.next_larger(node)) == '14->18'


def test_bst_delete():
    # Test delete
    bst = BinarySearchTree()

    data = [14, 7, 18, 5, 9, 11, 8, 16, 20, 17, 22]
    bst.build_tree(data)

    bst.delete(14)
    assert str(bst.root) == '16'
    assert bst.find(14) is None
    assert str(bst.find(18)) == '16->18'


def test_bst_inorder():
    # Test in-order traversal
    bst = BinarySearchTree()
    c = [5, 3, 7, 0, -1, 2, 4, 10, 23]
    bst.build_tree(c)

    answer = [-1, 0, 2, 3, 4, 5, 7, 10, 23]
    test_root = bst.find(5)
    assert str(test_root) == '5'  # 5 is root!

    assert bst.in_order_traversal(test_root) == answer


def test_aug_bst_insert():
    # Test BST insert
    bst = AugmentedBinarySearchTree()

    data = [14, 7, 18, 5, 8, 9]
    bst.build_tree(data)

    assert bst.root.size == 6
    assert bst.root.left_child.size == 4
    assert bst.root.left_child.right_child.size == 2
    assert bst.root.right_child.size == 1
