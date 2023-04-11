def find_odd_or_pair(*args):
    odd_or_pair = ''
    for numbers in args:
        if numbers % 2 == 0:
            odd_or_pair += f'O número {numbers} é par\n'
        else:
            odd_or_pair += f'O número {numbers} é ímpar\n'
    return odd_or_pair

testing_odd_or_pair = find_odd_or_pair(1,2,3,4,5,6,7,8,9)

print(testing_odd_or_pair)
