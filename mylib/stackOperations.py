from mylib.stackNode import StackNode


def sorted_insertion(random_stack, sorted_stack_in, item_in):
    # insert item_in into sorted stack, using random_stack as buffer
    popped_count = 0
    if sorted_stack_in.is_empty() is False and sorted_stack_in.peek() < item_in:
        sorted_stack_in.push(item_in)
        return
    else:
        while sorted_stack_in.is_empty() is False and sorted_stack_in.peek() >= item_in:
            random_stack.push(sorted_stack_in.pop())
            popped_count += 1
        sorted_stack_in.push(item_in)
        while popped_count > 0:
            sorted_stack_in.push(random_stack.pop())
            popped_count -= 1
    return


def sort_stack(stack_in):

    if stack_in is None:
        return None
    if stack_in.is_empty():
        return stack_in

    if stack_in.size() == 1:
        return stack_in

    first = stack_in.pop()
    second = stack_in.pop()

    sorted_stack = StackNode()

    if first < second:
        sorted_stack.push(first)
        sorted_stack.push(second)
    else:
        sorted_stack.push(second)
        sorted_stack.push(first)

    while stack_in.is_empty() is False:
        first = stack_in.pop()
        sorted_insertion(stack_in, sorted_stack, first)

    return sorted_stack
