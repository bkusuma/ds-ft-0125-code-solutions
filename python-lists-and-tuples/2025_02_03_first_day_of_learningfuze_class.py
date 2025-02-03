# -*- coding: utf-8 -*-
"""2025/02/03 First day of LearningFuze class

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TY7V5vw00_qvT-Y7y7jRSXKSJLs0KHOx
"""



"""# Python Review

## Exercise 1
"""

def alpha_num_tuple(string):
  list_of_tuples = []
  counter = 1
  for letter in string:
    alpha_num = (counter, letter)
    counter += 1
    list_of_tuples.append(alpha_num)
  return list_of_tuples

L = "abcdefghijklmnopqrstuvwxyz"

print(alpha_num_tuple(L))

list_tuples = alpha_num_tuple(L)

dict(list_tuples)

"""## Josh's solution"""

# creating a function to make a list

def alpha_index(letters):
  indices = range(1, len(alpha) + 1)
  return list(zip(indices, letters))

alpha = "abcdefghijklmnopqrstuvwxyz"

alpha_index(alpha)

