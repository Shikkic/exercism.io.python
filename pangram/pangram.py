
# is_pangram returns if a string uses every character of the alphabet
# atlest once. Returns true if is_pangram, flase if not (or empty).
def is_pangram(input):
    # If input is empty, or less than num of lettes in alphabet
    # return false
    if len(input) < 1 or len(input) < 26:
        return False

    # Create a dictionary where we will store all the letters we use.
    alphabetDict = {}
    # Loop over every character in the input string (lowercased).
    for char in input.lower():
        # If char is an alph char and our dict does not have our character,
        # store it.
        if char.isalpha() and not alphabetDict.has_key(char):
            alphabetDict[char] = 1

    # If our dict does not contain 26 characters, return false.
    if len(alphabetDict) < 26:
        return False

    return True
