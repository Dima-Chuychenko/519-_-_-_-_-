def compare_regex(pattern, string):
    if pattern == '':
        return True
    elif string == '':
        return pattern == ''

    if pattern[0] == '^':
        return compare_regex_start(pattern[1:], string)
    elif pattern[-1] == '$':
        return compare_regex_end(pattern[:-1], string)
    elif pattern[0] == '.':
        return compare_regex(pattern[1:], string[1:])
    elif pattern[0] == '/':
        return pattern[1] == string[0] and compare_regex(pattern[2:], string[1:])
    elif pattern[0] == string[0]:
        return compare_regex(pattern[1:], string[1:])
    elif pattern[0] == '?':
        return compare_regex(pattern[1:], string) or compare_regex(pattern[2:], string[1:])
    elif pattern[0] == '*':
        return compare_regex(pattern[1:], string) or (pattern[1] == string[0] and compare_regex(pattern, string[1:]))
    elif pattern[0] == '+':
        return pattern[1] == string[0] and compare_regex(pattern[2:], string[1:])
    else:
        return False


def compare_regex_start(pattern, string):
    if pattern == '':
        return True
    elif string == '':
        return False

    if pattern[0] == '.':
        return compare_regex_start(pattern[1:], string[1:])
    elif pattern[0] == '/':
        return pattern[1] == string[0] and compare_regex_start(pattern[2:], string[1:])
    elif pattern[0] == string[0]:
        return compare_regex_start(pattern[1:], string[1:])
    else:
        return False


def compare_regex_end(pattern, string):
    if pattern == '':
        return True
    elif string == '':
        return False

    if pattern[-1] == '.':
        return compare_regex_end(pattern[:-1], string[:-1])
    elif pattern[-1] == '/':
        return len(pattern) >= 2 and pattern[-2] == string[-1] and compare_regex_end(pattern[:-2], string[:-1])
    elif pattern[-1] == string[-1]:
        return compare_regex_end(pattern[:-1], string[:-1])
    else:
        return False


def compare_regex_pairs(pattern, string):
    if len(pattern) == len(string):
        return compare_regex(pattern, string)
    elif len(pattern) < len(string):
        for i in range(len(string) - len(pattern) + 1):
            if compare_regex(pattern, string[i:]):
                return True
    else:  # len(pattern) > len(string)
        for i in range(len(pattern) - len(string) + 1):
            if compare_regex(pattern[i:], string):
                return True
    return False


print(compare_regex_pairs('/.$', 'end.'))
print(compare_regex_pairs('3/+3', '3+3=6'))
print(compare_regex_pairs('/?', 'Is this working?'))
print(compare_regex_pairs('//', '/'))
print(compare_regex_pairs('colou/?r', 'color'))
print(compare_regex_pairs('colou/?r', 'colour'))

print(compare_regex_pairs('/$', '$'))
print(compare_regex_pairs('le$', 'apple'))
