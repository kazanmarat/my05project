from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Function works incorrectly!')

if capitalize('') != '':
    raise Exception('Function works incorrectly!')

print('All tests passed!')
