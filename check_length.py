# -*- coding: utf-8 -*-
"""check_length.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ithyaVf3G0Q7eYilGfeIY87QRDJ2sj5o

***8. Check to see if the length of the word is greater than 2 (as it was researched that there is no adjective in 2-letters)**
"""

def check_length(word):
  if (len(word) > 2):
    st = word + " is more than 2 characters long."
  else:
    st = word + " is NOT more than 2 characters long."
  print(st)

check_length("ab")

check_length("abc")