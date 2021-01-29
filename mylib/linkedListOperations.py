from mylib.linkedList import SingleLink, Node


def remove_dups(ll_in):
    # unsorted linked list as an input
    if ll_in is None:
        return None

    if ll_in.head is None:
        return None

    walker = ll_in.head
    seen = {walker.value: 1}
    while walker.next is not None:
        if walker.next.value in seen:
            # next node is duplicate
            # delete next node
            walker.next = walker.next.next
        else:
            seen[walker.next.value] = 1
            walker = walker.next

    return


def k_to_last(ll_in, k_in):
    # linked list as an input
    if ll_in is None:
        return None

    if ll_in.head is None:
        return None

    end = ll_in.head
    start = ll_in.head
    diff = 0
    while end.next is not None:
        end = end.next

        if diff == k_in:
            start = start.next

        if diff < k_in:
            diff += 1
    if diff != k_in:
        return None

    return start


def delete_middle_node(node_in):
    if node_in is None:
        return None

    if node_in.next is None:
        raise ValueError('You can not delete the last node.')

    node_in.value, node_in.next.value = node_in.next.value, node_in.value
    node_in.next = node_in.next.next

    return


def linked_partition(ll_in, x_in):
    # x shows the partition limit
    if ll_in is None:
        return None

    if ll_in.head is None:
        return None

    partition_holder = None
    walker = ll_in.head
    while walker is not None:
        if walker.value >= x_in and partition_holder is None:
            # set partition_holder
            partition_holder = walker

        if walker.value < x_in and partition_holder is not None:
            # swap the value with partition holder
            walker.value, partition_holder.value = partition_holder.value, walker.value
            partition_holder = partition_holder.next

        walker = walker.next


def sum_list_rev(ll_in1, ll_in2):
    # ll_in1 is a linked list with digit reversed
    # ll_in2 is a linked list with digit reversed
    # response is a linked list with digit reversed
    if ll_in1 is None or ll_in2 is None:
        return None

    if ll_in1.head is None or ll_in2.head is None:
        return None

    response = SingleLink()
    answer_walker = None
    walker1 = ll_in1.head
    walker2 = ll_in2.head
    carry = 0
    while walker1 is not None or walker2 is not None:
        one_digit_sum = 0

        if walker1 is not None and walker2 is not None:
            # same length
            one_digit_sum = walker1.value + walker2.value + carry
            walker1 = walker1.next
            walker2 = walker2.next
        elif walker2 is None:
            # ll1 is larger
            one_digit_sum = walker1.value + carry
            walker1 = walker1.next
        elif walker1 is None:
            # ll2 is larger
            one_digit_sum = walker2.value + carry
            walker2 = walker2.next

        if one_digit_sum > 10:
            carry = 1
            one_digit_sum -= 10
        else:
            carry = 0

        if response.head is None:
            # first digit
            response.head = Node(one_digit_sum, None)
            answer_walker = response.head
        else:
            # other digit
            answer_walker.next = Node(one_digit_sum, None)
            answer_walker = answer_walker.next

    if carry != 0:
        # last number
        # other digit
        answer_walker.next = Node(carry, None)

    return response


def insert_at_first(ll_in, value_in):
    if ll_in is None:
        return None

    new_node = Node(value_in, ll_in.head)
    ll_in.head = new_node


def zero_pad(ll_in, length_in):
    if ll_in is None:
        return None

    for i in range(length_in):
        insert_at_first(ll_in, 0)


def sum_list_helper(node_in1, node_in2):
    # return carry and head of the linked list
    if node_in1 is None and node_in2 is None:
        new_ll = SingleLink()
        return 0, new_ll

    carry, new_head = sum_list_helper(node_in1.next, node_in2.next)
    one_digit_sum = node_in1.value + node_in2.value + carry

    if one_digit_sum > 10:
        carry = 1
        one_digit_sum -= 10
    else:
        carry = 0

    insert_at_first(new_head, one_digit_sum)

    return carry, new_head


def sum_list(ll_in1, ll_in2):
    # ll_in1 is a linked list with digits
    # ll_in2 is a linked list with digits
    # response is a linked list with digits
    if ll_in1 is None or ll_in2 is None:
        return None

    if ll_in1.head is None or ll_in2.head is None:
        return None

    # make the lengths the same
    length_diff = ll_in1.size() - ll_in2.size()
    if length_diff > 0:
        # zeropad ll_in2
        zero_pad(ll_in2, length_diff)

    elif length_diff < 0:
        # zeropad ll_in1
        zero_pad(ll_in1, (-1) * length_diff)

    carry, result = sum_list_helper(ll_in1.head, ll_in2.head)

    if carry != 0:
        insert_at_first(result, carry)

    return result


def list_palindrome_helper(node_in, length_in):
    if length_in == 0:
        return node_in, True
    if length_in == 1:
        return node_in.next, True

    back_node, rec_res = list_palindrome_helper(node_in.next, length_in - 2)
    if rec_res is False:
        return back_node, False

    else:
        if node_in.value != back_node.value:
            return node_in, False
        else:
            return back_node.next, True


def list_palindrome(ll_in):
    if ll_in is None:
        return True

    if ll_in.head is None:
        return True

    ll_length = ll_in.size()
    _, result = list_palindrome_helper(ll_in.head, ll_length)

    return result


def find_length_last(ll_in):
    # find the length of a linked list with the last node
    walker = ll_in.head
    length_out = 0
    while walker.next is not None:
        length_out += 1
        walker = walker.next

    return length_out, walker


def list_intersect(ll_in1, ll_in2):
    if ll_in1 is None or ll_in2 is None:
        return None, False

    if ll_in1.head is None or ll_in2.head is None:
        return None, False

    # finding length and last node
    length1, last_node1 = find_length_last(ll_in1)
    length2, last_node2 = find_length_last(ll_in2)

    if last_node1 != last_node2:
        # not intersecting
        return None, False

    # finding the intersection now
    shorter_walker, longer_walker = ll_in1.head, ll_in2.head
    length_diff = length1 - length2
    if length_diff > 0:
        shorter_walker, longer_walker = ll_in2.head, ll_in1.head

    # move longer walker as difference
    for i in range(length_diff):
        longer_walker = longer_walker.next

    while shorter_walker.next is not None:
        if shorter_walker == longer_walker:
            break
        else:
            shorter_walker = shorter_walker.next
            longer_walker = longer_walker.next

    return shorter_walker, True


def list_loop_detection(ll_in):
    # return the loop starting node, None otherwise
    if ll_in is None:
        return None

    if ll_in.head is None:
        return None

    if ll_in.head.next is None:
        return None

    walker = ll_in.head
    runner = ll_in.head

    while runner is not None and runner.next is not None:
        walker = walker.next
        runner = runner.next.next
        if runner == walker:
            # finding the loop
            walker = ll_in.head
            break

    if runner is None or runner.next is None:
        return None

    # we have loop
    while walker != runner:
        walker = walker.next
        runner = runner.next

    return walker


if __name__ == '__main__':
    l_list1 = SingleLink()
    l_list1.insert_after('A', None)
    l_list1.insert_after('B', 'A')
    l_list1.insert_after('C', 'B')
    l_list1.insert_after('D', 'C')
    l_list1.insert_after('E', 'D')
    find_node1 = l_list1.find('E')
    find_node2 = l_list1.find('C')
    find_node1.next = find_node2

    print(l_list1.head.value)
    print(list_loop_detection(l_list1).value)
