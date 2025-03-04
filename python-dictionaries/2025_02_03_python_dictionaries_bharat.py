# -*- coding: utf-8 -*-
"""2025/02/03 python-dictionaries-bharat

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jDggR8VF_KZnYWKwLW6m8FmqpQhZL7gs
"""

def binary_dict(num):
  binary_list = []
  for number in range(num+1):
    converted_number = bin(number)[2:]
    binary_list.append(converted_number)
  counter_list = range(num+1)
  zip_list = list(zip(counter_list, binary_list))
  return dict(zip_list)

binary_dict(15)

binaries = [bin(number)[2:] for number in range(16)]
binaries