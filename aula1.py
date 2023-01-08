# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/regex.html#regex-howto

import re

# findall search sub
# compile

string = 'Este é um teste de expressões teste regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCDE', string))

print('#' * 50)

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ASDFG', string))
