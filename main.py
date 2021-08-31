def skip_blanks(input_string, index):
    while index < len(input_string)\
            and input_string[index] == ' ':
        index += 1
    return index


def get_left_bracket(input_string, index):
    index = skip_blanks(input_string, index)
    if input_string[index] == '(':
        return '(', index+1
    raise Exception('get_left_bracket')


def get_right_bracket(input_string, index):
    while input_string[index] != ')':
        index += 1
    return ')', index+1


def get_operator(input_string, index):
    index = skip_blanks(input_string, index)
    operators = ('and', 'or', 'xor', 'sub')
    for operator in operators:
        if input_string.startswith(operator, index):
            return operator, index+1+len(operator)
    return '', index


def parse_range(range_string):
    numbers = range_string.split('-')
    if len(numbers) == 1:
        return {int(numbers[0])}
    if len(numbers) == 2:
        start = int(numbers[0])
        end = int(numbers[1])
        return set(range(start, end+1))
    raise Exception('parse_range')


def parse_sentence(sentence):
    sentence = sentence.split(',')
    ret = set()
    for x in sentence:
        ret = ret | parse_range(x)
    return ret


def get_one_set(input_string, index):
    _, left_index = get_left_bracket(input_string, index)
    _, right_index = get_right_bracket(input_string, left_index)
    sentence = input_string[left_index:right_index-1]
    sentence = parse_sentence(sentence)
    return sentence, right_index


def do_operator(set_left, operator, set_right):
    if operator == 'or':
        return set_left | set_right
    elif operator == 'and':
        return set_left & set_right
    elif operator == 'xor':
        return set_left ^ set_right
    elif operator == 'sub':
        return set_left - set_right
    raise Exception('do_operator')


def set_calc(input_string):
    index = 0

    ret = set()
    operator = 'or'

    while operator:
        sentence, index = get_one_set(input_string, index)
        ret = do_operator(ret, operator, sentence)
        operator, index = get_operator(input_string, index)

    return ret
