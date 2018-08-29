states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']

import re


def remove_punctuation(value):
    return re.sub('[!#?]', '', value)


clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings(string, ops):
    result = []
    for value in string:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


print(clean_strings(states, clean_ops))
