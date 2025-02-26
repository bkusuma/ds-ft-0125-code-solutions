# %%
# Name: letters_to_symbols
# Purpose: encode  string so that the amount of letters will be represented by a number and the letter
# Inputs:   1. take one parameter, a string named ‘s’
# Outputs:  1. encoded string
# Side effects: none

def letters_to_symbols(s):
    output_string = "" # initialize output string
    previous_letter = s[0] # initialize letter
    counter = 0 # initialize counter
    for letter in s: # loop over letters in input string
        if previous_letter == letter: # increase counter of same letter
            counter += 1
        else:
            output_string = output_string + str(counter) + previous_letter # add count of letters and letter to output string
            previous_letter = letter
            counter = 1
    output_string = output_string + str(counter) + previous_letter # capture final letter(s) that won't go through loop

    return output_string

s = "AAAABBBCCDAAA"

print(letters_to_symbols(s))


