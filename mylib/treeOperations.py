from collections import deque

from mylib.binarySearchTree import Node


def minimal_tree(array_in):
    if array_in is None or len(array_in) == 0:
        return None

    if len(array_in) == 1:
        return Node(array_in[0], None)

    middle = len(array_in) // 2

    root = Node(array_in[middle], None)
    if middle == 0:
        return root

    left_child = minimal_tree(array_in[:middle])
    left_child.parent = root
    root.left_child = left_child

    if middle + 1 >= len(array_in):
        return root

    right_child = minimal_tree(array_in[middle + 1:])
    right_child.parent = root
    root.right_child = right_child

    return root


def list_of_depth(bt_in):
    # implement list of depth using BFS

    if bt_in is None or bt_in.root is None:
        return None

    linked_lists = []
    # level 0: root
    new_list = deque()
    new_list.append(bt_in.root)

    while new_list:
        linked_lists.append(new_list)
        parents = new_list

        new_list = deque()
        for node in parents:
            if node.left_child is not None:
                new_list.append(node.left_child)

            if node.right_child is not None:
                new_list.append(node.right_child)

    return linked_lists


def check_height(node_in):
    if node_in is None:
        return -1

    left_height = check_height(node_in.left_child)
    if left_height == float('inf'):
        return float('inf')

    right_height = check_height(node_in.right_child)
    if right_height == float('inf'):
        return float('inf')

    if abs(left_height - right_height) > 1:
        return float('inf')

    return max(left_height, right_height) + 1


def check_balanced(bt_in):
    if bt_in is None or bt_in.root is None:
        return True

    height_check = check_height(bt_in.root)

    if height_check == float('inf'):
        return False

    return True


def validate_bst_helper(node_in, lower_bound, higher_bound):
    if node_in is None:
        return True

    if node_in.key < lower_bound or node_in.key > higher_bound:
        return False

    left_subtree_res = validate_bst_helper(node_in.left_child, lower_bound, node_in.key)
    right_subtree_res = validate_bst_helper(node_in.right_child, node_in.key, higher_bound)

    if left_subtree_res is False or right_subtree_res is False:
        return False

    return True


def validate_bst(bt_in):
    if bt_in is None or bt_in.root is None:
        return True

    result = validate_bst_helper(bt_in.root, float('-inf'), float('inf'))

    return result


def first_common_helper(node_in, q_in, p_in):
    if node_in is None or q_in is None or p_in is None:
        return None, False

    if node_in == q_in and node_in == p_in:
        return node_in, True

    left_ans, left_is_ans = first_common_helper(node_in.left_child, q_in, p_in)
    if left_is_ans:  # found ancestor!
        return left_ans, True

    right_ans, right_is_ans = first_common_helper(node_in.right_child, q_in, p_in)
    if right_is_ans:  # found ancestor!
        return right_ans, True

    if left_ans is not None and right_ans is not None:
        return node_in, True  # we found two nodes in either side so this is the ancestor

    elif node_in == p_in or node_in == q_in:  # we are at p or q
        # check if one of p or q is child of the other!
        cur_is_ans = left_ans is not None or right_ans is not None
        # this also handles if the node doesn't exist in the tree
        return node_in, cur_is_ans

    else:
        if left_ans is None:
            return right_ans, False
        else:
            return left_ans, False


def first_common_ancestor(bt_in, q_in, p_in):
    if bt_in is None or bt_in.root is None or q_in is None or p_in is None:
        return None

    if bt_in.root == q_in and bt_in.root == p_in:
        return bt_in.root

    res, is_anc = first_common_helper(bt_in.root, q_in, p_in)
    if is_anc:
        return res

    return None


def weave_two_sequence(seq_in1, seq_in2, prefix_in, result_in):
    # input is two deques!
    if not seq_in1 or not seq_in2:
        # one is empty
        new_prefix = prefix_in.copy()
        new_prefix.extend(seq_in1)
        new_prefix.extend(seq_in2)
        result_in.append(new_prefix)
        return

    # removing from first
    prefix_in.append(seq_in1.popleft())
    weave_two_sequence(seq_in1, seq_in2, prefix_in, result_in)
    seq_in1.appendleft(prefix_in.pop())

    # removing from second
    prefix_in.append(seq_in2.popleft())
    weave_two_sequence(seq_in1, seq_in2, prefix_in, result_in)
    seq_in2.appendleft(prefix_in.pop())


def bst_sequence_helper(node_in):
    seq_result = []

    if node_in is None:
        return [deque()]

    prefix = deque()
    prefix.append(node_in.key)

    left_seq = bst_sequence_helper(node_in.left_child)
    right_seq = bst_sequence_helper(node_in.right_child)

    for lf in left_seq:
        for lr in right_seq:
            weaves = []
            weave_two_sequence(lf, lr, prefix, weaves)
            seq_result.extend(weaves)

    return seq_result


def bst_sequence(bst_in):
    if bst_in is None or bst_in.root is None:
        return []

    return bst_sequence_helper(bst_in.root)


def match_tree(root_in1, root_in2):
    if root_in1 is None and root_in2 is None:
        return True
    elif root_in1 is None or root_in2 is None:
        return False
    elif root_in1.key != root_in2.key:
        return False
    else:
        return match_tree(root_in1.left_child, root_in2.left_child) and match_tree(root_in1.right_child,
                                                                                   root_in2.right_child)


def contain_tree_helper(tree_node_in1, tree_node_in2):
    # find T2 in T1 and then call match tree for that
    if tree_node_in1 is None:
        return False  # T2 is not in T1

    if tree_node_in1.key == tree_node_in2.key:
        subtree_res = match_tree(tree_node_in1, tree_node_in2)
        if subtree_res is True:
            return True

    else:
        return contain_tree_helper(tree_node_in1.left_child, tree_node_in2) or contain_tree_helper(
            tree_node_in1.right_child, tree_node_in2)


def contains_tree(bt_in1, bt_in2):
    if bt_in1 is None or bt_in1.root is None:
        return False
    if bt_in2 is None or bt_in2.root is None:
        return True

    return contain_tree_helper(bt_in1.root, bt_in2.root)


def path_sum_helper(node_in, target_sum_in, running_sum_in, paths_hash_in):
    if node_in is None:
        return 0

    running_sum_in += node_in.key

    paths = 0
    if (running_sum_in - target_sum_in) in paths_hash_in:
        paths = paths_hash_in[running_sum_in - target_sum_in]

    if running_sum_in == target_sum_in:
        paths += 1

    # add current sum to paths
    if running_sum_in in paths_hash_in:
        paths_hash_in[running_sum_in] += 1
    else:
        paths_hash_in[running_sum_in] = 1

    paths += path_sum_helper(node_in.left_child, target_sum_in, running_sum_in, paths_hash_in)
    paths += path_sum_helper(node_in.right_child, target_sum_in, running_sum_in, paths_hash_in)

    # remove current sum from path after calculation

    if paths_hash_in[running_sum_in] == 1:
        del paths_hash_in[running_sum_in]
    else:
        paths_hash_in[running_sum_in] -= 1

    return paths


def path_with_sum(bt_in, target_sum):
    if bt_in is None or bt_in.root is None:
        return 0

    return path_sum_helper(bt_in.root, target_sum, 0, paths_hash_in={})
