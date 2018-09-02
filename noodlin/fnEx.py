# functions practice

'''Write a function that returns the lesser of two numbers
if both the numbers are even, but greater if one or both
numbers are odd
'''

def lesserOfTwo(num1, num2):
  if num1 % 2 == 0 and num2 % 2 == 0:
    if num1 < num2:
      return num1
    else:
      return num2
  else:
    if num1 < num2:
      return num2
    else:
      return num1
