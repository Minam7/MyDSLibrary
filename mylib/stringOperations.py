def is_unique(string_in):
    if string_in is not None:
        already_chars = {}
        for c in str(string_in):
            if c.lower() in already_chars:
                return False
            else:
                already_chars[c.lower()] = 1
        return True
    return True


def is_permutation(string_in1, string_in2):
    if string_in1 is None or string_in2 is None:
        return False

    if len(str(string_in1)) != len(str(string_in2)):
        return False

    s1_dict = {}
    for c in str(string_in1):
        if c not in s1_dict:
            s1_dict[c] = 1
        else:
            s1_dict[c] += 1

    for c in str(string_in2):
        if c not in s1_dict:
            return False
        else:
            if s1_dict[c] == 0:
                return False
            s1_dict[c] -= 1

    return True


def urlify(string_in, length_in):
    if string_in is None:
        return None

    response = ''
    for c in str(string_in):
        if c == ' ':
            response += '%20'
            length_in += 2
        else:
            response += c
        if len(response) == length_in:
            return response

    return response


def palindrome_permutation(string_in):
    if string_in is None:
        return True

    words = {}
    for c in str(string_in):
        char = c.lower()
        if char != ' ':
            if char not in words:
                words[char] = 1
            else:
                words[char] += 1

    odd_chars = ''
    for key, value in words.items():
        if value % 2 == 1:
            odd_chars += key

        if len(odd_chars) > 1:
            return False
    return True


def one_away(string_in1, string_in2):
    # handling none
    if string_in1 is None and string_in2 is None:
        return True
    if string_in1 is None and string_in2 is not None:
        if len(string_in2) < 2:
            return True
        else:
            return False
    if string_in2 is None and len(string_in1) < 2:
        return True

    if (len(string_in1) - len(string_in2)) > 1 or (len(string_in1) - len(string_in2)) < -1:
        return False

    index1 = 0
    index2 = 0
    if len(string_in1) > len(string_in2):
        string_in1, string_in2 = string_in2, string_in1

    # string 1 is always the shortest one
    onediff = False

    while index1 < len(string_in1) and index2 < len(string_in2):
        if string_in1[index1] != string_in2[index2]:
            # second change
            if onediff:
                return False

            onediff = True

            # replace situation
            if len(string_in1) == len(string_in2):
                index1 += 1
        else:
            index1 += 1
        index2 += 1

    return True


def string_compression(string_in):
    if string_in is None:
        return None

    compressed_list = []
    compressed_length = 0
    previous_char = ''
    repeat = 1

    for c in str(string_in):
        if previous_char == '':
            previous_char = c
        else:
            if c == previous_char:
                # repetition
                repeat += 1
            else:
                # new character
                compstr = ''.join((previous_char, str(repeat)))
                compressed_length += len(compstr)
                compressed_list.append(compstr)
                repeat = 1
                previous_char = c

    compstr = ''.join((previous_char, str(repeat)))
    compressed_length += len(compstr)
    compressed_list.append(compstr)

    if compressed_length > len(string_in):
        return string_in

    response = ''.join(compressed_list)

    return response


def rotate_matrix(matrix_in):
    if matrix_in is None:
        return None

    # empty case
    if len(matrix_in) == 0:
        return []

    # non square case
    if len(matrix_in) != len(matrix_in[0]):
        return None

    # matrix: [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    # handling layers
    for i in range((len(matrix_in) // 2) + 1):
        length = len(matrix_in) - 2 * i
        # swapping for each offset
        for j in range(length - 1):
            # swap inplace for each 4
            if j == 0:
                # swap corners

                # top -> right
                temp = matrix_in[i][i + j + length - 1]
                matrix_in[i][i + j + length - 1] = matrix_in[i][i + j]
                # right -> bottom
                temp, matrix_in[i + j + length - 1][i + j + length - 1] = \
                    matrix_in[i + j + length - 1][i + j + length - 1], temp
                # bottom -> left
                temp, matrix_in[i + j + length - 1][i] = matrix_in[i + j + length - 1][i], temp
                # left -> top
                matrix_in[i][i + j] = temp

            else:
                # top -> right
                temp = matrix_in[i + j][i + length - 1]
                matrix_in[i + j][i + length - 1] = matrix_in[i][i + j]
                # right -> bottom
                temp, matrix_in[i + length - 1][i + length - 1 - j] = matrix_in[i + length - 1][
                                                                          i + length - 1 - j], temp
                # bottom -> left
                temp, matrix_in[i + length - 1 - j][i] = matrix_in[i + length - 1 - j][i], temp
                # left -> top
                matrix_in[i][i + j] = temp

    return matrix_in


def set_zero(matrix_in, index_in, col_row):
    # col_row = 0 for col
    # col_row = 1 for row
    if col_row == 0:
        # zero the column
        for k in range(len(matrix_in)):
            matrix_in[index_in][k] = 0

    if col_row == 1:
        # zero the row
        for k in range(len(matrix_in[0])):
            matrix_in[k][index_in] = 0


def zero_matrix(matrix_in):
    if matrix_in is None:
        return None

    if len(matrix_in) == 0:
        return None

    first_row = False
    first_col = False

    # check column
    for i in range(len(matrix_in)):
        if matrix_in[i][0] == 0:
            first_col = True
            break

    # check row
    for i in range(len(matrix_in[0])):
        if matrix_in[0][i] == 0:
            first_row = True
            break

    # setting first row and first column as the indicator for others
    # finding zeroes
    for i in range(1, len(matrix_in)):
        for j in range(1, len(matrix_in[0])):
            if matrix_in[i][j] == 0:
                matrix_in[0][j] = 0
                matrix_in[i][0] = 0

    # setting new zeroes
    # check column
    for i in range(1, len(matrix_in)):
        if matrix_in[i][0] == 0:
            set_zero(matrix_in, i, col_row=1)

    # check row
    for i in range(1, len(matrix_in[0])):
        if matrix_in[0][i] == 0:
            set_zero(matrix_in, i, col_row=0)

    if first_col:
        set_zero(matrix_in, 0, col_row=0)

    if first_row:
        set_zero(matrix_in, 0, col_row=1)

    return matrix_in


def string_rotation(string_in1, string_in2):
    if string_in1 is None and string_in2 is None:
        return True
    if string_in1 is None or string_in2 is None:
        return False

    if len(string_in1) != len(string_in2):
        return False

    repeated = ''.join([string_in2, string_in2])

    '''
    # using in
    if string_in1 in repeated:
        return True
    '''

    # implementation using find
    if repeated.find(string_in1) != -1:
        return True

    return False
