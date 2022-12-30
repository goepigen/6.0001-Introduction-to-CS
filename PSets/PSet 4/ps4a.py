# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # base case
    # if length of the string is 1, return an array with just the string inside
    # recursion case
    # save first letter to a variable fl
    # recurse on the rest of the string
    # take the result and for each entry, compute all permutations

    # base case
    if len(sequence) == 1:
        return [sequence]

    first_letter = sequence[0]

    rec_permutations = get_permutations(sequence[1:])
    permutations = []

    for p in rec_permutations:
        for j in range(len(p)+1):
            permutations.append(p[0:j] + first_letter + p[j:])
    return permutations


if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'bus'
    print('Input:', example_input)
    print('Expected Output:', ['bus', 'ubs', 'usb', 'bsu', 'sbu', 'sub'])
    print('Actual Output:', get_permutations(example_input))
